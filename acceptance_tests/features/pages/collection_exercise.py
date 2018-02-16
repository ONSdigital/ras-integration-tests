from acceptance_tests import browser
from config import Config


def go_to(survey):
    browser.visit(f'{Config.RESPONSE_OPERATIONS_UI}/surveys/{survey}')


def get_page_title():
    return browser.title


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
            "exercise_ref": row.find_by_name('tbl-ce-period').value,
            "user_description": row.find_by_name('tbl-ce-shown-as').value,
            "state": row.find_by_name('tbl-ce-status').value
        })
    return exercises


def get_table_headers():
    table = browser.find_by_id('tbl-collection-exercise').first
    return table.find_by_tag('thead').value


def click_qbs_1803_ce_link():
    link = browser.find_by_name('ce-link-1803')
    link.click()
