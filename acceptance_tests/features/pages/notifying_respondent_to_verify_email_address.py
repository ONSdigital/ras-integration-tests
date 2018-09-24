import time

from acceptance_tests import browser
from acceptance_tests.features.pages import sign_in_respondent


def enter_credentials(username, password):
    sign_in_respondent.go_to()
    browser.driver.find_element_by_id('username').send_keys(username)
    browser.driver.find_element_by_id('inputPassword').send_keys(password)


def log_in_respondent(_):
    browser.find_by_id('sign_in_button').click()


def get_verification_message(_):
    return browser.find_by_text('Verify your email')


def click_verification_link(_):
    browser.find_by_text('request another email').click()


def get_verification_resend_message(_):
    return browser.find_by_text('Please follow the link in the email we\'ve sent you to verify your email address '
                                'and sign in to your account.')
