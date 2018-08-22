from behave import given, when, then

from acceptance_tests.features.pages import social_enter_uac_rh
from config import Config


@given('a Household Respondent has received a UAC')
def respondent_navigates_to_respondent_home(_):
    social_enter_uac_rh.go_to()


@when('they enter the UAC into Respondent Home')
def respondent_enters_uac_into_respondent_home(context):
    social_enter_uac_rh.enter_uac(context.social_iac)
    social_enter_uac_rh.click_start_button()


@then('they are able to access the eQ landing page')
def respondent_is_redirected_to_eq(_):
    location = social_enter_uac_rh.get_location()
    assert Config.EQ_URL in location, location
