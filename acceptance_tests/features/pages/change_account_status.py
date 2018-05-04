from acceptance_tests import browser


def confirm_change_account_status():
    browser.find_by_id('confirm-btn').click()


def find_enrolment(ru_ref, survey_short_name):
    enrolment_list = browser.find_by_id("editor-account-enrolments")
    enrolments = enrolment_list.find_elements_by_tag_name("li")
    for enrolment in enrolments:
        if ru_ref in enrolment and survey_short_name in enrolment:
            return enrolment
    return "Enrolment not found"
