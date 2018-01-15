from behave import when, then

from acceptance_tests.features.pages import collection_exercise, collection_exercise_details,  home, survey


@when('the internal user navigates to the home page')
def internal_user_views_home(_):
    home.go_to()


@then('the user can view and click on a link to the surveys list page')
def internal_user_can_navigate_to_surveys_list(_):
    home.click_surveys_link()
    assert survey.get_page_title() == 'Surveys'


@then('the user can view and click on a link to the QBS survey page')
def internal_user_can_navigate_to_surveys_list(_):
    survey.click_qbs_survey_link()
    assert collection_exercise.get_page_title() == 'Quarterly Business Survey'


@then('the user can view and click on a link to the 1803 QBS collection exercise page')
def internal_user_can_navigate_to_surveys_list(_):
    collection_exercise.click_qbs_1803_ce_link()
    assert collection_exercise_details.get_page_title() == 'QBS 1803'
