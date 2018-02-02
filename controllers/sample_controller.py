from os.path import abspath

from acceptance_tests import browser
from config import Config


def load_sample(test_file):
    browser.visit('{}/surveys/{}/{}'.format(Config.RESPONSE_OPERATIONS_UI, 'Bricks', '201801'))
    browser.driver.find_element_by_id('sampleFile').send_keys(abspath(test_file))
    browser.find_by_id('btn-load-sample').click()
