import time
import logging

from structlog import wrap_logger

from acceptance_tests import browser
from acceptance_tests.features.steps import common
from config import Config
from controllers import collection_exercise_controller, database_controller, sample_controller
from controllers import party_controller, django_oauth_controller, case_controller


logger = wrap_logger(logging.getLogger(__name__))


def after_all(context):
    """
    Close the browser after testing. See https://pythonhosted.org/behave/tutorial.html#environmental-controls
    """
    browser.quit()


def before_all(context):
    database_controller.execute_rm_sql('resources/database/database_reset_rm.sql')
    database_controller.reset_ras_database()
    common.signed_in_rops(context)
    execute_collection_exercises()
    enrolment_setup()
    common.signed_out_internal(context)


def execute_collection_exercises():
    test_file = 'resources/sample_files/business-survey-sample-date.csv'
    sample_controller.load_sample('bricks', '201801', test_file)
    sample_controller.load_sample('bricks', '201812', test_file)
    collection_exercise_controller.execute_collection_exercise(survey_id='cb8accda-6118-4d3b-85a3-149e28960c54',
                                                               period='201801')
    collection_exercise_controller.execute_collection_exercise(survey_id='cb8accda-6118-4d3b-85a3-149e28960c54',
                                                               period='201812')
    logger.info('Waiting for collection exercises execution process to finish...')
    time.sleep(240)


def enrolment_setup():
    valid_enrolment_code = database_controller.select_iac()
    respondent_info = party_controller.register_respondent(email_address=Config.RESPONDENT_USERNAME,
                                                           first_name='first_name',
                                                           last_name='last_name',
                                                           password=Config.RESPONDENT_PASSWORD,
                                                           phone_number='0987654321',
                                                           enrolment_code=valid_enrolment_code)
    respondent_uuid = respondent_info['id']
    django_oauth_controller.verify_user(respondent_info['emailAddress'])
    case_id = database_controller.enrol_party(respondent_uuid)
    case_controller.post_case_event(case_id, respondent_uuid, "RESPONDENT_ENROLED", "Respondent enrolled")
