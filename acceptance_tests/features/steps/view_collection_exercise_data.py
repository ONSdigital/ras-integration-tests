from behave import given, when, then

from acceptance_tests.features.pages import collection_exercise


@given('collection exercises for a survey exist in the system')
def collection_exercises_for_a_survey_exist_in_the_system(_):
    pass


@when('the internal user views the collection exercise page')
def internal_user_views_the_collection_exercise_page(_):
    collection_exercise.go_to()


@then('the internal user can view all surveys')
def internal_user_can_view_all_survey_details(context):
    surveys = survey.get_surveys()

    for row in context.table:
        survey_by_id = next(filter(lambda s: s['id'] == row['survey_id'], surveys))
        assert survey_by_id['id'] == row['survey_id']
        assert survey_by_id['name'] == row['survey_name']
        assert survey_by_id['short_name'] == row['survey_short_name']
        assert survey_by_id['legal_basis'] == row['survey_legal_basis']
