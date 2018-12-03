from behave import fixture

from acceptance_tests.features.pages.inbox_internal import after_scenario_cleanup
from common import internal_utilities
from common.survey_utilities import COLLECTION_EXERCISE_STATUS_CREATED, \
                                    COLLECTION_EXERCISE_STATUS_LIVE, \
                                    create_data_for_collection_exercise, \
                                    create_data_for_survey, \
                                    create_default_data, \
                                    create_enrolled_respondent_for_the_test_survey, \
                                    create_ru_reference, \
                                    create_survey_reference, \
                                    create_test_business_collection_exercise, \
                                    create_test_survey, \
                                    create_unenrolled_respondent
from controllers import collection_exercise_controller


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
    context.add_cleanup(after_scenario_cleanup, context)


@fixture
def setup_data_with_response_user(context):
    create_default_data(context)
    create_internal_user(context)


@fixture
def setup_data_with_internal_user_and_social_collection_exercise_to_closed_status(context):
    """ Creates a collection exercise that has mandatory dates in the past """
    context.period_offset_days = -365
    setup_default_data(context)

    create_internal_user(context)


@fixture
def setup_data_with_enrolled_respondent_user_and_internal_user(context, generate_new_iac=False,
                                                               wait_ce_for_state=None):
    """ Creates default data + an enrolled Respondent in the default collection exercise """
    setup_default_data(context)

    create_enrolled_respondent_for_the_test_survey(context, generate_new_iac)

    create_internal_user(context)

    if wait_ce_for_state:
        collection_exercise_controller.wait_for_collection_exercise_state(context.survey_id, context.period,
                                                                          wait_ce_for_state)
    context.add_cleanup(after_scenario_cleanup, context)


@fixture
def setup_data_with_unenrolled_respondent_user(context, generate_new_iac=False,
                                               wait_for_collection_exercise_state=None):
    """
    Creates default data + an unenrolled Respondent
    :param context:
    :param generate_new_iac: generate a new unused iac
    :param wait_for_collection_exercise_state: wait for collection exercise state = live
    :return:
    """
    setup_default_data(context)

    create_unenrolled_respondent(context, generate_new_iac)

    if wait_for_collection_exercise_state:
        collection_exercise_controller.wait_for_collection_exercise_state(context.survey_id, context.period,
                                                                          wait_for_collection_exercise_state)
    context.add_cleanup(after_scenario_cleanup, context)


@fixture
def setup_data_with_unenrolled_respondent_user_and_internal_user(context):
    setup_data_with_unenrolled_respondent_user(context)

    create_internal_user(context)
    context.add_cleanup(after_scenario_cleanup, context)


@fixture
def setup_data_with_unenrolled_respondent_user_and_new_iac(context):
    """ Creates default data, an unenrolled Respondent and generates a new unused iac """
    setup_data_with_unenrolled_respondent_user(context, generate_new_iac=True)


@fixture
def setup_data_with_internal_user_and_collection_exercise_to_created_status(context):
    _setup_data_with_internal_user_and_collection_exercise_to_specific_status(context,
                                                                              COLLECTION_EXERCISE_STATUS_CREATED)


@fixture
def setup_data_with_internal_user_and_collection_exercise_to_live_status(context):
    _setup_data_with_internal_user_and_collection_exercise_to_specific_status(context,
                                                                              COLLECTION_EXERCISE_STATUS_LIVE)


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
    context.short_name = short_name
    context.period = period

    create_test_business_collection_exercise(survey_id, period, short_name, ce_name, survey_type,
                                             stop_at_state=stop_at_state)

    create_internal_user(context)






@fixture
def setup_data_with_unenrolled_respondent_user_and_new_iac_and_collection_exercise_to_live(context):
    """ Creates default data, an unenrolled Respondent, generates a new unused iac
    and waits until collection exercise state = live """
    setup_data_with_unenrolled_respondent_user(context, generate_new_iac=True,
                                               wait_for_collection_exercise_state=COLLECTION_EXERCISE_STATUS_LIVE)


@fixture
def setup_data_with_enrolled_respondent_user_and_internal_user_and_new_iac_and_collection_exercise_to_live(context):
    """ Creates default data, an enrolled Respondent, generates a new unused iac
    and waits until collection exercise state = live """
    setup_data_with_enrolled_respondent_user_and_internal_user(context, generate_new_iac=True,
                                                               wait_ce_for_state=COLLECTION_EXERCISE_STATUS_LIVE)
    context.add_cleanup(after_scenario_cleanup, context)


@fixture
def setup_data_with_2_enrolled_respondent_users_and_internal_user(context):
    """ Creates default survey + 2 enrolled respondents in 2 collection exercises """
    setup_data_with_enrolled_respondent_user_and_internal_user(context)

    # Save 1st collection exercise details - will probably need more depending on use?
    ce1_short_name = context.short_name

    context.period_offset_days = -31

    survey_data = create_data_for_survey(context)
    period = survey_data['period']
    short_name = survey_data['short_name']
    survey_id = context.survey_id
    ce_name = context.scenario_name
    survey_type = context.survey_type

    context.iac = create_test_business_collection_exercise(survey_id, period, short_name, ce_name, survey_type)

    context.short_name = short_name
    create_enrolled_respondent_for_the_test_survey(context)

    # Restore 1st collection exercise details
    context.short_name = ce1_short_name


def setup_default_data(context):
    """ Create the default Survey and Collection Exercise """
    create_default_data(context)


def create_internal_user(context):
    context.internal_user_name = create_ru_reference()

    internal_utilities.create_internal_user_login_account(context.internal_user_name)


def setup_survey_metadata_with_internal_user(context):
    setup_with_internal_user(context)
    setup_prepare_data_for_new_survey(context)


def setup_data_survey_with_internal_user(context):
    setup_survey_metadata_with_internal_user(context)
    survey_id = create_test_survey(context.long_name, context.short_name, context.survey_ref, context.survey_type,
                                   context.legal_basis)
    context.survey_id = survey_id
