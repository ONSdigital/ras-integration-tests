from acceptance_tests import browser
from config import Config


def go_to(ru_ref):
    browser.visit(f"{Config.RESPONSE_OPERATIONS_UI}/reporting-units/{ru_ref}")


def click_data_panel(survey_short_name):
    browser.find_by_id(f'survey-{survey_short_name}').click()


def get_ru_details():
    ru_details = {
        "name": browser.find_by_id('RU_NAME').text,
        "ru_ref": browser.find_by_id('RU_REF').text
    }
    return ru_details


def get_associated_surveys():
    survey_titles = browser.find_by_name('survey-titles')
    surveys = [title.value for title in survey_titles]
    return surveys


def get_associated_collection_exercises():
    exercises = []
    ce_tables = browser.find_by_name('tbl-ce-for-survey')

    for table in ce_tables:
        rows = table.find_by_tag('tbody').find_by_tag('tr')
        for row in rows:
            exercises.append({
                "exercise_ref": row.find_by_name('tbl-ce-period').value,
                "company_name": row.find_by_name('tbl-ce-company-name').value,
                "company_region": row.find_by_name('tbl-ce-company-region').value,
                "status": row.find_by_name('tbl-ce-status').value
            })
    return exercises


def get_associated_respondents():
    respondents = []
    respondents_tables = browser.find_by_name('tbl-respondents-for-survey')

    for table in respondents_tables:
        rows = table.find_by_tag('tbody').find_by_tag('tr')
        for row in rows:
            details = row.find_by_name('tbl-respondent-details').first
            respondents.append({
                "enrolementStatus": row.find_by_name('tbl-enrolment-status').value,
                "name": details.find_by_name('tbl-respondent-name').value,
                "email": details.find_by_name('tbl-respondent-email').value,
                "phone": details.find_by_name('tbl-respondent-phone').value,
                "accountStatus": details.find_by_name('tbl-respondent-status').value
            })
    return respondents


def get_unused_iac(ru_ref, survey_short_name):
    go_to(ru_ref)
    click_data_panel(survey_short_name)
    return browser.find_by_id(f'unused-enrolment-code-{survey_short_name}').value


def click_generate_new_code():
    browser.find_by_id('generate-new-code').click()
