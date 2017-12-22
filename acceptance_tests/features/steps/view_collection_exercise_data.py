from behave import given, when, then

from acceptance_tests.features.pages import collection_exercise


@given('collection exercises for a survey exist in the system')
def collection_exercises_for_a_survey_exist_in_the_system(_):
    pass


@when('the internal user views the collection exercise page')
def internal_user_views_the_collection_exercise_page(_):
    collection_exercise.go_to()


@then('the internal user can view relevant attributes for a survey')
def internal_user_can_view_relevant_attributes_for_a_survey(context):
    context.attributes = collection_exercise.get_survey_attributes()

    # TODO Assert string matching against context table from scenario here

@then('')
def