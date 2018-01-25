from behave import given, when, then

from acceptance_tests.features.pages import breadcrumbs, survey


@given('the user accesses the system')
def user_accesses_the_system(_):
    pass


@when('the user clicks the survey breadcrumb link')
def internal_user_clicks_survey_breadcrumb(_):
    breadcrumbs.click_breadcrumb(2)


@then('the user is taken to the surveys page')
def internal_user_is_taken_to_surveys_page(_):
    assert survey.get_page_title() == "Surveys | Survey Data Collection"


@then('the user does not see a breadcrumbs trail')
def internal_user_cannot_see_breadcrumb_trail(_):
    assert not breadcrumbs.breadcrumbs_exists()


@then('the user can see breadcrumbs showing the site hierarchy')
def site_hierarchy_in_breadcrumb_trail(_):
    breadcrumbs_list = breadcrumbs.get_breadcrumbs()
    assert breadcrumbs_list[0] == 'Home'
    assert breadcrumbs_list[1] == 'Surveys'
    assert breadcrumbs_list[2] == '139 QBS'
    assert breadcrumbs_list[3] == '1803'
