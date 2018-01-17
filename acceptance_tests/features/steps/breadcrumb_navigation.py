from behave import when, then

from acceptance_tests.features.pages import collection_exercise_details, survey


@when('the user clicks the survey breadcrumb link')
def internal_user_views_home(_):
    collection_exercise_details.click_survey_breadcrumb()


@then('the user is taken to the surveys page')
def internal_user_is_taken_to_surveys_page(_):
    assert survey.get_page_title() == "Surveys"
