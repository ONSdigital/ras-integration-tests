from acceptance_tests import browser
from config import Config


def go_to(survey, period):
    browser.visit('{}/surveys/{}/{}'.format(Config.RESPONSE_OPERATIONS_UI, survey, period))


def get_collection_exercise_details():
    ce_details = {
        "survey_info": browser.find_by_name('survey-info').value,
        "period": browser.find_by_name('period').value,
        "user_description": browser.find_by_name('user-description').value
    }
    return ce_details
