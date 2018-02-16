from behave import given, when, then

from acceptance_tests.features.pages import collection_exercise, collection_exercise_details
from controllers.collection_exercise_controller import get_survey_collection_exercises


@given('the collection exercises for that survey exist')
def ce_exist_for_survey(_):
    bricks_id = 'cb8accda-6118-4d3b-85a3-149e28960c54'
    collection_exercises = get_survey_collection_exercises(bricks_id)
    assert len(collection_exercises) != 0


@when('the internal user navigates to the survey details page')
@given('the internal user is on the survey details page')
def view_survey_details(_):
    collection_exercise.go_to('Bricks')


@then('the status of a collection exercise is Created')
def survey_ce_state_is_created(_):
    row = collection_exercise.get_table_row_by_period('201806')
    assert row['state'] == 'Created'


@when('the internal user navigates to the collection exercise details page')
def view_ce_details(_):
    collection_exercise_details.go_to('Bricks', '201806')


@then('the displayed status should be Created')
def ce_details_state_is_created(_):
    ce_state = collection_exercise_details.get_status()
    assert ce_state == 'Created'
