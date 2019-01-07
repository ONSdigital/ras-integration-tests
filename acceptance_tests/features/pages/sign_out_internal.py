from acceptance_tests import browser
from acceptance_tests.features.pages import sign_in_internal


def signed_out_successfully_message():
    browser.find_by_id('successfully-signed-out')


def sign_out():
    browser.find_by_id('sign-out-btn').click()


def try_sign_out():
    sign_in_internal.go_to()

    if browser.find_by_id('sign-out-btn'):
        sign_out()
