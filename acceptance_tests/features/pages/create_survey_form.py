from acceptance_tests import browser


def edit_survey_ref(survey_ref):
    browser.find_by_id('survey_ref').fill(survey_ref)


def edit_short_name(short_name):
    browser.find_by_id('short_name').fill(short_name)


def edit_long_name(long_name):
    browser.find_by_id('long_name').fill(long_name)


def edit_legal_basis(legal_basis):
    browser.find_by_id('legal_basis').select_by_text(legal_basis)


def click_save():
    browser.find_by_id('save-btn').click()


def click_cancel():
    browser.find_by_id('cancel-btn').click()


def save_error():
    return browser.find_by_id('save-error').first.text
