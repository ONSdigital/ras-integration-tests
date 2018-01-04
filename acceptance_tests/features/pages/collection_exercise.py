from acceptance_tests import browser
from config import Config


def go_to(survey, period):
    browser.visit(f'{Config.RESPONSE_OPERATIONS_UI}/surveys/{survey}/{period}')


def get_survey_info():
    survey_info = browser.find_by_name('survey-info')
    return survey_info.value


def get_period():
    period = browser.find_by_name('period')
    return period.value


def get_user_description():
    user_description = browser.find_by_name('user-description')
    return user_description.value
