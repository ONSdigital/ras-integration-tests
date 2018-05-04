from acceptance_tests import browser


def edit_period(period):
    browser.find_by_id('period').fill(period)


def check_period_length():
    return browser.find_by_id('period').value


def edit_user_description(user_description):
    browser.find_by_id('user_description').fill(user_description)


def click_save():
    browser.find_by_id('save-btn').click()


def click_cancel():
    browser.find_by_id('cancel-btn').click()


def period_error_panel():
    return browser.find_by_id('error-creating-ce-message').text
