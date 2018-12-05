from acceptance_tests import browser


def get_new_iac():
    return browser.find_by_id('IAC')


def get_unused_iac():
    return browser.find_by_id('unused-enrolment-code')
