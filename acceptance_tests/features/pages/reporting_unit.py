from acceptance_tests import browser
from acceptance_tests.features.pages import scroll_to
from config import Config


def go_to(ru_ref):
    browser.visit(f"{Config.RESPONSE_OPERATIONS_UI}/reporting-units/{ru_ref}")


def click_data_panel(short_name):
    browser.find_by_id(f'survey-{short_name}').click()


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


def get_associated_collection_exercises(survey_short_name):
    ce_table = browser.find_by_id(f'survey-{survey_short_name}').find_by_name('tbl-ce-for-survey')
    ce_rows = ce_table.find_by_tag('tbody').find_by_tag('tr')
    exercises = [{
        "exercise_ref": row.find_by_name('tbl-ce-period').value,
        "company_name": row.find_by_name('tbl-ce-company-name').value,
        "company_region": row.find_by_name('tbl-ce-company-region').value,
        "status": row.find_by_name('tbl-ce-status').value,
        "status_change_link": row.find_by_name('tbl-ce-status').find_by_tag("a")
    } for row in ce_rows]
    return exercises


def get_collection_exercise(exercise_ref, survey_short_name):
    return next((exercise for exercise in get_associated_collection_exercises(survey_short_name)
                 if exercise['exercise_ref'] == exercise_ref), None)


def create_respondent_dict(respondent):
    respondent_details = {
        "enrolmentStatus": respondent.find_by_id('enrolment-status').value,
        "name": respondent.find_by_name('tbl-respondent-details').first.find_by_name('tbl-respondent-name').value,
        "email": respondent.find_by_name('tbl-respondent-details').first.find_by_name('tbl-respondent-email').value,
        "phone": respondent.find_by_name('tbl-respondent-details').first.find_by_name('tbl-respondent-phone').value,
        "accountStatus": respondent.find_by_name('tbl-respondent-status').value
    }
    pending_email = respondent.find_by_name('tbl-respondent-pending-email')
    if len(pending_email) > 0:
        return {**respondent_details, "pending_email": pending_email.value}
    return respondent_details


def get_associated_respondents(survey_short_name):
    respondents_table = browser.find_by_id(f'survey-{survey_short_name}').find_by_name('tbl-respondents-for-survey')
    respondent_rows = respondents_table.find_by_tag('tbody').find_by_tag('tr')
    respondents = [create_respondent_dict(respondent) for respondent in respondent_rows]
    return respondents


def get_respondent(survey_short_name, email):
    return next((respondent for respondent in get_associated_respondents(survey_short_name)
                 if respondent['email'] == email), None)


def click_change_response_status_link(survey, period):
    collection_exercise = get_collection_exercise(period, survey)
    collection_exercise['status_change_link'].click()


def get_unused_iac(ru_ref, survey_short_name):
    go_to(ru_ref)
    click_data_panel(survey_short_name)
    unused_iac_element = browser.find_by_id(f'unused-enrolment-code-{survey_short_name}')
    unused_iac = unused_iac_element.value if unused_iac_element else None
    return unused_iac


def click_generate_new_code(code):
    browser.find_by_id('generate-new-code-' + code).click()


def click_disable_enrolment(email):
    respondents_table = browser.find_by_name('tbl-respondents-for-survey')
    rows = respondents_table.find_by_tag('tbody').find_by_tag('tr')
    for row in rows:
        details = row.find_by_name('tbl-respondent-details').first
        if details.find_by_name('tbl-respondent-email').value == email:
            change_enrolment_link = row.find_by_id('change-enrolment-status')
            scroll_to(change_enrolment_link).click()
            break


def click_edit_details(survey_short_name, email):
    respondents_table = browser.find_by_name('tbl-respondents-for-survey')
    rows = respondents_table.find_by_tag('tbody').find_by_tag('tr')
    for row in rows:
        details = row.find_by_name('tbl-respondent-details').first
        if details.find_by_name('tbl-respondent-email').value == email:
            details.find_by_id(f'edit-contact-details-btn-{survey_short_name}').click()
            break


def get_confirm_contact_details_success_text():
    return browser.find_by_id('success').text


def save_email_error():
    return browser.find_by_id('save-email-error')
