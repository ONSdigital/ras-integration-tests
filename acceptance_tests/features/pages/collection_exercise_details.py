import time
from os.path import abspath

from selenium.webdriver.support.ui import Select

from acceptance_tests import browser
from acceptance_tests.features.pages import collection_exercise
from common.browser_utilities import is_text_present_with_retry, is_text_present_with_action, \
    wait_for_url_matches, wait_for_element_by_name, wait_for_element_by_id, wait_for_url_path_or_query_changed
from config import Config


def go_to(survey, period):
    target_url = f'{Config.RESPONSE_OPERATIONS_UI}/surveys/{survey}/{period}'
    browser.visit(target_url)
    wait_for_url_matches(target_url, timeout=10, retry=1, post_change_delay=0.25)


def get_page_title():
    return browser.title


def get_collection_exercise_details():
    ce_details = {
        "survey_info": browser.find_by_name('survey-info').value,
        "survey_title": browser.find_by_name('survey-title').value,
        "period": browser.find_by_name('period').value,
        "user_description": browser.find_by_name('user-description').value
    }
    return ce_details


def select_sample(sample_file_path):
    browser.driver.find_element_by_id('sampleFile').send_keys(abspath(sample_file_path))


def load_sample(sample_file_path):
    select_sample(sample_file_path)
    browser.is_element_visible_by_css('#btn-load-sample', 3)
    browser.find_by_id('btn-load-sample').click()


def get_sample_success_text():
    if is_text_present_with_action('Sample loaded', click_refresh_link_for_sample_upload, retries=3, delay=3):
        return browser.find_by_id('sample-success').first.text


def has_sample_preview():
    element_ids = ['sample-preview-businesses', 'sample-preview-ci', 'sample-preview']
    elements = [browser.driver.find_elements_by_id(element_id) for element_id in element_ids]
    return all(elements)


def cancel_sample_preview():
    browser.find_by_id('btn-cancel-load-sample').click()


def get_loaded_sample():
    if is_text_present_with_retry('Total businesses'):
        tds = browser.find_by_id('sample-table').find_by_tag('tbody').find_by_tag('td')
        return list(map(lambda td: td.value, tds))


def get_success_panel_text():
    wait_for_element_by_id("success-panel", timeout=10, retry=0.25)
    return browser.driver.find_element_by_id("success-panel").text


def get_collection_exercise_events():
    ce_events = {
        "mps": browser.find_by_name('mps-date').value,
        "go_live": browser.find_by_name('go-live-date').value,
        "return_by": browser.find_by_name('return-by-date').value,
        "reminder": browser.find_by_name('first-reminder-date').value,
        "exercise_end": browser.find_by_name('exercise-end-date').value,
        "ref_period_start": browser.find_by_name('period-start-date').value,
        "ref_period_end": browser.find_by_name('period-end-date').value,
        "employment": browser.find_by_name('employment-date').value,
        "first_reminder": browser.find_by_name('first-reminder-date').value,
        "second_reminder": browser.find_by_name('second-reminder-date').value,
        "third_reminder": browser.find_by_name('third-reminder-date').value,
    }
    return ce_events


def load_collection_instrument(test_file):
    browser.driver.find_element_by_id('ciFile').send_keys(abspath(test_file))
    browser.find_by_id('btn-load-ci').click()


def upload_collection_instrument(test_file):
    browser.driver.find_element_by_id('selected-file').send_keys(abspath(test_file))


def select_wrong_file_type(test_file):
    browser.driver.find_element_by_id('ciFile').send_keys(abspath(test_file))


def add_eq_ci():
    wait_for_element_by_name('checkbox-answer', timeout=2, retry=1)
    browser.find_by_name('checkbox-answer').first.check()
    wait_for_element_by_id('btn-add-ci', timeout=2)
    browser.find_by_id('btn-add-ci').click()


def get_collection_instrument_error_text():
    return browser.driver.find_element_by_id('ciFileErrorText').text


def get_collection_instrument_added_success_text():
    return browser.find_by_id('collection-instrument-added-success').text


def get_sample_removed_success_text():
    return browser.find_by_id('success-panel').text


def get_collection_instruments():
    tds = browser.find_by_id('collection-instruments-table').find_by_tag('tbody').find_by_tag('td')
    return list(map(lambda td: td.value, tds))


def get_error_header():
    return browser.find_by_id('error-header').text


def get_status():
    wait_for_element_by_id('ce_status', timeout=3, retry=1)
    return browser.find_by_id('ce_status').text


def ready_for_live_button_exists():
    return browser.find_by_id('btn-ready-for-live')


def click_ready_for_live():
    browser.find_by_id('btn-ready-for-live').click()


def click_ready_for_live_and_confirm():
    initial_url = browser.url
    browser.find_by_id('btn-ready-for-live').click()
    browser.get_alert().accept()
    wait_for_url_path_or_query_changed(initial_url, timeout=10, retry=1)


def get_execution_success():
    return browser.find_by_id('execution-success').text


def get_confirmation_alert():
    return browser.get_alert()


def get_processing_info():
    return browser.find_by_id('processing-info').text


def click_refresh_link():
    """"This used to be : browser.click_link_by_id('a-processing-refresh')
    However we had the situation on some macs that the collex was set too live faster than expected
    so the 'a-processing-refresh' was not displayed. Since the href in this link issues a refresh anyway
    by being set to an empty string , its safer to show
    """

    browser.reload()


def click_refresh_link_until_ready_for_live():
    click_refresh_link()

    for i in range(60):
        ce_state = get_status()
        if collection_exercise.is_ready_for_live(ce_state):
            break
        time.sleep(1)
        click_refresh_link()


def click_refresh_link_for_sample_upload():
    browser.find_link_by_partial_href('?show_msg=true').click()


def form_select_ci_exists():
    return browser.find_by_id('form-select-ci')


def form_load_ci_exists():
    return browser.find_by_id('form-load-ci')


def form_load_sample_exists():
    return browser.find_by_id('form-load-sample')


def check_edit_period_is_enabled():
    return browser.find_by_id('edit-collection-exercise-period')


def click_edit_collection_exercise_period_button():
    browser.click_link_by_id('edit-collection-exercise-period')


def click_edit_collection_exercise_user_description_button():
    browser.click_link_by_id('edit-collection-exercise-user-description')


def remove_ci():
    entry_url = browser.url
    wait_for_element_by_id('unlink-ci-1', timeout=10, retry=0.25)
    browser.click_link_by_id('unlink-ci-1')
    wait_for_url_path_or_query_changed(entry_url, timeout=10, retry=0.25, post_change_delay=1)


def get_collection_instrument_removed_success_text():
    return browser.find_by_id('collection-instrument-removed-success').text


def is_able_to_remove_ci():
    remove_options = len(browser.find_by_id('unlink-ci-1'))

    return True if remove_options > 0 else None


def remove_sample():
    browser.click_link_by_id('remove_sample_btn_1')


def check_remove_sample():
    browser.find_by_id('remove_sample_btn_1')


def get_remove_sample():
    return browser.find_by_id('remove_sample_btn').text


def get_check_sample_contents():
    return browser.find_by_id('btn-check-sample-contents').text


def select_add_mps_date():
    browser.find_by_id("create-event-date-mps").click()


def add_ce_event_date(day, month, year):
    browser.driver.find_element_by_id("day").send_keys(day)
    select = Select(browser.driver.find_element_by_id("month"))
    select.select_by_visible_text(month)
    browser.driver.find_element_by_id("year").send_keys(year)


def confirm_ce_event_date():
    browser.find_by_id("submit").click()
