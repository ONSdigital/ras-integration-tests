
from behave import when, then

from acceptance_tests import browser
from acceptance_tests.features.pages import reporting_unit


@then('the "{survey}" "{period}" collection exercise for ru "{ru_ref}" displays a view link')
def assert_view_response_status_link(_, survey, period, ru_ref):
    reporting_unit.go_to(ru_ref)
    reporting_unit.click_data_panel(survey)
    response_table = browser.find_by_name('tbl-ce-for-survey')
    rows = response_table.find_by_tag('tbody').find_by_tag('tr')
    for row in rows:
        if period in row.text:
            assert browser.is_text_present('Completed by phone View')


@when('the internal user click view the response status for the survey with correct period')
def internal_user_click_view_response_status(_):
    browser.click_link_by_text('View')


@then('the internal user can view the timestamp for the completed state')
def assert_date_and_timestamp_for_completed_stated(_):
    assert browser.is_element_present_by_id('date-and-time')


@then('the only action available is the close link')
def assert_close_link_in_response_status(_):
    assert browser.is_text_present('Close')
