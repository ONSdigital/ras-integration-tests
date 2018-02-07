from acceptance_tests import browser
from config import Config


def go_to():
    browser.visit(Config.FRONTSTAGE_SERVICE + '/surveys/')


def get_collection_exercise_periods():
    return browser.find_by_id('SURVEY_PERIOD')
