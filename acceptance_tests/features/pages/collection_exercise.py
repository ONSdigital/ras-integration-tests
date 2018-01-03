from acceptance_tests import browser
from config import Config


def go_to(survey):
    browser.visit('{}/surveys/{}'.format(Config.RESPONSE_OPERATIONS_UI, survey))


def get_survey_attributes():
    survey_data = browser.find_by_id('survey-attributes').first
    survey_attributes = {
        'survey_id': survey_data.find_by_name('survey-id').value,
        'survey_title': survey_data.find_by_name('survey-title').value,
        'survey_abbreviation': survey_data.find_by_name('survey-abbreviation').value,
        'survey_legal_basis': survey_data.find_by_name('survey-legal-basis').value,
    }
    return survey_attributes


def get_collection_exercises():
    exercises = []
    table = browser.find_by_id('tbl-collection-exercise').first
    rows = table.find_by_tag('tbody').find_by_tag('tr')
    for row in rows:
        exercises.append({
            "exercise_ref": row.find_by_name('tbl-ce-period'),
            "user_description": row.find_by_name('tbl-ce-shown-as')
        })
    return exercises


def get_table_headers():
    table = browser.find_by_id('tbl-collection-exercise').first
    return table.find_by_tag('thead').value
