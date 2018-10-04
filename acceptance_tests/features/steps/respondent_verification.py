from behave import given, when, then

from acceptance_tests import browser
from acceptance_tests.features.pages.respondent_verification import enter_credentials, \
    log_in_respondent, get_verification_message, click_verification_link, get_unverified_message
from common.generate_token import generate_email_token
from config import Config


@given('an external "{user}" with unverified account tried to sign into their account')
def enter_respondent_credentials(_, user):
    enter_credentials(username=user, password=Config.RESPONDENT_PASSWORD)


@when('they enter correct credentials')
@given('they enter correct credentials')
def log_in_attempt(_):
    log_in_respondent()


@then('they are shown on-screen notification to verify their email')
def verification_page(_):
    assert get_unverified_message()


@then('They are shown on-screen notification to request a verification link email')
def request_verification_link(_):
    assert click_verification_link()


@given('a user has an expired verification link')
@when('they click the expired verification link')
def click_expired_verification_link(_):
    url = f'{Config.FRONTSTAGE_SERVICE}/register/activate-account/InVudmVyaWZpZWQxQGVtYWlsLmNvbSI.DoOicQ.Fi4dkj3J1C' \
          f'41Ehd4qNhnOdsZELc'
    browser.visit(url)


@given('a user has received a verification link')
def unverified_user_page(_):
    assert get_verification_message()


@when('they select the verification link in the email "{email}"')
def click_valid_verification_link(_, email):
    return _click_verification_link(email)


@then('the user is notified that their link has expired, and given the option to re-send a verification email')
@given('a user has been notified their link has expired')
def get_expired_verification_message(_):
    assert browser.find_by_text("Your link has expired")
    assert browser.find_by_text("request another verification email")


@when('they select the re-send verification email link')
def click_resend_verification_link(_):
    browser.find_by_text("request another verification email").click()


@then('they are notified that their verification email has been re-sent')
def resend_verification_page(_):
    assert browser.find_by_text('Check your email')


@then('the user is taken to a page stating their account has been activated')
def verified_user_page(_):
    assert browser.url == f'{Config.FRONTSTAGE_SERVICE}/sign-in/?account_activated=True'
    assert browser.find_by_text("You've activated your account")


def _click_verification_link(email):
    token = generate_email_token(email)
    url = f'{Config.FRONTSTAGE_SERVICE}/register/activate-account/{token}'
    browser.visit(url)
