from acceptance_tests import browser
from config import Config


def go_to():
    browser.visit(f"{Config.RESPONSE_OPERATIONS_SOCIAL_UI}/")


def get_page_title():
    return browser.title


def get_search_results():
    return browser.find_by_id('search-results-info').text


def get_reference_number():
    return browser.driver.find_element_by_id('search-results-case-link-1').text


def get_postcode():
    return browser.driver.find_element_by_id('search-results-postcode-1').text


def get_address():
    return browser.driver.find_element_by_id('search-results-address-1').text


def click_search_by_postcode():
    browser.driver.find_element_by_id('postcode-search-submit').click()


def click_case_link():
    browser.driver.find_element_by_id('search-results-case-link-1').click()


def enter_postcode(postcode):
    browser.driver.find_element_by_id('postcode-search').send_keys(postcode)
