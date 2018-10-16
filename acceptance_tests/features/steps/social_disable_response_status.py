from behave import given, when, then

from acceptance_tests.features.pages import social_change_case_status
from acceptance_tests.features.pages import social_search_by_postcode
from acceptance_tests.features.pages import social_view_case_details
from acceptance_tests.features.steps import authentication
from controllers.case_controller import post_case_event
from controllers.iac_controller import get_iac


@given("the SEL user has entered a status of '{status}'")
def sel_user_changes_case_details(context, status):
    transition_case_to_in_progress(context)  # Case must be INPROGRESS

    authentication.signed_in_internal_social(context)
    social_search_by_postcode.go_to()
    social_search_by_postcode.enter_postcode(context.address["postcode"])
    social_search_by_postcode.click_search_by_postcode()
    social_search_by_postcode.click_case_link()

    social_view_case_details.click_change_status()

    social_change_case_status.click_status_option(status)
    social_change_case_status.click_set_new_status()


@when('the respondent enters a UAC')
def transition_case_to_in_progress(context):
    # Send an EQ_LAUNCH event to transition the case to IN_PROGRESS
    post_case_event(context.case['id'], 'EQ_LAUNCH', 'Launching EQ')


@then('they are informed that they are unable to launch the survey')
def uac_is_disabled(context):
    is_iac_active = get_iac(context.iac)['active']
    assert not is_iac_active
