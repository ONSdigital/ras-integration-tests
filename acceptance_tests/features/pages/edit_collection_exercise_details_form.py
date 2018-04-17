from acceptance_tests import browser


def edit_period(period):
    browser.find_by_id('period').fill(period)


def edit_user_description(user_description):
    browser.find_by_id('user_description').fill(user_description)


def click_save():
    browser.find_by_id('save-btn').click()


def click_cancel():
    browser.find_by_id('cancel-btn').click()
