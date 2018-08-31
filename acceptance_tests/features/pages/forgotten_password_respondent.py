from acceptance_tests import browser
from config import Config


def go_to_forgot_password_url():
    browser.visit(Config.FRONTSTAGE_SERVICE + '/sign-in')
    browser.find_link_by_href('/passwords/forgot-password').click()


def enter_correct_username():
    browser.driver.find_element_by_id('email_address').send_keys(str(Config.RESPONDENT_USERNAME))


def enter_invalid_username():
    browser.driver.find_element_by_id('email_address').send_keys(str(''))


def send_reset_link():
    browser.find_by_id('reset-password-btn').click()


def password_reset_sent():
    browser.find_link_by_text('Password reset request sent')


def check_email_error_message():
    browser.find_by_text('Invalid email address')
