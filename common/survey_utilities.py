from datetime import datetime
from logging import getLogger
from random import randint

from structlog import wrap_logger

from acceptance_tests.features.steps import add_a_survey, social_survey, survey_enrolment
from common import collection_exercise_utilities, respondent_utilities
from common import common_utilities
from config import Config
from controllers import collection_exercise_controller, survey_controller

# todo more constants needed everywhere
FIELD_SEPARATOR = '-'

SURVEY_NAME_SOCIAL_PREFIX = 'SOCIAL'
SURVEY_NAME_BUSINESS_PREFIX = 'BUSINESS'

RU_REFERENCE_START = 50000000000
RU_REFERENCE_END = 59999999999

SURVEY_REFERENCE_START = 1001
SURVEY_REFERENCE_END = 9999

COLLECTION_EXERCISE_STATUS_LIVE = 'LIVE'

logger = wrap_logger(getLogger(__name__))


# todo docs everywhere

# Non-standalone methods

def setup_non_standalone_data_for_test():
    collection_exercise_utilities.execute_collection_exercises()
    collection_exercise_utilities.register_respondent(survey_id='cb8accda-6118-4d3b-85a3-149e28960c54', period='201801',
                                                      username=Config.RESPONDENT_USERNAME, ru_ref=49900000001)


# Standalone methods


def setup_standalone_data_for_test(context):
    survey_type = context.survey_type

    if is_social_survey(survey_type):
        period = create_social_survey_period()
        survey_legal_basis = 'Vol'
    else:
        period = create_business_survey_period()
        survey_legal_basis = 'STA1947'

    context.unique_id = create_ru_reference()
    survey_name = format_survey_name(context.feature_name, is_social_survey(survey_type))

    survey_response = setup_survey_for_test(context, period, survey_name, survey_type, survey_legal_basis)

    # Save values for use later
    context.survey_type = survey_type
    context.period = period
    context.survey_legal_basis = survey_legal_basis
    context.survey_id = survey_response['survey_id']
    context.survey_name = survey_response['survey_name']
    context.survey_short_name = survey_response['survey_short_name']
    context.iac = survey_response['iac']

    # Create unique username based on unique_id (RU Reference)
    context.user_name = respondent_utilities.make_respondent_user_name(str(context.unique_id),
                                                                       context.survey_short_name)

    # Call Feature method where Scenario specific setup lives
    features[context.feature_name](context)


def setup_survey_for_test(context, period, survey_name, survey_type, survey_legal_basis):
    ''' Creates a new Survey with single collection exercise based on the values supplied '''

    survey_ref = create_survey_reference()
    response = create_survey_for_test(survey_name, context.unique_id, survey_ref, survey_type, survey_legal_basis)

    survey_id = response['survey_id']

    if is_social_survey(survey_type):
        iac = create_social_collection_exercise_for_test(survey_id, period, context.unique_id,
                                                                    context.scenario_name, survey_type)
    else:
        iac = create_business_collection_exercise_for_test(survey_id, period, context.unique_id,
                                                                      context.scenario_name, survey_type)

    survey_response = {
        'survey_id': survey_id,
        'survey_name': response['survey_name'],
        'survey_short_name': response['survey_short_name'],
        'iac': iac
    }

    return survey_response


# General methods

def create_survey_for_test(survey_name, unique_id, survey_ref, survey_type, survey_legal_basis):
    logger.info('Creating survey', test_name=survey_name)

    survey_short_name = unique_id

    response = survey_controller.create_survey(survey_type=survey_type, survey_ref=survey_ref,
                                               short_name=survey_short_name,
                                               long_name=survey_name,
                                               legal_basis=survey_legal_basis)

    survey_id = response['id']

    logger.info('Survey created - ', survey_id=survey_id,
                unique_id=unique_id,
                survey_long_name=survey_name,
                survey_short_name=survey_short_name)

    response = {}
    response['survey_id'] = survey_id
    response['unique_id'] = unique_id
    response['survey_name'] = survey_name
    response['survey_short_name'] = survey_short_name

    return response


def create_social_collection_exercise_for_test(survey_id, period, ru_ref, ce_name, survey_type):
    ''' Creates a new Collection Exercise for the survey supplied '''

    logger.info('Creating Social Collection Exercise', survey_id=survey_id, period=period)

    user_description = collection_exercise_utilities.make_user_description(ce_name, is_social_survey(survey_type))
    dates = collection_exercise_utilities.generate_collection_exercise_dates_from_period(period)

    iac = collection_exercise_controller.create_and_execute_social_collection_exercise(survey_id, period,
                                                                                       user_description, dates,
                                                                                       short_name=ru_ref)

    logger.info('Social Collection Exercise created - ', survey_id=survey_id,
                ru_ref=ru_ref,
                user_description=user_description,
                period=period,
                dates=dates)

    return iac


def create_business_collection_exercise_for_test(survey_id, period, ru_ref, ce_name, survey_type):
    ''' Creates a new Collection Exercise for the survey supplied '''

    logger.info('Creating Business Collection Exercise', survey_id=survey_id, period=period)

    user_description = collection_exercise_utilities.make_user_description(ce_name, is_social_survey(survey_type))
    dates = collection_exercise_utilities.generate_collection_exercise_dates_from_period(period)

    iac = collection_exercise_controller.create_and_execute_collection_exercise_with_unique_sample(survey_id, period,
                                                                                                   user_description,
                                                                                                   dates, ru_ref)

    logger.info('Business Collection Exercise created - ', survey_id=survey_id,
                ru_ref=ru_ref,
                user_description=user_description,
                period=period,
                dates=dates)

    return iac


def create_respondent_enrolled_in_the_test_survey(context):
    # todo sort out common.*
    user_name = respondent_utilities.make_respondent_user_name(str(context.unique_id),
                                                               context.survey_short_name)
    respondent_utilities.create_respondent(user_name=user_name, enrolment_code=context.iac)['id']
    respondent_utilities.create_respondent_user_login_account(user_name)

    case = collection_exercise_utilities.find_case_by_enrolment_code(context.iac)

    context.iac = collection_exercise_utilities.generate_new_enrolment_code(case['id'], case['partyId'])


def create_respondent_not_enrolled_in_the_test_survey(context, wait_for_live_collection_exercise=False):
    create_respondent_enrolled_in_the_test_survey(context)

    #  Rollback the enrolment part of registering a respondent
    respondent_utilities.unenrol_respondent_in_survey(context.survey_id)

    if wait_for_live_collection_exercise:
        collection_exercise_controller.wait_for_collection_exercise_state(context.survey_id, context.period,
                                                                          COLLECTION_EXERCISE_STATUS_LIVE)


def is_social_survey(survey_type):
    return 'Social' == survey_type


def create_business_survey_period(from_date=datetime.utcnow()):
    return format_period(from_date.year, from_date.month)


def create_social_survey_period():
    return '1'

def format_period(period_year, period_month):
    return common_utilities.concatenate_strings(str(period_year), str(period_month).zfill(2))


def create_ru_reference():
    return str(randint(RU_REFERENCE_START, RU_REFERENCE_END))


def format_survey_name(description, is_social_survey):
    unique_id = common_utilities.create_utc_timestamp()

    if is_social_survey:
        prefix = SURVEY_NAME_SOCIAL_PREFIX
    else:
        prefix = SURVEY_NAME_BUSINESS_PREFIX

    left_part = common_utilities.concatenate_strings(prefix, description, FIELD_SEPARATOR)

    return common_utilities.concatenate_strings(left_part, unique_id, FIELD_SEPARATOR)


def create_survey_reference():
    return str(randint(SURVEY_REFERENCE_START, SURVEY_REFERENCE_END))


# Add every Feature name + data setup method handler here
features = {
    'Display enrolment code': survey_enrolment.feature_setup_survey_enrolment,
    'Generate new enrolment code': survey_enrolment.feature_setup_survey_enrolment,
    'As an respondent user': survey_enrolment.feature_setup_survey_enrolment,

    'Add a survey': add_a_survey.feature_setup_add_a_survey,

    'View social case details': social_survey.feature_setup_social_survey,
    'Search social cases by postcode': social_survey.feature_setup_social_survey
}
