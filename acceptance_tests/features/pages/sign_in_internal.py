from acceptance_tests import browser
from config import Config


def go_to():
    browser.visit(Config.RESPONSE_OPERATIONS_UI + '/sign-in')


def get_page_title():
    return browser.title


def enter_correct_username(user_name):
    browser.driver.find_element_by_id('username').send_keys(user_name)


def enter_incorrect_username():
    browser.driver.find_element_by_id('username').send_keys('someone')


def enter_correct_password():
    browser.driver.find_element_by_id('password').send_keys(str(Config.INTERNAL_PASSWORD))


def enter_incorrect_password():
    browser.driver.find_element_by_id('password').send_keys('words')


def click_internal_sign_in_button():
    browser.find_by_id('SIGN_IN_BUTTON').click()


def check_username_required():
    browser.find_link_by_text('Please enter a username')


def check_password_required():
    browser.find_link_by_text('Please enter a password')


def check_authentication_error_message():
    browser.find_by_id('try-again-link')
