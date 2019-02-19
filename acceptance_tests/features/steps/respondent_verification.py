from behave import given, then, when

from acceptance_tests import browser
from acceptance_tests.features.pages import sign_in_respondent
from acceptance_tests.features.pages.respondent_verification import click_sign_in_button, click_verification_link, \
    enter_credentials, get_unverified_message
from acceptance_tests.features.pages.respondent import click_resend_verification_email, go_to_find_respondent, confirm_on_respondent_page, search_respondent_by_email
from common.generate_token import generate_email_token, generate_expired_email_token
from config import Config


@given('the respondent with unverified account navigates to the sign in page')
def navigate_to_sign_in_page(_):
    sign_in_respondent.go_to()


@when('they enter correct credentials')
def log_in_attempt(context):
    enter_credentials(username=context.respondent_email, password=Config.RESPONDENT_PASSWORD)
    click_sign_in_button()


@then('they are shown on-screen notification to verify their email')
def verification_page(_):
    assert get_unverified_message()


@then('They are shown on-screen notification to request a verification link email')
def request_verification_link(_):
    assert click_verification_link()


@when('the respondent clicks an expired verification link')
@given('the respondent has clicked an expired account verification link')
def user_clicks_expired_verification_link(context):
    expired_token = generate_expired_email_token(context.respondent_email)
    browser.visit(f'{Config.FRONTSTAGE_SERVICE}/register/activate-account/{expired_token}')


@given('a user has received a verification link')
def receive_email_verification_link(context):
    token = generate_email_token(context.respondent_email)
    context.email_verification_link = f'{Config.FRONTSTAGE_SERVICE}/register/activate-account/{token}'


@when('the respondent clicks a valid verification link in the email')
def click_valid_verification_link(context):
    token = generate_email_token(context.respondent_email)
    browser.visit(f'{Config.FRONTSTAGE_SERVICE}/register/activate-account/{token}')


@then('the user is notified that their link has expired, and given the option to re-send a verification email')
@given('the user has been notified their link has expired')
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
    assert '/sign-in/?account_activated=True' in browser.url
    assert browser.find_by_text("You've activated your account")


@when('the internal user clicks re-send verification email')
@given('the internal user clicks re-send verification email')
def click_resend_verification(_):
   browser.find_by_id('resend-verification-email-btn').click()


@then('then they are redirected to a confirmation screen')
def resend_confirmation_screen(_):
    assert 'Re-send verification email' in browser.title


@given('the user is already on the confirmation screen')
def go_to_resend_confirmation(email):
    go_to_find_respondent()
    search_respondent_by_email(email)
    browser.find_by_id('resend-verification-email-btn').click()


@when('they press confirm')
def click_confirm(_):
    browser.find_by_id('confirm').click()


@when('they press cancel')
def click_confirm(_):
    browser.find_by_id('cancel').click()


@then('they are redirected to the respondents page and a confirmation message is displayed')
def confirm_email_resend(_):
    assert browser.find_by_text('Verification email re-sent')
