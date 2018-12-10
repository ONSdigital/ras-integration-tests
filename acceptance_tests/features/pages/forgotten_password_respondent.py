from acceptance_tests import browser
from common.generate_token import generate_email_token, generate_expired_email_token
from config import Config


def go_to_forgot_password_url():
    browser.visit(Config.FRONTSTAGE_SERVICE + '/sign-in')
    browser.find_link_by_href('/passwords/forgot-password').click()


def enter_email_address(email_address):
    browser.driver.find_element_by_id('email_address').send_keys(email_address)


def send_reset_link():
    browser.find_by_id('reset-password-btn').click()


def password_reset_sent():
    return browser.find_by_text('Password reset request sent')


def check_email_error_message():
    return browser.find_by_text('Invalid email address')


def go_to_expired_password_request_url(context):
    expired_token = generate_expired_email_token(context.respondent_email)
    browser.visit(f'{Config.FRONTSTAGE_SERVICE}/passwords/reset-password/{expired_token}')


def get_password_reset_url(context):
    token = generate_email_token(context.respondent_email)
    return f'{Config.FRONTSTAGE_SERVICE}/passwords/reset-password/{token}'


def get_expired_message():
    return browser.find_by_text('Your link has expired')


def get_request_new_password_email():
    return browser.find_link_by_text('request another password reset email')


def click_request_new_password_email():
    browser.find_link_by_text('request another password reset email').click()


def get_request_new_password():
    return browser.find_by_text('Check your email')


def get_reset_password_message():
    return browser.find_by_text('Reset your password')


def click_confirm_new_password():
    browser.find_by_id('confirm_password_button').click()


def get_passwords_do_not_match_message():
    return browser.find_by_text('Your passwords do not match')


def get_password_changed_message():
    return browser.find_by_text('Your password has been changed')


def enter_in_passwords(password, confirm_password):
    browser.driver.find_element_by_id('inputPassword').send_keys(password)
    browser.driver.find_element_by_id('password_confirm').send_keys(confirm_password)


def get_password_requirements_message():
    return browser.find_by_text("Your password doesn't meet the requirements")


def respondent_successfully_logged_in():
    return browser.find_by_text('ONS Business Surveys')
