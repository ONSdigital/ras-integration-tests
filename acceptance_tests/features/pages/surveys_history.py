from acceptance_tests import browser


def go_to_history_tab():
    browser.find_by_id('SURVEY_HISTORY_TAB').click()


def get_status_text():
    return browser.find_by_id('status-1').text
