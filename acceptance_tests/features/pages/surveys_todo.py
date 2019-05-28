from acceptance_tests import browser
from config import Config
from common.browser_utilities import wait_for_element_by_name, wait_for_element_by_id


def go_to():
    target_url = Config.FRONTSTAGE_SERVICE + '/surveys/todo'
    browser.visit(target_url)


def get_collection_exercise_periods():
    wait_for_element_by_name('period', timeout=3, retry=1)
    return browser.find_by_name('period')


def get_surveys_list():
    wait_for_element_by_id('survey-list', timeout=3, retry=1)
    return browser.find_by_id('survey-list')


def access_survey(survey_name):
    surveys_list = get_surveys_list()

    for survey in surveys_list.find_by_tag('li'):
        if survey.find_by_id('SURVEY_NAME') and survey_name in survey.find_by_id('SURVEY_NAME').text:
            survey.find_by_tag('button').click()
            break


def select_to_create_message():
    wait_for_element_by_id('create-message-link-1', timeout=3, retry=1)
    browser.find_by_id('create-message-link-1').click()
