from acceptance_tests import browser
from config import Config


def go_to():
    browser.visit(Config.RESPONSE_OPERATIONS_UI)


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
