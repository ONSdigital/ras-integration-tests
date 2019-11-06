from datetime import datetime, timezone

from behave import given, when, then

from acceptance_tests.features.pages import collection_exercise, collection_exercise_details
from common.browser_utilities import is_text_present_with_retry


@given('a new collection exercise has been created')
def collection_exercise_created(context):
    pass


@given('the user has confirmed that the collection exercise is Ready for Live')
def internal_user_views_ready_for_live(context):
    collection_exercise_details.go_to(context.short_name, context.period)
    is_text_present_with_retry('Ready for live', 10)
    ce_state = collection_exercise_details.get_status()
    assert collection_exercise.is_ready_for_live(ce_state), ce_state


@given('the user is on the collection exercise Page')
@when('they navigate to the collection exercise page')
def user_navigate_to_survey_details(context):
    collection_exercise.go_to(context.short_name)


@when('the collection exercise go live date hits')
def go_live_date_hits(context):
    while True:
        if datetime.now(timezone.utc) > context.dates['go_live']:
            return


@then('the state of a collection exercise is to be changed to Live')
@then('they are able to see the Live Status for that Collection Exercise')
def ce_details_state_is_live(_):
    assert is_text_present_with_retry('Live', 10)


@then('they are able to see the Live Status')
def survey_ce_state_is_live(context):
    ce_state = collection_exercise.get_table_row_by_period(context.period)['state']
    assert collection_exercise.is_live(ce_state), ce_state
