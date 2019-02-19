from behave import given, when, then

from acceptance_tests import browser
from acceptance_tests.features.pages import collection_exercise_details
from controllers.collection_exercise_controller import create_collection_exercise, get_events_for_collection_exercise
from controllers.survey_controller import get_survey_by_short_name


@given('the internal user has created a new collection exercise for '
       '"{survey}" and period "{period}" with shown as "{shown_as}"')
def create_ce(_, survey, period, shown_as):
    survey = get_survey_by_short_name(survey)
    create_collection_exercise(survey['id'], period, shown_as)


@when('there is no mandatory event dates scheduled for the ce for "{survey}" "{period}"')
def check_no_mandatory_dates_for_ce(_, survey, period):
    survey = get_survey_by_short_name(survey)
    events = get_events_for_collection_exercise(survey['id'], period)

    assert len(events) == 0


@then('the user must be able to input the mandatory event dates into the CE "{period}" for a given "{survey}" survey')
def assert_mandatory_dates_can_be_added(_, period, survey):
    collection_exercise_details.go_to(survey, period)

    assert browser.find_by_id("create-event-date-mps"), "Cannot add mps event date"
    assert browser.find_by_id("create-event-date-go-live"), "Cannot add go live event date"
    assert browser.find_by_id("create-event-date-return-by"), \
        "Cannot add return by event date"
    assert browser.find_by_id("create-event-date-exercise-end"), \
        "Cannot add exercise end event date"


@given('the internal user has chosen to enter a mandatory ce event date for "{survey}" "{period}"')
def select_to_enter_mandatory_event_date(_, survey, period):
    collection_exercise_details.go_to(survey, period)
    collection_exercise_details.select_add_mps_date()


@when('the user enters a date of "{day}" "{month}" "{year}"')
def enter_invalid_day_for_ce_event(_, day, month, year):
    collection_exercise_details.add_ce_event_date(day, month, year)


@when('submits mandatory ce event date')
def submit_event_date(_):
    collection_exercise_details.confirm_ce_event_date()


@then('an error message should appear identifying invalid date entered')
def assert_error_message_for_invalid_date(_):
    assert browser.find_by_id("error-saving-message")


@then('invalid date of "{day}" "{month}" "{year}" should not appear on "{survey}"'
      ' "{period}" collection exercise details page')
def check_invalid_event_date_not_persisted(_, day, month, year, survey, period):
    collection_exercise_details.go_to(survey, period)

    assert day not in browser.find_by_name("mps-date").text
    assert month not in browser.find_by_name("mps-date").text
    assert year not in browser.find_by_name("mps-date").text


@then('the user is redirected to the ce details page')
def assert_redirect_to_ce_details_page(_):
    assert browser.find_by_id("tbl-ce-details")


@then('the new mandatory event date of "{day}" "{year}" is displayed')
def assert_new_date_displayed(_, day, year):
    assert day in browser.find_by_name("mps-date").text
    assert year in browser.find_by_name("mps-date").text
