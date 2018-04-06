from logging import getLogger
import time

from structlog import wrap_logger

from acceptance_tests import browser
from config import Config
from controllers import case_controller, collection_exercise_controller, database_controller, \
    django_oauth_controller, party_controller, sample_controller
from controllers.collection_instrument_controller import get_collection_instruments_by_classifier, \
    link_collection_instrument_to_exercise, upload_seft_collection_instrument

logger = wrap_logger(getLogger(__name__))


def before_all(_):
    logger.info('Resetting databases')
    database_controller.execute_sql('resources/database/database_reset_rm.sql')
    database_controller.execute_sql('resources/database/database_reset_party.sql',
                                    database_uri=Config.PARTY_DATABASE_URI)
    database_controller.execute_sql('resources/database/database_reset_oauth.sql',
                                    database_uri=Config.DJANGO_OAUTH_DATABASE_URI)
    database_controller.execute_sql('resources/database/database_reset_secure_message.sql',
                                    database_uri=Config.SECURE_MESSAGE_DATABASE_URI)
    logger.info('Successfully reset databases')

    execute_collection_exercises()
    register_respondent(survey_id='cb8accda-6118-4d3b-85a3-149e28960c54', period='201801',
                        username=Config.RESPONDENT_USERNAME, ru_ref=49900000001)


def before_scenario(_, scenario):
    if "skip" in scenario.effective_tags:
        scenario.skip("Marked with @skip")
        return


def after_step(context, step):
    if step.status == "failed":
        logger.exception('Failed step', scenario=context.scenario.name, step=step.name, html=browser.html)


def after_all(_):
    browser.quit()


def execute_collection_exercises():
    logger.info('Executing collection exercises')
    # Bricks
    execute_collection_exercise('cb8accda-6118-4d3b-85a3-149e28960c54', '201801')
    execute_collection_exercise('cb8accda-6118-4d3b-85a3-149e28960c54', '201812')
    # QBS
    execute_collection_exercise('02b9c366-7397-42f7-942a-76dc5876d86d', '1809', ci_type='eQ')

    logger.info('Waiting for collection exercises to finish executing')
    poll_database_for_iac(survey_id='cb8accda-6118-4d3b-85a3-149e28960c54', period='201801')
    poll_database_for_iac(survey_id='cb8accda-6118-4d3b-85a3-149e28960c54', period='201812')
    poll_database_for_iac(survey_id='02b9c366-7397-42f7-942a-76dc5876d86d', period='1809')
    logger.info('Collection exercises have finished executing')


def execute_collection_exercise(survey_id, period, ci_type='SEFT'):
    logger.info('Executing collection exercise', survey_id=survey_id, period=period, ci_type=ci_type)
    collection_exercise = collection_exercise_controller.get_collection_exercise(survey_id, period)

    if ci_type == 'eQ':
        collection_instruments = get_collection_instruments_by_classifier(survey_id, form_type='0001')
        for collection_instrument in collection_instruments:
            link_collection_instrument_to_exercise(collection_instrument['id'], collection_exercise['id'])
    else:
        upload_seft_collection_instrument(collection_exercise['id'],
                                          'resources/collection_instrument_files/064_201803_0001.xlsx',
                                          form_type='0001')

    sample_summary = sample_controller.upload_sample(collection_exercise['id'],
                                                     'resources/sample_files/business-survey-sample-date.csv')
    collection_exercise_controller.link_sample_summary_to_collection_exercise(collection_exercise['id'],
                                                                              sample_summary['id'])
    time.sleep(5)
    collection_exercise_controller.execute_collection_exercise(survey_id, period)
    logger.info('Successfully executed collection exercise', survey_id=survey_id, period=period, ci_type=ci_type)


def poll_database_for_iac(survey_id, period):
    logger.info('Waiting for collection exercise execution process to finish',
                survey_id=survey_id, period=period)
    collection_exercise_id = collection_exercise_controller.get_collection_exercise(survey_id, period)['id']
    while True:
        if database_controller.get_iac_for_collection_exercise(collection_exercise_id):
            logger.info('Collection exercise finished executing', survey_id=survey_id, period=period)
            break
        time.sleep(5)


def register_respondent(survey_id, period, username, ru_ref=None):
    logger.info('Registering respondent', survey_id=survey_id, period=period, username=username, ru_ref=ru_ref)
    collection_exercise_id = collection_exercise_controller.get_collection_exercise(survey_id, period)['id']
    if ru_ref:
        business_party = party_controller.get_party_by_ru_ref(ru_ref)
        enrolment_code = database_controller.get_iac_for_collection_exercise_and_business(collection_exercise_id,
                                                                                          business_party['id'])
        if not enrolment_code:
            enrolment_code = case_controller.generate_new_enrolment_code(collection_exercise_id, ru_ref).get('iac')
    else:
        enrolment_code = database_controller.get_iac_for_collection_exercise(collection_exercise_id)
    respondent_party = party_controller.register_respondent(email_address=username,
                                                            first_name='first_name',
                                                            last_name='last_name',
                                                            password=Config.RESPONDENT_PASSWORD,
                                                            phone_number='0987654321',
                                                            enrolment_code=enrolment_code)

    respondent_id = respondent_party['id']
    party_controller.change_respondent_status(respondent_party['id'])
    django_oauth_controller.verify_user(respondent_party['emailAddress'])
    case_id = database_controller.enrol_party(respondent_id)
    case_controller.post_case_event(case_id, respondent_id, "RESPONDENT_ENROLED", "Respondent enrolled")
    logger.info('Successfully registered respondent', survey_id=survey_id, period=period, username=username,
                ru_ref=ru_ref, respondent_id=respondent_id)
    return respondent_id


def enrol_respondent(party_id, survey_id, period):
    collection_exercise_id = collection_exercise_controller.get_collection_exercise(survey_id, period)['id']
    enrolment_code = database_controller.get_iac_for_collection_exercise(collection_exercise_id)
    party_controller.add_survey(party_id, enrolment_code)
