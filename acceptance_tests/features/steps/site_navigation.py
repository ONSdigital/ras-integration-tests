from behave import when, then

from acceptance_tests.features.pages import collection_exercise, collection_exercise_details,  home, survey


@when('the internal user navigates to the home page')
def internal_user_views_home(_):
    home.go_to()


@then('the user can view and click on a link to the surveys list page')
def should_be_able_to_click_survey_link(_):
    home.click_surveys_link()
    assert survey.get_page_title() == 'Surveys'


@then('the user can view and click on a link to the QBS survey page')
def should_be_able_to_click_qbs_survey_link(_):
    survey.click_qbs_survey_link()
    assert collection_exercise.get_page_title() == 'Quarterly Business Survey'


@then('the user can view and click on a link to the 1803 QBS collection exercise page')
def should_be_able_to_click_qbs_collection_exercise_link(_):
    collection_exercise.click_qbs_1803_ce_link()
    assert collection_exercise_details.get_page_title() == 'QBS 1803'
