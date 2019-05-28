from behave import when, given, then

from acceptance_tests.features.pages import change_response_status, surveys_history, reporting_unit
from acceptance_tests.features.steps.authentication import signed_in_respondent
from controllers.collection_exercise_controller import map_ce_status


@given('the internal user is on the reporting unit page')
def go_to_reporting_unit_page(context):
    reporting_unit.go_to(context.short_name)


@given('the collection exercise is in the "{status}" status')
@then('the collection exercise is in the "{status}" status')
def assert_collection_exercise_status(context, status):
    reporting_unit.go_to(context.short_name)
    reporting_unit.click_data_panel(context.short_name)
    collection_exericse = reporting_unit.get_collection_exercise(context.period, context.short_name)
    assert status in collection_exericse['status'], collection_exericse['status']


@given('the respondent has had their response status changed to Completed by phone')
def change_response_status_to_completed_by_phone(context):
    reporting_unit.go_to(context.short_name)
    reporting_unit.click_data_panel(context.short_name)
    internal_user_changes_response_status(context, "Completed by phone")


@when('the internal user changes the response status to "{status}"')
def internal_user_changes_response_status(context, status):
    reporting_unit.click_change_response_status_link(survey=context.short_name, period=context.period)
    mapped_status = map_ce_status(status)
    change_response_status.update_response_status(mapped_status)


@when('the respondent goes to the history page')
def respondent_goes_to_history_page(context):
    signed_in_respondent(context)
    surveys_history.go_to_history_tab()


@then('the respondent is presented the status as "{status}"')
def respondent_view_ce_status(context, status):
    case = surveys_history.get_case(context.short_name)
    assert status == case.get('status'), case.get('status')
