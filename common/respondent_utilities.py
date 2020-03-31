from logging import getLogger
from random import randint

from structlog import wrap_logger

from config import Config
from controllers import case_controller, collection_exercise_controller, database_controller, django_oauth_controller, \
    iac_controller, party_controller

import json

RU_REFERENCE_START = 50000000000
RU_REFERENCE_END = 59999999999

TELEPHONE_NUMBER_START = 0
TELEPHONE_NUMBER_END = 99999999999

logger = wrap_logger(getLogger(__name__))


def create_respondent(user_name, enrolment_code, phone_number, activate=True):
    logger.debug('Creating a respondent', username=user_name, enrolment_code=enrolment_code, phone_number=phone_number,
                 activate=activate)

    # party_controller.register_respondent endpoint performs many tasks including survey enrolment (which is not always
    # needed and can be rolled back using the unenrol_respondent_in_survey() method)
    respondent = party_controller.register_respondent(email_address=user_name,
                                                      first_name='first_name',
                                                      last_name='last_name',
                                                      password=Config.RESPONDENT_PASSWORD,
                                                      phone_number=phone_number,
                                                      enrolment_code=enrolment_code)
    respondent_id = respondent['id']
    if activate:
        party_controller.change_respondent_status(respondent_id)

    logger.debug('Respondent created', respondent_id=respondent_id, username=user_name, enrolment_code=enrolment_code,
                 activate=activate)

    return respondent


def create_respondent_data(context):
    context.respondent_email = create_respondent_email_address(context.short_name)
    context.phone_number = create_phone_number()


def unenrol_respondent_in_survey(survey_id):
    database_controller.unenrol_respondent_in_survey(survey_id)


def enrol_respondent(respondent_id):
    logger.debug('Enrolling respondent', respondent_id=respondent_id)

    case_id = database_controller.enrol_party(respondent_id)

    case_controller.post_case_event(case_id, respondent_id, "RESPONDENT_ENROLED")

    logger.debug('Respondent Enrolled', respondent_id=respondent_id, case_id=case_id)

    return respondent_id


def create_respondent_email_address(short_name):
    return make_email_address(short_name, short_name)


def create_respondent_user_login_account(user_name):
    django_oauth_controller.verify_user(user_name)


def register_respondent(survey_id, period, username, ru_ref=None, verified=True):
    logger.debug('Registering respondent', survey_id=survey_id, period=period, ru_ref=ru_ref)
    collection_exercise_id = collection_exercise_controller.get_collection_exercise(survey_id, period)['id']
    if ru_ref:
        business_party = party_controller.get_party_by_ru_ref(ru_ref)
        b_case = case_controller.get_b_case(collection_exercise_id, business_party['id'])
        if b_case['iac'] is None or not iac_controller.get_iac(b_case['iac'])['active']:
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
    logger.debug('Successfully registered respondent', survey_id=survey_id, period=period,
                 ru_ref=ru_ref, respondent_id=respondent_id)
    return respondent_id


def create_phone_number():
    return format(randint(TELEPHONE_NUMBER_START, TELEPHONE_NUMBER_END), '011d')


def create_enrolled_respondent_for_the_test_survey(context):
    create_respondent_data(context)

    respondent = create_respondent(user_name=context.respondent_email, enrolment_code=context.iac, phone_number=context.phone_number)
    context.respondent_id = respondent['id']
    create_respondent_user_login_account(context.respondent_email)


def create_unenrolled_respondent(context):
    create_respondent_data(context)
    respondent = create_respondent(user_name=context.respondent_email, enrolment_code=context.iac, phone_number=context.phone_number)
    create_respondent_user_login_account(context.respondent_email)
    context.respondent_id = respondent['id']

    unenrol_respondent_in_survey(context.survey_id)


def create_unverified_respondent(context):
    create_respondent_data(context)
    respondent = create_respondent(user_name=context.respondent_email, enrolment_code=context.iac, phone_number=context.phone_number,
                      activate=False)
    context.respondent_id = respondent['id']


def make_email_address(local_part=None, domain=None):
    if not local_part:
        local_part = create_ru_reference()

    if not domain:
        domain = local_part

    return f"{local_part}@{domain}.com"


def create_ru_reference():
    return str(randint(RU_REFERENCE_START, RU_REFERENCE_END))
