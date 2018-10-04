from behave import given, when, then

from acceptance_tests import browser
from acceptance_tests.features.pages import forgotten_password_respondent, sign_in_respondent
from common.generate_token import generate_email_token
from config import Config


@given('the user has an active account and they have forgotten their password')
def go_to_forgotten_password(_):
    forgotten_password_respondent.go_to_forgot_password_url()


@when('they enter a registered email address')
def enter_email_address(_):
    forgotten_password_respondent.enter_username(str(Config.RESPONDENT_USERNAME))


@when('they enter a invalid email address')
def enter_invalid_email_address(_):
    forgotten_password_respondent.enter_username(' ')


@when('they enter a unregistered email address')
def enter_unregistered_email_address(_):
    forgotten_password_respondent.enter_username('fakeemail@email.com')


@then('the user is notified that they have had a password reset link email sent to them')
def password_reset_link_occurred(_):
    forgotten_password_respondent.send_reset_link()
    assert forgotten_password_respondent.password_reset_sent()


@then('the user is notified that a valid email address is required')
def invalid_email_error_occurred(_):
    forgotten_password_respondent.send_reset_link()
    assert forgotten_password_respondent.check_email_error_message()


@given('the user has received an expired link for the reset password form')
@when('they click a expired link')
def click_expired_password_link(_):
    forgotten_password_respondent.go_to_expired_password_request_url()


@then('the user is notified that the link has expired')
@given('the user has been notified that the link they used has expired')
def notified_link_has_expired(_):
    assert forgotten_password_respondent.get_expired_message()


@then('can now request a new link')
def request_new_password_link_available(_):
    assert forgotten_password_respondent.get_request_new_password_email()


@when('they click the request new password link')
def click_request_new_password_link_(_):
    forgotten_password_respondent.click_request_new_password_email()


@then('the user is notified that they should check their email')
@given('a user has received a link to reset password')
def password_reset_request_sent(_):
    assert forgotten_password_respondent.get_request_new_password()


@when('"{email}" clicks the link')
def click_password_reset_link(_, email):
    token = generate_email_token(email)
    url = f'{Config.FRONTSTAGE_SERVICE}/passwords/reset-password/{token}'
    browser.visit(url)


@then('the user is taken to a reset password form')
def get_password_reset_form(_):
    assert forgotten_password_respondent.get_reset_password_message()


@given('the user has entered a new password and an incorrect confirmed password')
def entering_in_invalid_passwords(_):
    forgotten_password_respondent.enter_in_passwords('Password1!', 'Password')


@when('they submit the new password')
def submitting_password(_):
    forgotten_password_respondent.click_confirm_new_password()


@then("the user is notified that the passwords don't match")
def passwords_is_invalid(_):
    assert forgotten_password_respondent.get_passwords_do_not_match_message()


@given('the user has entered a new password and confirmed the password')
def entering_in_valid_passwords(_):
    forgotten_password_respondent.enter_in_passwords('Password1!', 'Password1!')


@then('the user is notified that the password has been changed')
@given('the user has reset their password')
def password_changed(_):
    assert forgotten_password_respondent.get_password_changed_message()


@given('the user has entered a new password and confirmed the password which does not meet requirements')
def entering_passwords_does_not_meet_requirements(_):
    forgotten_password_respondent.enter_in_passwords('password', 'password')


@then('the user is notified that the password does not meet requirements')
def password_does_not_meet_requirements(_):
    assert forgotten_password_respondent.get_password_requirements_message()


@when('"{username}" enters their credentials')
def respondent_logs_into_account(_, username):
    sign_in_respondent.go_to()
    browser.driver.find_element_by_id('username').send_keys(username)
    browser.driver.find_element_by_id('inputPassword').send_keys('Password1!')
    browser.find_by_id('sign_in_button').click()


@then('They successfully log in to their account')
def respondent_home_page(_):
    assert forgotten_password_respondent.respondent_successfully_logged_in()
