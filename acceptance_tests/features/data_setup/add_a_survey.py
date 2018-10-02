import traceback

from common import survey_utilities


def scenario_setup_select_to_add_new_survey(context):
    survey_utilities.create_respondent_not_enrolled_in_the_test_survey(context)


def scenario_setup_enter_the_enrolment_code(context):
    survey_utilities.create_respondent_not_enrolled_in_the_test_survey(context)


def scenario_setup_view_survey_and_organisation_that_they_are_enrolling_for(context):
    survey_utilities.create_respondent_not_enrolled_in_the_test_survey(context)


def scenario_setup_invalid_entry_of_an_enrolment_code(context):
    survey_utilities.create_respondent_not_enrolled_in_the_test_survey(context)


def scenario_setup_view_new_survey_in_my_surveys(context):
    survey_utilities.create_respondent_not_enrolled_in_the_test_survey(context, wait_for_live_collection_exercise=True)


def scenario_setup_user_can_cancel_at_any_point_for(context):
    survey_utilities.create_respondent_not_enrolled_in_the_test_survey(context)


def scenario_setup_add_a_survey(context):
    # Scenario specific setup

    try:
        scenarios[context.scenario_name](context)
    except KeyError:
        traceback.print_exc()
        exit(1)


# Add every Scenario name + data setup method handler here
scenarios = {
    'Select to add new survey': scenario_setup_select_to_add_new_survey,
    'Enter the enrolment code': scenario_setup_enter_the_enrolment_code,
    'View survey & organisation that they are enrolling for': scenario_setup_view_survey_and_organisation_that_they_are_enrolling_for,
    'Invalid entry of an enrolment code': scenario_setup_invalid_entry_of_an_enrolment_code,
    'View new survey in my surveys': scenario_setup_view_new_survey_in_my_surveys,
    'User can cancel at any point': scenario_setup_user_can_cancel_at_any_point_for
}
