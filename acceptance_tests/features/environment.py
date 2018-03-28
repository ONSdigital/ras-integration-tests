from logging import getLogger
import time

from selenium.common.exceptions import WebDriverException
from structlog import wrap_logger

from acceptance_tests import browser
from acceptance_tests.features.pages import collection_exercise_details, sign_out_internal
from acceptance_tests.features.steps import authentication
from config import Config
from controllers import (case_controller, collection_exercise_controller, collection_instrument_controller,
                         database_controller, django_oauth_controller, party_controller, sample_controller)

logger = wrap_logger(getLogger(__name__))


def before_all(context):
    logger.info('Resetting databases')
    database_controller.execute_sql('resources/database/database_reset_rm.sql')
    database_controller.execute_sql('resources/database/database_reset_party.sql')
    database_controller.execute_sql('resources/database/database_reset_oauth.sql')
    database_controller.execute_sql_secure_message('resources/database/database_reset_secure_message.sql')
    logger.info('Successfully reset databases')

    try:
        authentication.signed_in_internal(context)
        execute_collection_exercises()
        register_respondent(survey_id='cb8accda-6118-4d3b-85a3-149e28960c54', period='201801',
                            username=Config.RESPONDENT_USERNAME, ru_ref=49900000001)
        sign_out_internal.sign_out()
    except WebDriverException:
        logger.exception('Failed to setup before running tests', html=browser.html)


def before_scenario(_, scenario):
    if "skip" in scenario.effective_tags:
        scenario.skip("Marked with @skip")
        return


def after_step(context, step):
    if step.status == "failed":
        logger.exception('Failed step', scenario=context.scenario.name, step=step.name, html=browser.html)


def after_all(context):
    browser.quit()


def execute_collection_exercises():
    logger.info('Executing collection exercises')
    # Bricks
    execute_seft_collection_exercise('cb8accda-6118-4d3b-85a3-149e28960c54', '201801')
    execute_seft_collection_exercise('cb8accda-6118-4d3b-85a3-149e28960c54', '201812')
    # QBS
    execute_eq_collection_exercise('QBS', '1809')

    logger.info('Waiting for collection exercises to finish executing')
    poll_database_for_iac(survey_id='cb8accda-6118-4d3b-85a3-149e28960c54', period='201801')
    poll_database_for_iac(survey_id='cb8accda-6118-4d3b-85a3-149e28960c54', period='201812')
    poll_database_for_iac(survey_id='02b9c366-7397-42f7-942a-76dc5876d86d', period='1809')
    logger.info('Collection exercises have finished executing')


def execute_seft_collection_exercise(survey_id, period):
    logger.debug('Executing SEFT collection exercise', survey_id=survey_id, period=period)
    collection_exercise = collection_exercise_controller.get_collection_exercise(survey_id, period)
    collection_instrument_controller.upload_seft_collection_instrument(collection_exercise['id'],
                                                                       'resources/collection_instrument_files/064_201803_0001.xlsx',
                                                                       form_type='0001')
    sample_summary = sample_controller.upload_sample(collection_exercise['id'],
                                                     'resources/sample_files/business-survey-sample-date.csv')
    collection_exercise_controller.link_sample_summary_to_collection_exercise(collection_exercise['id'],
                                                                              sample_summary['id'])
    time.sleep(5)
    collection_exercise_controller.execute_collection_exercise(survey_id, period)
    logger.debug('Successfully executed SEFT collection exercise', survey_id=survey_id, period=period)


def execute_eq_collection_exercise(survey_name, period):
    logger.debug('Executing eQ collection exercise', survey=survey_name, period=period)
    collection_exercise_details.go_to(survey_name, period)
    collection_exercise_details.add_eq_ci()
    collection_exercise_details.load_sample('resources/sample_files/business-survey-sample-date.csv')
    collection_exercise_details.click_ready_for_live_and_confirm()
    logger.debug('Successfully executed eQ collection exercise', survey=survey_name, period=period)


def poll_database_for_iac(survey_id, period):
    logger.debug('Waiting for collection exercise execution process to finish',
                 survey_id=survey_id, period=period)
    collection_exercise_id = collection_exercise_controller.get_collection_exercise(survey_id, period)['id']
    while True:
        if database_controller.get_iac_for_collection_exercise(collection_exercise_id):
            logger.debug('Collection exercise finished executing', survey_id=survey_id, period=period)
            break
        time.sleep(5)


def register_respondent(survey_id, period, username, ru_ref=None):
    collection_exercise_id = collection_exercise_controller.get_collection_exercise(survey_id, period)['id']
    if ru_ref:
        business_party = party_controller.get_party_by_ru_ref(ru_ref)
        enrolment_code = database_controller.get_iac_for_collection_exercise_and_business(collection_exercise_id,
                                                                                          business_party['id'])
    else:
        enrolment_code = database_controller.get_iac_for_collection_exercise(collection_exercise_id)
    respondent_party = party_controller.register_respondent(email_address=username,
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
