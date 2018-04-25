from acceptance_tests import browser


def confirm_change_enrolment_status():
    browser.find_by_id('confirm-btn').click()
