from acceptance_tests import browser
from config import Config


def go_to(ru_ref):
    browser.visit(f"{Config.RESPONSE_OPERATIONS_UI}/reporting-units/{ru_ref}")


def get_ru_ref():
    return browser.find_by_id('RU_REF').text


def get_ru_name():
    return browser.find_by_id('RU_NAME').text
