from acceptance_tests import browser


def get_iac():
    return browser.find_by_id('IAC')
