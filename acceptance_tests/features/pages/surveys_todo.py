import time

from acceptance_tests import browser
from config import Config


def go_to():
    browser.visit(Config.FRONTSTAGE_SERVICE + '/surveys/')


def get_collection_exercise_periods():
    return browser.find_by_id('SURVEY_PERIOD')


def get_surveys_list():
    return browser.find_by_id('survey-list')


def access_survey(survey_name):
    surveys_list = get_surveys_list()

    for survey in surveys_list.find_by_tag('li'):
        if survey.find_by_id('SURVEY_NAME') and survey_name in survey.find_by_id('SURVEY_NAME').text:
            survey.find_by_tag('button').click()


def select_to_create_message():
    browser.find_by_id('create-message-link-1').click()


def get_status_text(expected):
    for c in range(5):
        if browser.find_by_id('status-1').text == expected:
            break
        time.sleep(1)
    return browser.find_by_id('status-1').text
