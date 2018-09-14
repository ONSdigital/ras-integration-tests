from behave import given, when, then

from acceptance_tests.features.pages import social_search_by_postcode
from acceptance_tests.features.pages.social_change_case_status import click_first_new_response_status_option, \
    click_set_new_status
from acceptance_tests.features.pages.social_view_case_details import click_change_status, get_detailed_case_status


@given('the SEL user has received a call and found the case details')
def sel_user_finds_case_details(context):
    social_search_by_postcode.go_to()
    social_search_by_postcode.enter_postcode(context.address["postcode"])
    social_search_by_postcode.click_search_by_postcode()
    social_search_by_postcode.click_case_link()


@when('they change the response status')
def change_response_status(context):
    click_change_status()
    new_status = click_first_new_response_status_option()
    context.new_status = new_status.text
    click_set_new_status()


@then('the new status is to be saved against that case')
def new_case_status_is_saved(context):
    assert context.new_status == get_detailed_case_status()


@given('the SEL user has selected to change the status')
def sel_user_has_navigated_to_change_status(context):
    raise NotImplementedError


@when("the status is updated to '{new_status}'")
def sel_user_changes_status_to(context, new_status):
    raise NotImplementedError


@then('any further communication from being triggered such as pre-notification/invitation/reminder is prevented')
def case_is_set_to_inactionable(context):
    raise NotImplementedError


@given('the SEL user has selected a new response status')
def sel_user_selects_first_new_status(context):
    raise NotImplementedError


@when('they confirm the status change')
def sel_user_confirms_status_change(context):
    raise NotImplementedError


@then('the new response status is to be displayed on the case details page')
def new_status_is_displayed_on_case_details(context):
    raise NotImplementedError
