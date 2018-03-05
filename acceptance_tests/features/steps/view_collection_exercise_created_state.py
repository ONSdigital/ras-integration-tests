from behave import given, when, then

from acceptance_tests.features.pages import collection_exercise, collection_exercise_details
from controllers.collection_exercise_controller import get_survey_collection_exercises


@given('the collection exercises for that survey exist')
def ce_exist_for_survey(_):
    rsi_id = '75b19ea0-69a4-4c58-8d7f-4458c8f43f5c'
    collection_exercises = get_survey_collection_exercises(rsi_id)
    assert len(collection_exercises) != 0


@when('the internal user navigates to the survey details page')
@given('the internal user is on the survey details page')
def view_survey_details(_):
    collection_exercise.go_to('RSI')


@then('the status of a collection exercise is Created')
def survey_ce_state_is_created(_):
    ce_state = collection_exercise.get_table_row_by_period('201801')['state']
    assert collection_exercise.is_created(ce_state), ce_state


@when('the internal user navigates to the collection exercise details page')
def view_ce_details(_):
    collection_exercise_details.go_to('RSI', '201801')


@then('the displayed status should be Created')
def ce_details_state_is_created(_):
    ce_state = collection_exercise_details.get_status()
    assert collection_exercise.is_created(ce_state), ce_state
