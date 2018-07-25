from acceptance_tests.features.pages import forgotten_password_respondent
from behave import given, when, then


@given('the user has an active account and they have forgotten their password')
def go_to_forgotten_password(_):
    forgotten_password_respondent.go_to_forgot_password_url()


@when('they enter a registered email address')
def enter_email_address(_):
    forgotten_password_respondent.enter_correct_username()


@when('they enter a invalid email address')
def enter_invalid_email_address(_):
    forgotten_password_respondent.enter_invalid_username()


@then('the user is notified that they have had a password reset link email sent to them')
def password_reset_link_occurred(_):
    forgotten_password_respondent.send_reset_link()
    forgotten_password_respondent.password_reset_sent()


@then('the user is notified that a valid email address is required')
def invalid_email_error_occurred(_):
    forgotten_password_respondent.check_email_error_message()
