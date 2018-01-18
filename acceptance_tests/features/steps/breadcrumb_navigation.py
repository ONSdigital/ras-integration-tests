from behave import given, when, then

from acceptance_tests.features.pages import collection_exercise_details, home, survey


@given('the user accesses the system')
def user_accesses_the_system(_):
    pass


@when('the user clicks the survey breadcrumb link')
def internal_user_views_home(_):
    collection_exercise_details.click_survey_breadcrumb()


@then('the user is taken to the surveys page')
def internal_user_is_taken_to_surveys_page(_):
    assert survey.get_page_title() == "Surveys"


@then('the user does not see a breadcrumbs trail')
def internal_user_cannot_see_breadcrumb_trail(_):
    assert not home.get_breadcrumbs_list()


@then('the user can see breadcrumbs showing the site hierarchy')
def is_last_breadcrumb_the_title(_):
    breadcrumbs = collection_exercise_details.get_breadcrumbs()
    assert breadcrumbs[0] == 'Home'
    assert breadcrumbs[1] == 'Surveys'
    assert breadcrumbs[2] == '139 QBS'
    assert breadcrumbs[3] == '1803'
