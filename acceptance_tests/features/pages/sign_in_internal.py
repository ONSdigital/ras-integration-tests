from acceptance_tests import browser
from config import Config


def go_to():
    browser.visit(Config.RESPONSE_OPERATIONS_UI + '/sign-in')


def enter_correct_username():
    browser.driver.find_element_by_id('username').send_keys(str(Config.INTERNAL_USERNAME))


def enter_incorrect_username():
    browser.driver.find_element_by_id('username').send_keys('someone')


def enter_correct_password():
    browser.driver.find_element_by_id('password').send_keys(str(Config.INTERNAL_PASSWORD))


def enter_incorrect_password():
    browser.driver.find_element_by_id('password').send_keys('words')


def internal_sign_in_button():
    browser.find_by_id('SIGN_IN_BUTTON').click()


def username_required():
    browser.find_link_by_text('Username is required')


def password_required():
    browser.find_link_by_text('Password is required')


def authentication_error_message():
    browser.find_by_id('try-again-link')
