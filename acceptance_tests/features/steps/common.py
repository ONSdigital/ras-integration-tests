from behave import given, then, when

from acceptance_tests.features.pages import sign_in_respondent
from acceptance_tests.features.pages import sign_in_internal
from acceptance_tests import browser
from config import Config


@given('the respondent is signed into their account')
def signed_in_frontstage(_):
    sign_in_respondent.go_to()
    browser.driver.find_element_by_id('username').send_keys(Config.RESPONDENT_USERNAME)
    browser.driver.find_element_by_id('password').send_keys(Config.RESPONDENT_PASSWORD)
    browser.find_by_id('SIGN_IN_BUTTON').click()


@when('they click the sign out link')
@then('the internal user signs out')
def signed_out_internal(_):
    browser.find_by_id('sign-out-btn').click()


@given('The internal user is already signed in')
def signed_in_rops(_):
    sign_in_internal.go_to()
    sign_in_internal.enter_correct_username()
    sign_in_internal.enter_correct_password()
    sign_in_internal.click_internal_sign_in_button()
