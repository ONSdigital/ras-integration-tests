from acceptance_tests import browser
from config import Config


def go_to():
    browser.visit(f"{Config.RESPONSE_OPERATIONS_UI}/surveys")


def go_to_create():
    browser.visit(f"{Config.RESPONSE_OPERATIONS_UI}/surveys/create")


def get_page_title():
    return browser.title


def get_surveys():
    surveys = []
    table = browser.find_by_id('tbl-surveys').first
    rows = table.find_by_tag('tbody').find_by_tag('tr')
    for row in rows:
        surveys.append({
            'id': row.find_by_name('tbl-surveys-id').value,
            'name': row.find_by_name('tbl-surveys-title').value,
            'short_name': row.find_by_name('tbl-surveys-abbreviation').value,
            'legal_basis': row.find_by_name('tbl-surveys-legal-basis').value,
        })
    return surveys


def click_survey_link(context):
    link = browser.find_by_name(f'survey-link-{context.short_name}')
    link.click()


def click_edit_survey_details_button():
    browser.click_link_by_id('edit-survey-details-199')


# todo to support site_navigation rollback to sequential changes - delete and use click_survey_link(context) when fixed
def click_qbs_survey_link():
    link = browser.find_by_name('survey-link-QBS')
    link.click()
