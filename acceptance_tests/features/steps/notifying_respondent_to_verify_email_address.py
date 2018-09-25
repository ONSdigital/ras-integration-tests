from behave import given, when, then

from acceptance_tests import browser
from acceptance_tests.features.pages.notifying_respondent_to_verify_email_address import enter_credentials, \
    log_in_respondent, get_verification_message
from common.generate_token import generate_email_token
from config import Config


@given('an external user with unverified account tried to sign into their account')
def enter_respondent_credentials(_):
    enter_credentials(username='unverified@test.com', password=Config.RESPONDENT_PASSWORD)


@when('they enter correct credentials')
def log_in_attempt(_):
    log_in_respondent(_)


@then('they are shown on-screen notification to check their email')
def verification_page(_):
    assert get_verification_message(_)


@given('a user is notified their link has expired')
def verification_link_expired(_):
    assert get_verification_message(_)


@when('they select the verification link in the email')
def click_verification_link(_):
    email = 'unverified@test.com'
    token = generate_email_token(email)
    url = f'{Config.FRONTSTAGE_SERVICE}/register/activate-account/{token}'
    browser.visit(url)


@then('the user is taken to a page stating their account has been activated')
def verified_user_page(_):
    assert browser.url == f'{Config.FRONTSTAGE_SERVICE}/sign-in/?account_activated=True'
    assert browser.find_by_text("You've activated your account")
