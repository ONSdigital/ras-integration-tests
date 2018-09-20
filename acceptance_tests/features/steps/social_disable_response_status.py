from behave import given, when, then

from acceptance_tests.features.pages import social_change_case_status
from acceptance_tests.features.pages import social_enter_uac
from acceptance_tests.features.pages import social_search_by_postcode
from acceptance_tests.features.pages import social_view_case_details
from acceptance_tests.features.steps import authentication


@given("the SEL user has entered a status of '{status}'")
def sel_user_changes_case_details(context, status):
    respondent_enters_uac(context)  # Case must be INPROGRESS

    authentication.signed_in_internal(context)
    social_search_by_postcode.go_to()
    social_search_by_postcode.enter_postcode(context.address["postcode"])
    social_search_by_postcode.click_search_by_postcode()
    social_search_by_postcode.click_case_link()

    social_view_case_details.click_change_status()

    social_change_case_status.click_status_option(status)
    social_change_case_status.click_set_new_status()


@when('the respondent enters a UAC')
def respondent_enters_uac(context):
    social_enter_uac.go_to()
    social_enter_uac.enter_uac(context.iac)
    social_enter_uac.click_start_button()


@then('they are informed that they are unable to launch the survey')
def respondent_unable_to_launch_survey(context):
    uac_error_text = social_enter_uac.get_uac_error_text()
    assert 'The unique access code entered has already been used' in uac_error_text, uac_error_text
