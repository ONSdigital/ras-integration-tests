from datetime import datetime, timedelta
from logging import getLogger
from random import randint

from structlog import wrap_logger

import common.collection_exercise_utilities
import common.respondent_utilities
from common import common_utilities
from common import respondent_utilities
from config import Config
from controllers import collection_exercise_controller, survey_controller

FIELD_SEPARATOR = '-'

SURVEY_NAME_SOCIAL_PREFIX = 'SOCIAL'
SURVEY_NAME_BUSINESS_PREFIX = 'BUSINESS'

RU_REFERENCE_START = 50000000000
RU_REFERENCE_END = 59999999999

SURVEY_REFERENCE_PREFIX = '9'
SURVEY_REFERENCE_START = 1001
SURVEY_REFERENCE_END = 999999

COLLECTION_EXERCISE_STATUS_CREATED = 'CREATED'
COLLECTION_EXERCISE_STATUS_LIVE = 'LIVE'

logger = wrap_logger(getLogger(__name__))


# Non-standalone methods

def setup_sequential_data_for_test():
    common.collection_exercise_utilities.execute_collection_exercises()
    common.respondent_utilities.register_respondent(survey_id='cb8accda-6118-4d3b-85a3-149e28960c54', period='201801',
                                                    username=Config.RESPONDENT_USERNAME, ru_ref=49900000001)


# Standalone methods

def create_data_for_survey(context):
    """ Data used for creating a Survey """
    period_offset_days = getattr(context, 'period_offset_days', 0)

    if is_social_survey(context.survey_type):
        period = create_social_survey_period(period_offset_days)
        legal_basis = 'Vol'
    else:
        period = create_business_survey_period()
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
    context.user_name = respondent_utilities.make_respondent_user_name(str(short_name), short_name)


# General methods

def create_test_survey(long_name, short_name, survey_ref, survey_type, legal_basis):
    logger.info('Creating survey', test_name=long_name)

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

    user_description = common.collection_exercise_utilities.make_user_description(ce_name,
                                                                                  is_social_survey(survey_type), 50)
    dates = common.collection_exercise_utilities.generate_collection_exercise_dates_from_period(period)

    iac = collection_exercise_controller.create_and_execute_social_collection_exercise(context, survey_id, period,
                                                                                       user_description, dates,
                                                                                       short_name=ru_ref)

    logger.debug('Social Collection Exercise created - ', survey_id=survey_id, ru_ref=ru_ref,
                 user_description=user_description, period=period, dates=dates)

    return iac


def create_test_business_collection_exercise(survey_id, period, ru_ref, ce_name, survey_type, stop_at_state='LIVE'):
    """ Creates a new Collection Exercise for the survey supplied """

    logger.debug('Creating Business Collection Exercise', survey_id=survey_id, period=period)

    user_description = common.collection_exercise_utilities.make_user_description(ce_name,
                                                                                  is_social_survey(survey_type), 50)
    dates = common.collection_exercise_utilities.generate_collection_exercise_dates_from_period(period)

    iac = collection_exercise_controller.create_and_execute_collection_exercise_with_unique_sample(survey_id, period,
                                                                                                   user_description,
                                                                                                   dates, ru_ref,
                                                                                                   stop_at_state)

    logger.debug('Business Collection Exercise created - ', survey_id=survey_id, ru_ref=ru_ref,
                 user_description=user_description, period=period, dates=dates)

    return iac


def create_enrolled_respondent_for_the_test_survey(context, generate_new_iac=False):
    user_name = respondent_utilities.make_respondent_user_name(str(context.short_name),
                                                               context.short_name)
    respondent_utilities.create_respondent(user_name=user_name, enrolment_code=context.iac)['id']
    respondent_utilities.create_respondent_user_login_account(user_name)

    if generate_new_iac:
        case = common.collection_exercise_utilities.find_case_by_enrolment_code(context.iac)
        context.iac = common.collection_exercise_utilities.generate_new_enrolment_code(case['id'], case['partyId'])


def create_unenrolled_respondent(context, generate_new_iac=False):
    create_enrolled_respondent_for_the_test_survey(context, generate_new_iac)

    respondent_utilities.unenrol_respondent_in_survey(context.survey_id)


def is_social_survey(survey_type):
    return 'Social' == survey_type


def create_business_survey_period(from_date=datetime.utcnow()):
    return format_period(from_date.year, from_date.month)


def create_social_survey_period(period_offset_days=0):
    period_date = datetime.utcnow() + timedelta(days=period_offset_days)

    return format_period(period_date.year, period_date.month)


def format_period(period_year, period_month):
    return common_utilities.concatenate_strings(str(period_year), str(period_month).zfill(2))


def create_ru_reference():
    return str(randint(RU_REFERENCE_START, RU_REFERENCE_END))


def format_survey_name(survey_name_in, social_survey, max_field_length):
    if social_survey:
        prefix = common_utilities.concatenate_strings(SURVEY_NAME_SOCIAL_PREFIX, '', FIELD_SEPARATOR)
    else:
        prefix = common_utilities.concatenate_strings(SURVEY_NAME_BUSINESS_PREFIX, '', FIELD_SEPARATOR)

    # Append timestamp
    survey_name_out = common_utilities.concatenate_strings(survey_name_in, common_utilities.create_utc_timestamp(),
                                                           FIELD_SEPARATOR)

    survey_name_out = common_utilities.compact_string(survey_name_out, max_field_length - len(prefix))

    # return with prefix
    return common_utilities.concatenate_strings(prefix, survey_name_out)


def create_survey_reference():
    ref = str(randint(SURVEY_REFERENCE_START, SURVEY_REFERENCE_END))

    return common_utilities.concatenate_strings(SURVEY_REFERENCE_PREFIX, ref)
