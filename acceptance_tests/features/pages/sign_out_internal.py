from acceptance_tests import browser


def internal_sign_out_link():
    browser.find_by_id('SIGN_OUT_LINK').click()
