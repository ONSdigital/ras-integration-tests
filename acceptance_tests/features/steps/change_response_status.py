from datetime import datetime, timedelta

from behave import when, given, then

from acceptance_tests.features.environment import enrol_respondent
from acceptance_tests.features.pages import change_response_status, surveys_history, reporting_unit
from acceptance_tests.features.steps.authentication import signed_in_respondent
from controllers.collection_exercise_controller import create_and_execute_collection_exercise, \
    get_collection_exercise, map_ce_status
from config import Config
from controllers import party_controller


@given('the internal user is on the reporting unit page for ru ref "{ru_ref}"')
def go_to_reporting_unit_page(_, ru_ref):
    reporting_unit.go_to(ru_ref)


@given('the "{survey}" "{period}" collection exercise has been executed')
def create_collection_exercise(_, survey, period):
    if get_collection_exercise('cb8accda-6118-4d3b-85a3-149e28960c54', period):
        return
    now = datetime.utcnow()
    dates = {
        "mps": now + timedelta(seconds=5),
        "go_live": now + timedelta(minutes=1),
        "return_by": now + timedelta(days=10),
        "exercise_end": now + timedelta(days=11),
    }
    create_and_execute_collection_exercise('cb8accda-6118-4d3b-85a3-149e28960c54',
                                           period, 'test_exercise', dates)


@given('the "{survey}" "{period}" collection exercise for ru "{ru_ref}" is in the "{status}" status')
@then('the "{survey}" "{period}" collection exercise for ru "{ru_ref}" is in the "{status}" status')
def assert_collection_exercise_status(_, survey, period, ru_ref, status):
    reporting_unit.go_to(ru_ref)
    reporting_unit.click_data_panel('Bricks')
    collection_exericse = reporting_unit.get_collection_exercise(period, survey)
    assert status in collection_exericse['status'], collection_exericse['status']


@given('the respondent has been enrolled for Bricks 204901 for ru 49900000001 which is in Completed by phone status')
def already_enrolled(_):
    pass


@when('the internal user changes the response status for "{survey}" "{period}" to "{status}"')
def internal_user_changes_response_status(_, survey, period, status):
    reporting_unit.click_change_response_status_link(survey=survey, period=period)
    mapped_status = map_ce_status(status)
    change_response_status.update_response_status(mapped_status)


@given('the respondent has been enrolled for "{survey}" "{period}" for ru "{ru_ref}"')
def respondent_enrolled_for_ce(_, survey, period, ru_ref):
    party_id = party_controller.get_party_by_email(Config.RESPONDENT_USERNAME)['id']
    enrol_respondent(party_id, 'cb8accda-6118-4d3b-85a3-149e28960c54', period)


@when('the respondent goes to the history page')
def respondent_goes_to_history_page_for_49900000002(_):
    signed_in_respondent(_)
    surveys_history.go_to_history_tab()


@then('the respondent is presented the "{survey}" "{period}" "{ru_ref}" status as "{status}"')
def respondent_view_ce_status(_, survey, period, ru_ref, status):
    case = surveys_history.get_case(ru_ref)
    assert status == case.get('status'), case.get('status')
