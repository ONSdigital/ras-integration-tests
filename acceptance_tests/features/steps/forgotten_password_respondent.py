from behave import given, then, when

from acceptance_tests import browser
from acceptance_tests.features.pages import forgotten_password_respondent, sign_in_respondent
from acceptance_tests.features.pages.forgotten_password_respondent import get_password_reset_url


@given('the user has an active account and they have forgotten their password')
def go_to_forgotten_password(_):
    forgotten_password_respondent.go_to_forgot_password_url()


@when('they enter a registered email address')
def enter_email_address(context):
    forgotten_password_respondent.enter_email_address(context.respondent_email)


@when('they enter a invalid email address')
def enter_invalid_email_address(_):
    forgotten_password_respondent.enter_email_address(' ')


@when('they enter a unregistered email address')
def enter_unregistered_email_address(_):
    forgotten_password_respondent.enter_email_address('fakeemail@email.com')


@then('the user is notified that they have had a password reset link email sent to them')
def password_reset_link_occurred(_):
    forgotten_password_respondent.send_reset_link()
    assert forgotten_password_respondent.password_reset_sent()


@then('the user is notified that a valid email address is required')
def invalid_email_error_occurred(_):
    forgotten_password_respondent.send_reset_link()
    assert forgotten_password_respondent.check_email_error_message()


@given('the user has received an expired link for the reset password form')
@given('the user has clicked an expired password reset link')
@when('they click a expired link')
def click_expired_password_link(context):
    forgotten_password_respondent.go_to_expired_password_request_url(context)


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
def password_reset_request_sent(_):
    assert forgotten_password_respondent.get_request_new_password()


@given('the user has received a link to reset password')
def user_received_password_reset_link(context):
    context.respondent_password_reset_link = get_password_reset_url(context)


@when('the user clicks the link')
def click_password_reset_link(context):
    browser.visit(context.respondent_password_reset_link)


@given('the user has clicked a valid password reset link')
def user_navigates_to_valid_password_reset(context):
    user_received_password_reset_link(context)
    click_password_reset_link(context)


@then('the user is taken to a reset password form')
def get_password_reset_form(_):
    assert forgotten_password_respondent.get_reset_password_message()


@when('the user enters a new password and an incorrect confirmed password')
def entering_in_invalid_passwords(_):
    forgotten_password_respondent.enter_in_passwords('Password1!', 'Password')


@when('they submit the new password')
def submitting_password(_):
    forgotten_password_respondent.click_confirm_new_password()


@then("the user is notified that the passwords don't match")
def passwords_is_invalid(_):
    assert forgotten_password_respondent.get_passwords_do_not_match_message()


@when('the user enters a new password and confirms the password')
def entering_in_valid_passwords(_):
    forgotten_password_respondent.enter_in_passwords('Password1!', 'Password1!')


@then('the user is notified that the password has been changed')
def confirm_password_changed_message(_):
    assert forgotten_password_respondent.get_password_changed_message()


@when('the user enters and confirms a new password which does not meet requirements')
def entering_passwords_does_not_meet_requirements(_):
    forgotten_password_respondent.enter_in_passwords('password', 'password')


@then('the user is notified that the password does not meet requirements')
def password_does_not_meet_requirements(_):
    assert forgotten_password_respondent.get_password_requirements_message()


@given('the user has reset their password')
def user_have_reset_their_password(context):
    user_received_password_reset_link(context)
    user_navigates_to_valid_password_reset(context)
    forgotten_password_respondent.enter_in_passwords('Password1!', 'Password1!')
    forgotten_password_respondent.click_confirm_new_password()


@when('the user enters their new credentials')
def respondent_logs_into_account(context):
    sign_in_respondent.go_to()
    browser.driver.find_element_by_id('username').send_keys(context.respondent_email)
    browser.driver.find_element_by_id('inputPassword').send_keys('Password1!')
    browser.find_by_id('sign_in_button').click()


@then('They successfully log in to their account')
def respondent_home_page(_):
    assert forgotten_password_respondent.respondent_successfully_logged_in()
