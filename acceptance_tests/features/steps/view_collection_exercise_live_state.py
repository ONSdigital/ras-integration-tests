from datetime import datetime, timedelta

from behave import given, when, then

from acceptance_tests.features.pages import collection_exercise, collection_exercise_details
from common.browser_utilities import is_text_present_with_retry
from controllers import collection_exercise_controller


@given('a new exercise with period "{period}" is created and executed for BRICKS')
def create_execute_new_exercise(context, period):
    if collection_exercise_controller.get_collection_exercise('cb8accda-6118-4d3b-85a3-149e28960c54', period):
        return
    now = datetime.utcnow()
    go_live = now + timedelta(minutes=2)
    context.go_live = go_live
    dates = {
        "mps": now + timedelta(seconds=5),
        "go_live": go_live,
        "return_by": now + timedelta(days=10),
        "exercise_end": now + timedelta(days=11)
    }
    collection_exercise_controller.create_and_execute_collection_exercise('cb8accda-6118-4d3b-85a3-149e28960c54',
                                                                          period, 'test_exercise', dates)


@given('the user has confirmed that "{survey}" "{period}" is Ready for Live')
def internal_user_views_ready_for_live(_, survey, period):
    collection_exercise_details.go_to(survey, period)
    is_text_present_with_retry('Ready for live', 10)
    ce_state = collection_exercise_details.get_status()
    assert collection_exercise.is_ready_for_live(ce_state), ce_state


@given('the user is on the "{survey}" Page')
@when('they navigate to the "{survey}" page')
def user_navigate_to_survey_details(_, survey):
    collection_exercise.go_to(survey)


@when('they navigate to the Collection Exercise Details Page for "{period}"')
def user_navigate_to_ce_details(_, period):
    collection_exercise.click_ce_link(period)


@when('"{survey}" "{period}" go live date hits')
def go_live_date_hits(context, survey, period):
    while True:
        if datetime.utcnow() > context.go_live:
            return


@then('the state of a collection exercise is to be changed to Live')
@then('they are able to see the Live Status for that Collection Exercise')
def ce_details_state_is_live(_):
    assert is_text_present_with_retry('Live', 10)


@then('they are able to see the Live Status for "{period}"')
def survey_ce_state_is_live(_, period):
    ce_state = collection_exercise.get_table_row_by_period(period)['state']
    assert collection_exercise.is_live(ce_state), ce_state
