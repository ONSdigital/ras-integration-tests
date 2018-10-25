from behave import when, given, then

from acceptance_tests import browser
from acceptance_tests.features.pages import reporting_unit

RESPONSE_STATUS = browser.find_by_name('tbl-ce-status')


@then('the "{survey}" "{period}" collection exercise for ru "{ru_ref}" displays a view link')
def assert_view_response_status_link(_, survey, period, ru_ref):
    reporting_unit.go_to(ru_ref)
    reporting_unit.click_data_panel('Bricks')
    view_link = '<a href="/case/49900000001/response-status?survey=Bricks&amp;period=202001">View</a>'
    assert view_link in RESPONSE_STATUS


@when('the internal user click view the response status for "{survey}" "{period}"')
def internal_user_click_view_response_status(_, survey, period):
    view_link = '/case/49900000001/response-status?survey=Bricks&amp;period=202001'
    browser.click_link_by_href(view_link)


@then('the internal user can view the timestamp for the completed state')
def assert_date_and_timestamp_for_completed_stated(_):
    date_and_time_stamp = browser.find_by_id('date-and-time')
    assert date_and_time_stamp in RESPONSE_STATUS


@then('the only action available is the close link')
def assert_close_link_in_response_status(_):
    close_link = '<a href="http://localhost:8085/reporting-units/49900000001?survey=Bricks&amp;period=202001" ' \
                 'onclick="history.back(); return false;" class="u-d-b u-mt-s">Close</a>'
    assert close_link in RESPONSE_STATUS
