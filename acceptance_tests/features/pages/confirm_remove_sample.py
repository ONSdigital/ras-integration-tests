from acceptance_tests import browser


def click_remove_sample():
    browser.find_by_id('remove-sample-btn').click()


def click_cancel():
    browser.find_by_id('cancel-btn').click()
