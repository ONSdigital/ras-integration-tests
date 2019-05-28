from behave import given, when

from acceptance_tests import browser
from acceptance_tests.features.pages import sign_in_internal, social_sign_in_internal
from acceptance_tests.features.pages import sign_in_respondent
from config import Config


@given('the respondent is signed into their account')
@when('the respondent is signed into their account')
def signed_in_respondent(context):
    sign_in_respondent.go_to()
    # Only attempt to sign in if not already signed in otherwise implicitly redirected to homepage
    if '/sign-in' in browser.url:
        browser.driver.find_element_by_id('username').send_keys(context.respondent_email)
        browser.driver.find_element_by_id('inputPassword').send_keys(Config.RESPONDENT_PASSWORD)
        browser.find_by_id('sign_in_button').click()


@given('The internal user is already signed in')
@when('The internal user is already signed in')
def signed_in_internal(context):
    internal_user_name = getattr(context, 'internal_user_name', Config.INTERNAL_USERNAME)
    _sign_in_internal_user(internal_user_name)


@given('an alternate internal user signs in')
@when('an alternate internal user signs in')
def signed_in_internal_alternate_user(context):
    _sign_in_internal_user(context.alternate_internal_user_name)


def _sign_in_internal_user(user_name):
    sign_in_internal.go_to()
    # Only attempt to sign in if not already signed in otherwise implicitly redirected to homepage
    if '/sign-in' in browser.url:
        sign_in_internal.enter_correct_username(user_name)
        sign_in_internal.enter_correct_password()
        sign_in_internal.click_internal_sign_in_button()


@given('The internal user is already signed in to social UI')
def signed_in_internal_social(context):
    social_sign_in_internal.go_to()
    # Only attempt to sign in if not already signed in otherwise implicitly redirected to homepage
    if '/sign-in' in browser.url:
        # todo temp fix until all converted
        internal_user_name = getattr(context, 'internal_user_name', Config.INTERNAL_USERNAME)

        sign_in_internal.enter_correct_username(internal_user_name)
        sign_in_internal.enter_correct_password()
        sign_in_internal.click_internal_sign_in_button()


def sign_in_respondent_without_go_to(context):
    if '/sign-in' in browser.url:
        browser.driver.find_element_by_id('username').send_keys(context.respondent_email)
        browser.driver.find_element_by_id('inputPassword').send_keys(Config.RESPONDENT_PASSWORD)
        browser.find_by_id('sign_in_button').click()
