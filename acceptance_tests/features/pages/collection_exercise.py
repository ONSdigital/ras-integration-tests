from acceptance_tests import browser
from config import Config


def go_to(survey):
    browser.visit(Config.RESPONSE_OPERATIONS_UI_COLLECTION_EXERCISE.format(survey))


def get_survey_attributes():
    survey_data = browser.find_by_id('survey-attributes').first
    survey_attributes = {
        'survey_id': survey_data.find_by_name('survey-id').value,
        'survey_title': survey_data.find_by_name('survey-title').value,
        'survey_abbreviation': survey_data.find_by_name('survey-abbreviation').value,
        'survey_legal_basis': survey_data.find_by_name('survey-legal-basis').value,
    }
    return survey_attributes
