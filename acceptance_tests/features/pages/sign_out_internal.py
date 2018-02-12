from acceptance_tests import browser


def signed_out_successfully_message():
    browser.find_by_id('successfully-signed-out')
