from behave import fixture

from common.survey_utilities import create_default_data, create_enrolled_respondent_for_the_test_survey, \
    COLLECTION_EXERCISE_STATUS_LIVE, create_unenrolled_respondent, create_data_for_survey, create_test_survey, \
    create_data_for_collection_exercise, \
    create_test_business_collection_exercise, COLLECTION_EXERCISE_STATUS_CREATED
from controllers import collection_exercise_controller


@fixture
def setup_default_data(context):
    """ Create the default Survey and Collection Exercise """

    create_default_data(context)


@fixture
def setup_enrolled_respondent(context, generate_new_iac=False):
    """ Creates default data + an enrolled Respondent in the default colelction exercise """
    setup_default_data(context)

    create_enrolled_respondent_for_the_test_survey(context, generate_new_iac)


@fixture
def setup_unenrolled_respondent(context, generate_new_iac=False, wait_for_collection_exercise_state=None):
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


@fixture
def setup_unenrolled_respondent_generate_new_iac(context):
    """ Creates default data, an unenrolled Respondent and generates a new unused iac """

    setup_default_data(context)

    create_enrolled_respondent_for_the_test_survey(context)


@fixture
def setup_collection_exercise_to_created_status(context):
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
                                             stop_at_state=COLLECTION_EXERCISE_STATUS_CREATED)


@fixture
def setup_unenrolled_respondent_generate_new_iac_collection_exercise_to_live_status(context):
    """ Creates default data, an unenrolled Respondent, generates a new unused iac
    and waits until collection exercise state = live """

    setup_unenrolled_respondent(context, generate_new_iac=True,
                                wait_for_collection_exercise_state=COLLECTION_EXERCISE_STATUS_LIVE)
