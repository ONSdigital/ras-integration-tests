from acceptance_tests import browser


def edit_short_name(short_name):
    browser.find_by_id('short_name').fill(short_name)


def edit_long_name(long_name):
    browser.find_by_id('long_name').fill(long_name)


def click_save():
    browser.find_by_id('save-btn').click()


def click_cancel():
    browser.find_by_id('cancel-btn').click()
