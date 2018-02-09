from acceptance_tests import browser
from config import Config


def go_to_find_ru():
    browser.visit('{}/reporting-units'.format(Config.RESPONSE_OPERATIONS_UI))


def search_reporting_unit(query):
    browser.find_by_id('query').fill(query)
    browser.find_by_id('btn-search-ru').click()


def get_reporting_units():
    tds = browser.find_by_id('tbl-businesses').find_by_tag('tbody').find_by_tag('td')
    return list(map(lambda td: td.value, tds))
