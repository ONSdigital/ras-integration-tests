from acceptance_tests import browser


def sign_out():
    browser.find_by_id('SIGN_OUT_BTN').click()


def try_sign_out():
    if browser.find_by_id('SIGN_OUT_BTN'):
        sign_out()
