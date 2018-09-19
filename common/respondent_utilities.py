from logging import getLogger

from structlog import wrap_logger

from common import collection_exercise_utilities, common_utilities
from config import Config
from controllers import party_controller, database_controller, case_controller, django_oauth_controller

logger = wrap_logger(getLogger(__name__))


def create_respondent(user_name, enrolment_code):
    logger.info('Creating a respondent', username=user_name, enrolment_code=enrolment_code)

    # party_controller.register_respondent endpoint performs many tasks including survey enrolment (which is not always
    # needed and can be rolled back using the unenrol_respondent_in_survey() method)
    respondent = party_controller.register_respondent(email_address=user_name,
                                                      first_name='first_name',
                                                      last_name='last_name',
                                                      password=Config.RESPONDENT_PASSWORD,
                                                      phone_number='0987654321',
                                                      enrolment_code=enrolment_code)
    respondent_id = respondent['id']

    party_controller.change_respondent_status(respondent_id)

    logger.info('Respondent created', respondent_id=respondent_id, username=user_name, enrolment_code=enrolment_code)

    return respondent


def unenrol_respondent_in_survey(survey_id):
    database_controller.unenrol_respondent_in_survey(survey_id)


def enrol_respondent(respondent_id, wait_for_case=False):
    logger.info('Enroling respondent', respondent_id=respondent_id, wait_for_case=wait_for_case)

    case_id = database_controller.enrol_party(respondent_id)

    case_controller.post_case_event(case_id, respondent_id, "RESPONDENT_ENROLED", "Respondent enrolled")
    if wait_for_case:
        collection_exercise_utilities.wait_for_case_to_update(respondent_id)

    logger.info('Respondent Enrolled', respondent_id=respondent_id, case_id=case_id, wait_for_case=wait_for_case)

    return respondent_id


def make_respondent_user_name(left_part, right_part):
    return common_utilities.concatenate_strings(common_utilities.concatenate_strings(left_part, '@'),
                                                common_utilities.concatenate_strings(right_part, '.com'))


def create_respondent_user_login_account(user_name):
    django_oauth_controller.verify_user(user_name)
