from os.path import abspath

from acceptance_tests import browser
from config import Config


def load_sample(survey_name, period, test_file):
    browser.visit(f'{Config.RESPONSE_OPERATIONS_UI}/surveys/{survey_name}/{period}')
    browser.driver.find_element_by_id('sampleFile').send_keys(abspath(test_file))
    browser.driver.find_element_by_id('btn-load-sample').click()
