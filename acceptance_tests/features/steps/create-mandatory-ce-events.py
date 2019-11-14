from behave import given, when, then

from acceptance_tests import browser
from acceptance_tests.features.pages import collection_exercise_details
from common.browser_utilities import wait_for_url_matches
from config import Config


@given('the internal user enters an "{event}" event date for the survey')
def select_to_enter_mandatory_event_date(context, event):
    collection_exercise_details.go_to(context.short_name, context.period)
    collection_exercise_details.select_add_date(event)


@given('the internal user adds an "{event}" event date of "{day}" "{month}" "{year}" for the survey')
@when('the internal user adds an "{event}" event date of "{day}" "{month}" "{year}" for the survey')
def select_to_enter_mandatory_event_date(context, event, day, month, year):
    collection_exercise_details.go_to(context.short_name, context.period)
    collection_exercise_details.select_add_date(event)
    enter_date_for_ce_event(context, day, month, year)
    submit_event_date(context)


@when('the user enters a date of "{day}" "{month}" "{year}"')
def enter_date_for_ce_event(_, day, month, year):
    collection_exercise_details.add_ce_event_date(day, month, year)


@when('they submit the event date')
def submit_event_date(_):
    collection_exercise_details.confirm_ce_event_date()


@then('an error message should appear identifying invalid date entered')
def assert_error_message_for_invalid_date(_):
    assert browser.find_by_id("error-saving-message")


@then('mps date should not appear on collection exercise details page')
def check_invalid_event_date_not_persisted(context):
    collection_exercise_details.go_to(context.short_name, context.period)

    assert len(browser.find_by_name("mps-date").text) == 0


@then('they are redirected to the ce details page')
def assert_redirect_to_ce_details_page(context):
    wait_for_url_matches(f'{Config.RESPONSE_OPERATIONS_UI}/surveys/{context.short_name}/{context.period}')
    assert browser.find_by_id("tbl-ce-details")


@then('the new "{event}" date of "{day}" "{month}" "{year}" is displayed')
def assert_new_date_displayed(_, event, day, month, year):
    # tds not supporting id , so using name , resulting in needing to manipulate event string to match expected
    name = event.replace('_', '-')
    name = "first-reminder" if event == 'reminder' else name
    name = "second-reminder" if event == 'reminder2' else name
    name = "third-reminder" if event == 'reminder3'else name

    assert day in browser.find_by_name(f"{name}-date").text
    assert month[:3] in browser.find_by_name(f"{name}-date").text
    assert year in browser.find_by_name(f"{name}-date").text


@then('the add reminder "{reminder_number}" option should not be displayed')
def assert_add_specific_reminder_not_available(context, reminder_number):
    assert not browser.find_by_id(f"create-event-date-reminder{reminder_number}")


@then('the add reminder "{reminder_number}" option should be displayed')
def assert_add_specific_reminder_available(context, reminder_number):
    assert browser.find_by_id(f"create-event-date-reminder{reminder_number}")
