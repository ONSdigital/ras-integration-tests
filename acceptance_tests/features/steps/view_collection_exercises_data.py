from behave import given, when, then

from acceptance_tests.features.pages import collection_exercise


@given('collection exercises for {survey} exist in the system')
def collection_exercises_for_a_survey_exist_in_the_system(_, survey):
    pass


@given('all surveys have collection exercises')
def all_surveys_have_collection_exercises(_):
    pass


@when('the internal user views the collection exercise page for {survey}')
def internal_user_views_the_collection_exercise_page_for_survey(_, survey):
    collection_exercise.go_to(survey)


@then('the internal user can view relevant attributes for QBS')
def internal_user_can_view_relevant_attributes_for_qbs(context):
    attributes = collection_exercise.get_survey_attributes()
    for row in context.table:
        assert attributes['survey_id'] == row['survey_id']
        assert attributes['survey_title'] == row['survey_title']
        assert attributes['survey_abbreviation'] == row['survey_abbreviation']
        assert attributes['survey_legal_basis'] == row['survey_legal_basis']


@then('the internal user can view all collection exercises for QBS')
def the_internal_user_can_view_all_collection_exercises_for_qbs(context):
    # Validate collection exercise table headers
    table_headers = collection_exercise.get_table_headers()
    required_headers = ['Period', 'Shown to respondent as', 'Status']
    assert table_headers == ' '.join(required_headers)

    # Validate rows to ensure values are in the correct columns
    collection_exercises = collection_exercise.get_collection_exercises()
    for row in context.table:
        collection_exercises_by_period = next(filter(lambda ce: ce['exercise_ref'] == row['period'],
                                                     collection_exercises))
        assert collection_exercises_by_period['exercise_ref'] == row['period']
        assert collection_exercises_by_period['user_description'] == row['shown_to_respondent_as']
        assert collection_exercises_by_period['state'] == row['status']


@then('there is at least one collection exercise')
def there_is_at_least_one_collection_exercise(_):
    collection_exercises = collection_exercise.get_collection_exercises()
    assert len(collection_exercises) > 0
