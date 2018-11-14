from logging import getLogger

from structlog import wrap_logger

from common import survey_utilities
from config import Config
from controllers import party_controller, database_controller, case_controller, django_oauth_controller, \
    collection_exercise_controller, iac_controller

logger = wrap_logger(getLogger(__name__))


def create_respondent(user_name, enrolment_code, phone_number):
    logger.info('Creating a respondent', username=user_name, enrolment_code=enrolment_code, phone_number=phone_number)

    # party_controller.register_respondent endpoint performs many tasks including survey enrolment (which is not always
    # needed and can be rolled back using the unenrol_respondent_in_survey() method)
    respondent = party_controller.register_respondent(email_address=user_name,
                                                      first_name='first_name',
                                                      last_name='last_name',
                                                      password=Config.RESPONDENT_PASSWORD,
                                                      phone_number=phone_number,
                                                      enrolment_code=enrolment_code)
    respondent_id = respondent['id']

    party_controller.change_respondent_status(respondent_id)

    logger.info('Respondent created', respondent_id=respondent_id, username=user_name, enrolment_code=enrolment_code)

    return respondent


def unenrol_respondent_in_survey(survey_id):
    database_controller.unenrol_respondent_in_survey(survey_id)


def enrol_respondent(respondent_id):
    logger.info('Enroling respondent', respondent_id=respondent_id)

    case_id = database_controller.enrol_party(respondent_id)

    case_controller.post_case_event(case_id, respondent_id, "RESPONDENT_ENROLED")

    logger.info('Respondent Enrolled', respondent_id=respondent_id, case_id=case_id)

    return respondent_id


def make_respondent_user_name(short_name):
    return survey_utilities.make_email_address(short_name, short_name)


def create_respondent_user_login_account(user_name):
    django_oauth_controller.verify_user(user_name)


def register_respondent(survey_id, period, username, ru_ref=None, verified=True):
    logger.info('Registering respondent', survey_id=survey_id, period=period, ru_ref=ru_ref)
    collection_exercise_id = collection_exercise_controller.get_collection_exercise(survey_id, period)['id']
    if ru_ref:
        business_party = party_controller.get_party_by_ru_ref(ru_ref)
        b_case = case_controller.get_b_case(collection_exercise_id, business_party['id'])
        is_iac_active = iac_controller.get_iac(b_case['iac'])['active']
        if not is_iac_active:
            enrolment_code = case_controller.generate_new_enrolment_code(b_case['id'], business_party['id'])
        else:
            enrolment_code = b_case['iac']
    else:
        enrolment_code = database_controller.get_iac_for_collection_exercise(collection_exercise_id)
    respondent_party = party_controller.register_respondent(email_address=username,
                                                            first_name='first_name',
                                                            last_name='last_name',
                                                            password=Config.RESPONDENT_PASSWORD,
                                                            phone_number='0987654321',
                                                            enrolment_code=enrolment_code)

    respondent_id = respondent_party['id']
    if verified:
        party_controller.change_respondent_status(respondent_party['id'])
    logger.info('Successfully registered respondent', survey_id=survey_id, period=period,
                ru_ref=ru_ref, respondent_id=respondent_id)
    return respondent_id
