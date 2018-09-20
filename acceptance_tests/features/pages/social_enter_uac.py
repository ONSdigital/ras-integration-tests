from acceptance_tests import browser
from config import Config


def go_to():
    browser.visit(f'{Config.RESPONDENT_HOME_UI}')


def enter_uac(iac):
    browser.driver.find_element_by_id('iac1').send_keys(iac[:4])
    browser.driver.find_element_by_id('iac2').send_keys(iac[4:8])
    browser.driver.find_element_by_id('iac3').send_keys(iac[8:])


def click_start_button():
    browser.driver.find_element_by_name('action[save_continue]').click()


def get_uac_error_text():
    return browser.driver.find_element_by_class_name('list__item').text
