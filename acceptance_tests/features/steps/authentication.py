from behave import given

from acceptance_tests import browser
from acceptance_tests.features.pages import sign_in_internal
from acceptance_tests.features.pages import sign_in_respondent
from config import Config


@given('the respondent is signed into their account')
def signed_in_respondent(_):
    sign_in_respondent.go_to()
    # Only attempt to sign in if not already signed in otherwise implicitly redirected to homepage
    if '/sign-in' in browser.url:
        browser.driver.find_element_by_id('username').send_keys(Config.RESPONDENT_USERNAME)
        browser.driver.find_element_by_id('password').send_keys(Config.RESPONDENT_PASSWORD)
        browser.find_by_id('sign_in_button').click()


@given('The internal user is already signed in')
def signed_in_internal(_):
    sign_in_internal.go_to()
    # Only attempt to sign in if not already signed in otherwise implicitly redirected to homepage
    if '/sign-in' in browser.url:
        sign_in_internal.enter_correct_username()
        sign_in_internal.enter_correct_password()
        sign_in_internal.click_internal_sign_in_button()
