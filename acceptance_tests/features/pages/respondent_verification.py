from acceptance_tests import browser
from acceptance_tests.features.pages import sign_in_respondent


def enter_credentials(username, password):
    sign_in_respondent.go_to()
    browser.driver.find_element_by_id('username').send_keys(username)
    browser.driver.find_element_by_id('inputPassword').send_keys(password)


def click_sign_in_button():
    browser.find_by_id('sign_in_button').click()


def get_verification_message():
    return browser.find_by_text('Check your email')


def get_unverified_message():
    return browser.find_by_text('Verify your email')


def click_verification_link():
    return browser.find_by_text('request another email')


def get_verification_resend_message():
    return browser.find_by_text('Please follow the link in the email we\'ve sent you to verify your email address '
                                'and sign in to your account.')
