from acceptance_tests import browser
from common.survey_utilities import make_email_address


def get_new_iac():
    return browser.find_by_id('IAC')


def get_unused_iac():
    return browser.find_by_id('unused-enrolment-code')


def generate_random_email_address():
    return make_email_address()
