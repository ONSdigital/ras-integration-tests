from behave import given, when, then

from acceptance_tests.features.pages import collection_exercise


@given('collection exercises for {survey} exist in the system')
def collection_exercises_for_a_survey_exist_in_the_system(_, survey):
    pass


@when('the internal user views the collection exercise page for {survey}')
def internal_user_views_the_collection_exercise_page(_, survey):
    collection_exercise.go_to(survey)


@then('the internal user can view relevant attributes for the survey')
def internal_user_can_view_relevant_attributes_for_the_survey(context):
    attributes = collection_exercise.get_survey_attributes()
    for row in context.table:
        assert attributes['survey_id'] == row['survey_id']
        assert attributes['survey_title'] == row['survey_title']
        assert attributes['survey_abbreviation'] == row['survey_abbreviation']
        assert attributes['survey_legal_basis'] == row['survey_legal_basis']


@then('the internal user can view all collection exercises for the survey')
def the_internal_user_can_view_all_collection_exercises_for_a_survey(_):
    # Validate collection exercise table headers
    table_headers = collection_exercise.get_table_headers()
    required_headers = ['Period', 'Shown to respondent as']
    assert table_headers == ' '.join(required_headers)

    # Validate the collection exercises
    collection_exercises = collection_exercise.get_collection_exercises()
    for ce in collection_exercises:
        assert ce['exercise_ref'].value
        assert ce['user_description'].value
