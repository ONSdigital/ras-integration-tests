from behave import given, when, then

from acceptance_tests.features.pages import collection_exercise, collection_exercise_details
from controllers.collection_exercise_controller import get_survey_collection_exercises


@given('a collection exercise has been created')
def collection_exercise_created(_):
    pass


@given('the collection exercises for that survey exist')
def ce_exist_for_survey(context):
    collection_exercises = get_survey_collection_exercises(context.survey_id)
    assert len(collection_exercises) == 1


@when('the internal user navigates to the survey details page')
@given('the internal user is on the survey details page')
def view_survey_details(context):
    collection_exercise.go_to(context.short_name)


@then('the status of a collection exercise is Created')
def survey_ce_state_is_created(context):
    ce_state = collection_exercise.get_table_row_by_period(context.period)['state']
    assert collection_exercise.is_created(ce_state), ce_state


@given('the internal user navigates to the collection exercise details page')
@when('the internal user navigates to the collection exercise details page')
def view_ce_details(context):
    collection_exercise_details.go_to(context.short_name, context.period)


@then('the displayed status should be Created')
def ce_details_state_is_created(_):
    ce_state = collection_exercise_details.get_status()
    assert collection_exercise.is_created(ce_state), ce_state
