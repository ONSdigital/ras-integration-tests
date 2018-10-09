import traceback
from datetime import datetime
from logging import getLogger
from random import randint

from structlog import wrap_logger

from acceptance_tests.features import environment
from acceptance_tests.features.data_setup import display_unused_enrolment_code, generate_new_enrolment_code, \
    survey_enrolment, add_a_survey, social_change_case_status, social_disable_uac, social_find_case_by_postcode, \
    social_view_case_details, internal_user_signs_out, internal_user_signs_in
from common import common_utilities
from common import respondent_utilities
from config import Config
from controllers import collection_exercise_controller, survey_controller

# todo more constants
FIELD_SEPARATOR = '-'

SURVEY_NAME_SOCIAL_PREFIX = 'SOCIAL'
SURVEY_NAME_BUSINESS_PREFIX = 'BUSINESS'

RU_REFERENCE_START = 50000000000
RU_REFERENCE_END = 59999999999

SURVEY_REFERENCE_PREFIX = '9'
SURVEY_REFERENCE_START = 1001
SURVEY_REFERENCE_END = 9999

COLLECTION_EXERCISE_STATUS_LIVE = 'LIVE'

logger = wrap_logger(getLogger(__name__))


# todo docs everywhere


# Non-standalone methods

def setup_non_standalone_data_for_test():
    environment.execute_collection_exercises()
    environment.register_respondent(survey_id='cb8accda-6118-4d3b-85a3-149e28960c54', period='201801',
                                                      username=Config.RESPONDENT_USERNAME, ru_ref=49900000001)


# Standalone methods


def setup_standalone_data_for_test(context):
    # todo handles business/social with many defaults - this will probably change big time as more tests are converted

    logger.info(
        f'Feature [{context.feature_name}], Scenario [{context.scenario_name}] requires default Survey & Collection Exercise created')

    survey_type = context.survey_type

    if is_social_survey(survey_type):
        period = create_social_survey_period()
        survey_legal_basis = 'Vol'
    else:
        period = create_business_survey_period()
        survey_legal_basis = 'STA1947'

    context.unique_id = create_ru_reference()
    survey_name = format_survey_name(context.feature_name, is_social_survey(survey_type), 100)

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
    #todo fixtures are cleaner but initial investigation did not work as expected, needs further investigaton
    try:
        features[context.feature_name](context)
    except KeyError:
        traceback.print_exc()
        exit(1)


def setup_survey_for_test(context, period, survey_name, survey_type, survey_legal_basis):
    ''' Creates a new Survey with single collection exercise based on the values supplied '''

    survey_ref = create_survey_reference()
    response = create_survey_for_test(survey_name, context.unique_id, survey_ref, survey_type, survey_legal_basis)

    survey_id = response['survey_id']

    if is_social_survey(survey_type):
        iac = create_social_collection_exercise_for_test(context, survey_id, period, context.unique_id,
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

    response = {
        'survey_id': survey_id,
        'unique_id': unique_id,
        'survey_name': survey_name,
        'survey_short_name': survey_short_name
    }

    return response


def create_social_collection_exercise_for_test(context, survey_id, period, ru_ref, ce_name, survey_type):
    ''' Creates a new Collection Exercise for the survey supplied '''

    logger.info('Creating Social Collection Exercise', survey_id=survey_id, period=period)

    user_description = environment.make_user_description(ce_name, is_social_survey(survey_type), 50)
    dates = environment.generate_social_collection_exercise_dates()

    iac = collection_exercise_controller.create_and_execute_social_collection_exercise(context, survey_id, period,
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

    user_description = environment.make_user_description(ce_name, is_social_survey(survey_type), 50)
    dates = environment.generate_collection_exercise_dates_from_period(period)

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

    case = environment.find_case_by_enrolment_code(context.iac)

    context.iac = environment.generate_new_enrolment_code(case['id'], case['partyId'])


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


# todo features with no scenario setup could be stopped here using setup_utilities.scenario_setup_not_defined ?
# Add every Feature name + data setup method handler here
features = {
    'Display enrolment code': display_unused_enrolment_code.scenario_setup_display_unused_enrolment_code,
    'Generate new enrolment code': generate_new_enrolment_code.scenario_setup_generate_new_enrolment_code,
    'As an respondent user': survey_enrolment.scenario_setup_survey_enrolment,

    'Add a survey': add_a_survey.scenario_setup_add_a_survey,

    'View social case details': social_view_case_details.scenario_setup_social_view_case_details,
    'Search social cases by postcode': social_find_case_by_postcode.scenario_setup_social_find_case_by_postcode,
    'Change Response Status': social_change_case_status.scenario_setup_social_change_case_status,
    'Change Response Status to \'Partial interview achieved but respondent requested data be deleted\'': social_disable_uac.scenario_setup_social_disable_uac,

    'Internal user signs in': internal_user_signs_in.scenario_setup_internal_user_signs_in,

    'Internal user signs out': internal_user_signs_out.scenario_setup_internal_user_signs_out
}
