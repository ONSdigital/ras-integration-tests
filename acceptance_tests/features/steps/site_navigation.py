from behave import when, then

from acceptance_tests.features.pages import collection_exercise, collection_exercise_details, home, survey


@when('the internal user navigates to the home page')
def internal_user_views_home(_):
    home.go_to()


@then('the user can view and click on a link to the surveys list page')
def should_be_able_to_click_survey_link(_):
    home.click_surveys_link()
    assert survey.get_page_title() == "Surveys | Survey Data Collection"


@then('the user can view and click on a link to the survey page')
def should_be_able_to_click_survey_link(context):
    survey.click_survey_link(context)
    assert collection_exercise.get_page_title() == f'{context.short_name} | Surveys | Survey Data Collection'


@then('the user can view and click on a link to the collection exercise page')
def should_be_able_to_click_collection_exercise_link(context):
    collection_exercise.click_ce_link(context.period)
    actual = collection_exercise_details.get_page_title()
    expected = f'{context.survey_ref} {context.short_name} {context.period} | Surveys | Survey Data Collection'
    assert actual == expected
