from acceptance_tests import browser
from config import Config


def go_to():
    browser.visit(Config.FRONTSTAGE_SERVICE + '/surveys/todo')


def get_collection_exercise_periods():
    return browser.find_by_name('period')


def get_surveys_list():
    return browser.find_by_id('survey-list')


def access_survey(survey_name):
    surveys_list = get_surveys_list()

    for survey in surveys_list.find_by_tag('li'):
        if survey.find_by_id('SURVEY_NAME') and survey_name in survey.find_by_id('SURVEY_NAME').text:
            survey.find_by_tag('button').click()
            break


def select_to_create_message():
    browser.find_by_id('create-message-link-1').click()
