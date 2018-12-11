from behave import fixture

from acceptance_tests.features.pages import sign_out_internal
from common.collection_exercise_utilities import create_business_survey_period, create_social_survey_period, \
    execute_collection_exercises, generate_collection_exercise_dates_from_period, \
    generate_new_enrolment_code_from_existing_code, make_user_description, create_variable_collection_exercise_dates
from common.internal_user_utilities import create_internal_user_login_account
from common.respondent_utilities import create_enrolled_respondent_for_the_test_survey, create_respondent, \
    create_respondent_data, create_respondent_email_address, create_respondent_user_login_account, \
    create_ru_reference, \
    create_unenrolled_respondent, create_unverified_respondent, register_respondent
from common.survey_utilities import create_survey_reference, create_test_survey, format_survey_name, is_social_survey, \
    logger
from config import Config
from controllers import collection_exercise_controller

COLLECTION_EXERCISE_CREATED = 'CREATED'
COLLECTION_EXERCISE_SCHEDULED = 'SCHEDULED'
COLLECTION_EXERCISE_READY_FOR_REVIEW = 'READY_FOR_REVIEW'
COLLECTION_EXERCISE_READY_FOR_LIVE = 'READY_FOR_LIVE'
COLLECTION_EXERCISE_LIVE = 'LIVE'


def setup_sequential_data_for_test():
    # Data setup for before sequential test run
    execute_collection_exercises()
    register_respondent(survey_id='cb8accda-6118-4d3b-85a3-149e28960c54', period='201801',
                        username=Config.RESPONDENT_USERNAME, ru_ref=49900000001)


def setup_prepare_data_for_new_survey(context):
    survey_data = create_data_for_survey(context)

    context.long_name = survey_data['long_name']
    context.short_name = survey_data['short_name']
    context.period = survey_data['period']
    context.survey_ref = create_survey_reference()
    context.legal_basis = survey_data['legal_basis']


@fixture
def setup_with_internal_user(context):
    create_internal_user(context)
    context.add_cleanup(sign_out_internal.try_sign_out)


@fixture
def setup_data_with_internal_user(context):
    create_default_data(context)
    create_internal_user(context)


@fixture
def setup_data_with_enrolled_respondent_user(context):
    create_default_data(context)
    create_enrolled_respondent_for_the_test_survey(context)


@fixture
def setup_data_with_internal_user_and_social_collection_exercise_to_closed_status(context):
    """ Creates a collection exercise that has mandatory dates in the past """
    context.period_offset_days = -365
    setup_data_with_internal_user(context)


@fixture
def setup_data_with_enrolled_respondent_user_and_internal_user(context):
    """ Creates default data + an enrolled Respondent in the default collection exercise """
    setup_data_with_internal_user(context)
    create_enrolled_respondent_for_the_test_survey(context)

    context.add_cleanup(sign_out_internal.try_sign_out)


@fixture
def setup_data_with_unenrolled_respondent_user(context):
    """
    Creates default data + an unenrolled Respondent
    :param context:
    :return:
    """
    create_default_data(context)
    create_unenrolled_respondent(context)


@fixture
def setup_data_with_unenrolled_respondent_user_and_internal_user(context):
    setup_data_with_internal_user(context)
    create_unenrolled_respondent(context)

    context.add_cleanup(sign_out_internal.try_sign_out)


@fixture
def setup_data_with_respondent_user_data_and_new_iac(context):
    """ Creates default data, an unenrolled Respondent and generates a new unused iac """
    create_default_data(context)
    create_respondent_data(context)
    create_new_iac(context)


@fixture
def setup_data_with_internal_user_and_collection_exercise_to_created_status(context):
    _setup_data_with_internal_user_and_collection_exercise_to_specific_status(context,
                                                                              COLLECTION_EXERCISE_CREATED)


@fixture
def setup_data_with_internal_user_and_collection_exercise_to_scheduled_status(context):
    _setup_data_with_internal_user_and_collection_exercise_to_specific_status(context,
                                                                              COLLECTION_EXERCISE_SCHEDULED)
    create_variable_collection_exercise_dates(context.collection_exercise_id, context.dates)
    context.add_cleanup(sign_out_internal.try_sign_out)


@fixture
def setup_data_with_internal_user_and_collection_exercise_to_ready_for_review_status(context):
    _setup_data_with_internal_user_and_collection_exercise_to_specific_status(context,
                                                                              COLLECTION_EXERCISE_READY_FOR_REVIEW)


@fixture
def setup_data_with_internal_user_and_collection_exercise_to_ready_for_live_status(context):
    _setup_data_with_internal_user_and_collection_exercise_to_specific_status(context,
                                                                              COLLECTION_EXERCISE_READY_FOR_LIVE)
    context.add_cleanup(sign_out_internal.try_sign_out)


@fixture
def setup_data_with_internal_user_and_collection_exercise_to_live_status(context):
    _setup_data_with_internal_user_and_collection_exercise_to_specific_status(context,
                                                                              COLLECTION_EXERCISE_LIVE)
    context.add_cleanup(sign_out_internal.try_sign_out)


def _setup_data_with_internal_user_and_collection_exercise_to_specific_status(context, stop_at_state):
    """ Creates default survey + collection exercise state = created """
    survey_data = create_data_for_survey(context)
    period = survey_data['period']
    short_name = survey_data['short_name']
    legal_basis = survey_data['legal_basis']
    long_name = survey_data['long_name']

    survey_type = context.survey_type

    survey_ref = create_data_for_collection_exercise()['survey_ref']

    survey_id = create_test_survey(long_name, short_name, survey_ref, survey_type, legal_basis)

    ce_name = context.scenario_name

    context.survey_id = survey_id
    context.survey_ref = survey_ref
    context.long_name = long_name
    context.short_name = short_name
    context.period = period

    response = create_test_business_collection_exercise(survey_id, period, short_name, ce_name,
                                                        survey_type, stop_at_state=stop_at_state)

    context.collection_exercise_id = response['collection_exercise']['id']
    context.user_description = response['user_description']
    context.dates = response['dates']

    create_internal_user(context)


@fixture
def setup_data_with_unenrolled_respondent_user_and_new_iac_and_collection_exercise_to_live(context):
    """ Creates default data, an unenrolled Respondent, generates a new unused iac
    and waits until collection exercise state = live """
    create_default_data(context)
    create_unenrolled_respondent(context)
    create_new_iac(context)
    collection_exercise_controller.wait_for_collection_exercise_state(context.survey_id, context.period,
                                                                      expected_state=COLLECTION_EXERCISE_LIVE)


@fixture
def setup_data_with_enrolled_respondent_user_and_internal_user_and_new_iac_and_collection_exercise_to_live(context):
    """ Creates default data, an enrolled Respondent, generates a new unused iac
    and waits until collection exercise state = live """
    setup_data_with_internal_user(context)
    create_enrolled_respondent_for_the_test_survey(context)
    create_new_iac(context)
    collection_exercise_controller.wait_for_collection_exercise_state(context.survey_id, context.period,
                                                                      expected_state=COLLECTION_EXERCISE_LIVE)
    context.add_cleanup(sign_out_internal.try_sign_out)


@fixture
def setup_data_with_enrolled_respondent_user_and_collection_exercise_to_live(context):
    """ Creates default data, an enrolled Respondent waits until collection exercise state = live """
    create_default_data(context)
    create_enrolled_respondent_for_the_test_survey(context)
    collection_exercise_controller.wait_for_collection_exercise_state(context.survey_id, context.period,
                                                                      expected_state=COLLECTION_EXERCISE_LIVE)
    context.add_cleanup(sign_out_internal.try_sign_out)


@fixture
def setup_data_with_2_enrolled_respondent_users_and_internal_user(context):
    """ Creates default survey + 2 enrolled respondents in a collection exercise """
    setup_data_with_internal_user(context)
    create_enrolled_respondent_for_the_test_survey(context)

    # Create second enrolled respondent
    new_iac = generate_new_enrolment_code_from_existing_code(context.iac)
    second_ru_ref = create_ru_reference()
    context.used_email_address = create_respondent_email_address(second_ru_ref)
    create_respondent(context.used_email_address, new_iac, context.phone_number)
    create_respondent_user_login_account(context.used_email_address)
    

@fixture
def setup_data_with_enrolled_respondent_user_and_eq_collection_exercise_live(context):
    create_default_data(context, eq_ci=True)
    collection_exercise_controller.wait_for_collection_exercise_state(context.survey_id, context.period,
                                                                      expected_state=COLLECTION_EXERCISE_LIVE)
    create_enrolled_respondent_for_the_test_survey(context)


@fixture
def setup_data_with_unverified_respondent(context):
    create_default_data(context)
    create_unverified_respondent(context)


def create_internal_user(context):
    context.internal_user_name = create_ru_reference()

    create_internal_user_login_account(context.internal_user_name)


def create_new_iac(context):
    context.iac = generate_new_enrolment_code_from_existing_code(context.iac)


def setup_survey_metadata_with_internal_user(context):
    setup_with_internal_user(context)
    setup_prepare_data_for_new_survey(context)


def setup_data_survey_with_internal_user(context):
    setup_survey_metadata_with_internal_user(context)
    survey_id = create_test_survey(context.long_name, context.short_name, context.survey_ref, context.survey_type,
                                   context.legal_basis)
    context.survey_id = survey_id


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


def create_default_data(context, eq_ci=False):
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
        response = create_test_business_collection_exercise(survey_id, period, short_name, scenario_name,
                                                            survey_type, eq_ci=eq_ci)
        context.iac = response['iac']

    # Save values for later
    context.period = period
    context.legal_basis = legal_basis
    context.short_name = short_name
    context.long_name = long_name
    context.survey_ref = survey_ref
    context.survey_id = survey_id
    context.respondent_email = create_respondent_email_address(short_name)


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


def create_test_business_collection_exercise(survey_id, period, ru_ref, ce_name, survey_type, stop_at_state='LIVE',
                                             eq_ci=False):
    """ Creates a new Collection Exercise for the survey supplied """

    logger.debug('Creating Business Collection Exercise', survey_id=survey_id, period=period)

    user_desc = make_user_description(ce_name, is_social_survey(survey_type), 50)
    dates = generate_collection_exercise_dates_from_period(period)

    response = collection_exercise_controller.create_and_execute_collection_exercise_with_unique_sample(survey_id,
                                                                                                        period,
                                                                                                        user_desc,
                                                                                                        dates, ru_ref,
                                                                                                        stop_at_state,
                                                                                                        eq_ci=eq_ci)

    logger.debug('Business Collection Exercise created - ', survey_id=survey_id, ru_ref=ru_ref,
                 user_desc=user_desc, period=period, dates=dates)

    return {'collection_exercise': response['collection_exercise'],
            'iac': response['iac'],
            'user_description': user_desc,
            'dates': dates}
