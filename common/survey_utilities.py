from datetime import datetime, timedelta
from logging import getLogger
from random import randint

from structlog import wrap_logger
from common.collection_exercise_utilities import execute_collection_exercises, \
                                                 find_case_by_enrolment_code, \
                                                 generate_collection_exercise_dates_from_period, \
                                                 generate_new_enrolment_code, \
                                                 make_user_description
from common.common_utilities import concatenate_strings, compact_string, create_utc_timestamp
from common.respondent_utilities import create_respondent, \
                                        create_respondent_user_login_account, \
                                        make_respondent_user_name, \
                                        register_respondent, \
                                        unenrol_respondent_in_survey
from config import Config
from controllers import collection_exercise_controller, survey_controller

FIELD_SEPARATOR = '-'

SURVEY_NAME_SOCIAL_PREFIX = 'SOCIAL'
SURVEY_NAME_BUSINESS_PREFIX = 'BUSINESS'

RU_REFERENCE_START = 50000000000
RU_REFERENCE_END = 59999999999

SURVEY_REFERENCE_PREFIX = '9'
SURVEY_REFERENCE_START = 1001
SURVEY_REFERENCE_END = 99999

TELEPHONE_NUMBER_START = 0
TELEPHONE_NUMBER_END = 99999999999

COLLECTION_EXERCISE_STATUS_CREATED = 'CREATED'
COLLECTION_EXERCISE_STATUS_LIVE = 'LIVE'

logger = wrap_logger(getLogger(__name__))


# Sequential methods

def setup_sequential_data_for_test():
    execute_collection_exercises()
    register_respondent(survey_id='cb8accda-6118-4d3b-85a3-149e28960c54', period='201801',
                        username=Config.RESPONDENT_USERNAME, ru_ref=49900000001)


# Parallel methods

def create_data_for_survey(context):
    """ Data used for creating a Survey """
    period_offset_days = getattr(context, 'period_offset_days', 0)

    if is_social_survey(context.survey_type):
        period = create_social_survey_period(period_offset_days)
        legal_basis = 'Vol'
    else:
        period = create_business_survey_period(period_offset_days=period_offset_days)
        legal_basis = 'STA1947'

    return {
        'period': period,
        'legal_basis': legal_basis,
        'short_name': create_ru_reference(),
        'long_name': format_survey_name(context.feature_name, is_social_survey(context.survey_type), 100)
    }


def create_data_for_collection_exercise():
    """ Data used for creating a Collection Exercise """
    return {
        'survey_ref': create_survey_reference()
    }


def create_default_data(context):
    logger.debug(
        f'Feature [{context.feature_name}], Scenario [{context.scenario_name}] creating default Survey & Exercise')

    survey_type = context.survey_type
    scenario_name = context.scenario_name

    survey_data = create_data_for_survey(context)

    period = survey_data['period']
    legal_basis = survey_data['legal_basis']
    short_name = survey_data['short_name']
    long_name = survey_data['long_name']
    survey_ref = create_data_for_collection_exercise()['survey_ref']

    survey_id = create_test_survey(long_name, short_name, survey_ref, context.survey_type, legal_basis)

    if is_social_survey(context.survey_type):
        context.iac = create_test_social_collection_exercise(context, survey_id, period, short_name, scenario_name,
                                                             survey_type)
    else:
        context.iac = create_test_business_collection_exercise(survey_id, period, short_name, scenario_name,
                                                               survey_type)

    # Save values for later
    context.period = period
    context.legal_basis = legal_basis
    context.short_name = short_name
    context.long_name = long_name
    context.survey_ref = survey_ref
    context.survey_id = survey_id
    context.respondent_user_name = make_respondent_user_name(short_name)


# General methods

def create_test_survey(long_name, short_name, survey_ref, survey_type, legal_basis):
    logger.debug('Creating survey', test_name=long_name)

    response = survey_controller.create_survey(survey_type=survey_type, survey_ref=survey_ref,
                                               short_name=short_name,
                                               long_name=long_name,
                                               legal_basis=legal_basis)

    survey_id = response['id']

    logger.debug('Survey created - ', survey_id=survey_id, long_name=long_name, short_name=short_name)

    return survey_id


def create_test_social_collection_exercise(context, survey_id, period, ru_ref, ce_name, survey_type):
    """ Creates a new Collection Exercise for the survey supplied """

    logger.debug('Creating Social Collection Exercise', survey_id=survey_id, period=period)

    user_description = make_user_description(ce_name, is_social_survey(survey_type), 50)
    dates = generate_collection_exercise_dates_from_period(period)

    iac = collection_exercise_controller.create_and_execute_social_collection_exercise(context, survey_id, period,
                                                                                       user_description, dates,
                                                                                       short_name=ru_ref)

    logger.debug('Social Collection Exercise created - ', survey_id=survey_id, ru_ref=ru_ref,
                 user_description=user_description, period=period, dates=dates)

    return iac


def create_test_business_collection_exercise(survey_id, period, ru_ref, ce_name, survey_type, stop_at_state='LIVE'):
    """ Creates a new Collection Exercise for the survey supplied """

    logger.debug('Creating Business Collection Exercise', survey_id=survey_id, period=period)

    user_description = make_user_description(ce_name, is_social_survey(survey_type), 50)
    dates = generate_collection_exercise_dates_from_period(period)

    iac = collection_exercise_controller.create_and_execute_collection_exercise_with_unique_sample(survey_id, period,
                                                                                                   user_description,
                                                                                                   dates, ru_ref,
                                                                                                   stop_at_state)

    logger.debug('Business Collection Exercise created - ', survey_id=survey_id, ru_ref=ru_ref,
                 user_description=user_description, period=period, dates=dates)

    return iac


def create_enrolled_respondent_for_the_test_survey(context, generate_new_iac=False):
    user_name = make_respondent_user_name(context.short_name)

    context.phone_number = create_phone_number()

    create_respondent(user_name=user_name, enrolment_code=context.iac, phone_number=context.phone_number)
    create_respondent_user_login_account(user_name)

    if generate_new_iac:
        case = find_case_by_enrolment_code(context.iac)
        context.iac = generate_new_enrolment_code(case['id'], case['partyId'])


def create_unenrolled_respondent(context, generate_new_iac=False):
    create_enrolled_respondent_for_the_test_survey(context, generate_new_iac)

    unenrol_respondent_in_survey(context.survey_id)


def is_social_survey(survey_type):
    return 'Social' == survey_type


def create_business_survey_period(period_offset_days=0):
    period_date = datetime.utcnow() + timedelta(days=period_offset_days)

    return format_period(period_date.year, period_date.month)


def create_social_survey_period(period_offset_days=0):
    period_date = datetime.utcnow() + timedelta(days=period_offset_days)

    return format_period(period_date.year, period_date.month)


def format_period(period_year, period_month):
    return concatenate_strings(str(period_year), str(period_month).zfill(2))


def create_ru_reference():
    return str(randint(RU_REFERENCE_START, RU_REFERENCE_END))


def make_email_address(local_part=None, domain=None):
    if not local_part:
        local_part = create_ru_reference()

    if not domain:
        domain = local_part

    return f"{local_part}@{domain}.com"


def format_survey_name(survey_name_in, social_survey, max_field_length):
    timestamp = create_utc_timestamp()

    if social_survey:
        name = f"{SURVEY_NAME_SOCIAL_PREFIX}{FIELD_SEPARATOR}{survey_name_in}{FIELD_SEPARATOR}{timestamp}"
    else:
        name = f"{SURVEY_NAME_BUSINESS_PREFIX}{FIELD_SEPARATOR}{survey_name_in}{FIELD_SEPARATOR}{timestamp}"

    return compact_string(name, max_field_length)


def create_survey_reference():
    ref = str(randint(SURVEY_REFERENCE_START, SURVEY_REFERENCE_END))
    return f"{SURVEY_REFERENCE_PREFIX}{ref}"


def create_phone_number():
    return format(randint(TELEPHONE_NUMBER_START, TELEPHONE_NUMBER_END), '011d')
