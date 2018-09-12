from acceptance_tests import browser


def click_first_new_response_status_option():
    event = browser.driver.find_element_by_id('status-group-1-status-1')
    print(event)
    event.click()
    return event


def click_set_new_status():
    browser.driver.find_element_by_id('response-status-change-confirm-button').click()
