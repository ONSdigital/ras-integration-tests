from logging import getLogger
import time

from selenium.common.exceptions import WebDriverException
from structlog import wrap_logger

from acceptance_tests import browser
from acceptance_tests.features.pages import sign_out_internal
from acceptance_tests.features.steps import authentication
from config import Config
from controllers import (collection_exercise_controller, database_controller, sample_controller,
                         party_controller, django_oauth_controller, case_controller,
                         collection_instrument_controller)

logger = wrap_logger(getLogger(__name__))


def after_all(context):
    """
    Close the browser after testing. See https://pythonhosted.org/behave/tutorial.html#environmental-controls
    """
    browser.quit()


def before_all(context):
    try:
        database_controller.execute_rm_sql('resources/database/database_reset_rm.sql')
        database_controller.reset_ras_database()
        authentication.signed_in_internal(context)
        prepare_collection_exercises()
        execute_collection_exercises()
        register_respondent(survey_id='cb8accda-6118-4d3b-85a3-149e28960c54', period='201801')
        sign_out_internal.sign_out()
    except WebDriverException:
        logger.exception('Failed to setup before running tests', html=browser.html)


def before_scenario(_, scenario):
    if "skip" in scenario.effective_tags:
        scenario.skip("Marked with @skip")
        return


def prepare_collection_exercises():
    # for us028
    rsi_id = '75b19ea0-69a4-4c58-8d7f-4458c8f43f5c'
    periods = ('201812', '201811')
    sample_file = 'resources/sample_files/business-survey-sample-date.csv'
    ci_path = 'resources/collection_instrument_files/064_0001_201803.xlsx'

    for period in periods:
        logger.info('Loading sample', survey='rsi', period=period)
        sample_controller.load_sample('rsi', period, sample_file)

        logger.info('Loading collection instrument', survey='rsi', period=period)
        ce = collection_exercise_controller.get_collection_exercise(rsi_id, period)
        collection_instrument_controller.upload_collection_instrument(ce['id'], ci_path)


def before_step(context, step):
    try:
        context.survey, context.survey_period = next(tag.split('_')[1:] for tag in context.tags if tag.startswith('ce'))
    except StopIteration:
        context.survey = context.survey_period = None


def after_step(context, step):
    if step.status == "failed":
        logger.exception('Failed step', scenario=context.scenario.name, step=step.name, html=browser.html)


def execute_collection_exercises():
    test_file = 'resources/sample_files/business-survey-sample-date.csv'
    logger.info('Loading sample', survey='bricks', period='201801')
    sample_controller.load_sample('bricks', '201801', test_file)
    logger.info('Loading sample', survey='bricks', period='201812')
    sample_controller.load_sample('bricks', '201812', test_file)
    logger.info('Executing collection exercise', survey_id='cb8accda-6118-4d3b-85a3-149e28960c54', period='201801')
    collection_exercise_controller.execute_collection_exercise(survey_id='cb8accda-6118-4d3b-85a3-149e28960c54',
                                                               period='201801')
    logger.info('Executing collection exercise', survey_id='cb8accda-6118-4d3b-85a3-149e28960c54', period='201812')
    collection_exercise_controller.execute_collection_exercise(survey_id='cb8accda-6118-4d3b-85a3-149e28960c54',
                                                               period='201812')
    logger.info('Waiting for collection exercises execution process to finish',
                survey_id='cb8accda-6118-4d3b-85a3-149e28960c54', period='201801')
    poll_database_for_iac(survey_id='cb8accda-6118-4d3b-85a3-149e28960c54', period='201801')
    logger.info('Waiting for collection exercises execution process to finish',
                survey_id='cb8accda-6118-4d3b-85a3-149e28960c54', period='201812')
    poll_database_for_iac(survey_id='cb8accda-6118-4d3b-85a3-149e28960c54', period='201812')


def poll_database_for_iac(survey_id, period):
    collection_exercise_id = collection_exercise_controller.get_collection_exercise(survey_id, period)['id']
    while True:
        if database_controller.get_iac_for_collection_exercise(collection_exercise_id):
            break
        time.sleep(5)


def register_respondent(survey_id, period):
    collection_exercise_id = collection_exercise_controller.get_collection_exercise(survey_id, period)['id']
    enrolment_code = database_controller.get_iac_for_collection_exercise(collection_exercise_id)
    respondent_party = party_controller.register_respondent(email_address=Config.RESPONDENT_USERNAME,
                                                            first_name='first_name',
                                                            last_name='last_name',
                                                            password=Config.RESPONDENT_PASSWORD,
                                                            phone_number='0987654321',
                                                            enrolment_code=enrolment_code)
    django_oauth_controller.verify_user(respondent_party['emailAddress'])
    case_id = database_controller.enrol_party(respondent_party['id'])
    case_controller.post_case_event(case_id, respondent_party['id'], "RESPONDENT_ENROLED", "Respondent enrolled")
    return respondent_party['id']


def enrol_respondent(party_id, survey_id, period):
    collection_exercise_id = collection_exercise_controller.get_collection_exercise(survey_id, period)['id']
    enrolment_code = database_controller.get_iac_for_collection_exercise(collection_exercise_id)
    party_controller.add_survey(party_id, enrolment_code)
