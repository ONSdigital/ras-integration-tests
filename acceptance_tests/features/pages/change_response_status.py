from acceptance_tests import browser


def update_response_status(status_event):
    browser.find_by_value(status_event).click()
    browser.find_by_id('response-status-change-confirm-button').click()
