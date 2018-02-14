from acceptance_tests import browser


def signed_out_successfully_message():
    browser.find_by_id('successfully-signed-out')


def sign_out():
    browser.find_by_id('sign-out-btn').click()
