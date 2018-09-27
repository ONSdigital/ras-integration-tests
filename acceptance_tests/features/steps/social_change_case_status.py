from os import path
from urllib.parse import urlparse

from behave import given, when, then

from acceptance_tests.features.pages import social_change_case_status
from acceptance_tests.features.pages import social_search_by_postcode
from acceptance_tests.features.pages import social_view_case_details
from controllers.case_controller import get_case_by_id


@given('the SEL user has received a call and found the case details')
def sel_user_finds_case_details(context):
    social_search_by_postcode.go_to()
    social_search_by_postcode.enter_postcode(context.address["postcode"])
    social_search_by_postcode.click_search_by_postcode()
    social_search_by_postcode.click_case_link()


@when('they change the response status')
def change_response_status(context):
    social_view_case_details.click_change_status()
    new_status = social_change_case_status.click_first_new_response_status_option()
    context.new_status = new_status.text
    social_change_case_status.click_set_new_status()


@then('the new status is to be saved against that case')
@then('the new response status is to be displayed on the case details page')
def new_case_status_is_saved(context):
    assert context.new_status == social_view_case_details.get_detailed_case_status()


@given('the SEL user has selected to change the status')
def sel_user_has_navigated_to_change_status(context):
    sel_user_finds_case_details(context)
    social_view_case_details.click_change_status()


@when("the status is updated to '{new_status}'")
def sel_user_changes_status_to(context, new_status):
    social_change_case_status.click_status_option(new_status)
    social_change_case_status.click_set_new_status()


@then('any further communication from being triggered such as pre-notification/invitation/reminder is prevented')
def case_is_set_to_inactionable(context):
    # Currently no way of checking this step via the UI, so use case API for now
    case_id = _get_case_id_from_url()
    case = get_case_by_id(case_id)
    assert case['state'] == 'INACTIONABLE', case['state']


@given('the SEL user has selected a new response status')
def sel_user_selects_first_new_status(context):
    sel_user_finds_case_details(context)
    social_view_case_details.click_change_status()
    social_change_case_status.click_first_new_response_status_option()


@when('they confirm the status change')
def sel_user_confirms_status_change(context):
    new_status = social_change_case_status.click_first_new_response_status_option()
    context.new_status = new_status.text
    social_change_case_status.click_set_new_status()


def _get_case_id_from_url():
    url = social_change_case_status.get_social_case_change_status_url()
    url_path = urlparse(url).path
    return path.split(url_path)[-1]
