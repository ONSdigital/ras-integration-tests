from behave import given, when, then

from acceptance_tests.features.pages import collection_exercise


@given('collection exercises for {survey} exist in the system')
def collection_exercises_for_a_survey_exist_in_the_system(context, survey):
    pass


@when('the internal user views the collection exercise page for {survey}')
def internal_user_views_the_collection_exercise_page(context, survey):
    collection_exercise.go_to(survey)


@then('the internal user can view relevant attributes for the survey')
def internal_user_can_view_relevant_attributes_for_the_survey(context):
    attributes = collection_exercise.get_survey_attributes()
    for row in context.table:
        assert attributes['survey_id'] == row['survey_id']
        assert attributes['survey_title'] == row['survey_title']
        assert attributes['survey_abbreviation'] == row['survey_abbreviation']
        assert attributes['survey_legal_basis'] == row['survey_legal_basis']


@then('the internal user can view all collection exercises for {survey}')
def the_internal_user_can_view_all_collection_exercises_for_a_survey(context, survey):
    # TODO:     This data would be dynamic, so how should we assert? E.g. an
    # TODO:     annual survey collex for 2016, so assert row count of 1... what about 2017 etc?

    raise NotImplementedError('STEP: Then the internal user can view all collection exercises for <survey>')
