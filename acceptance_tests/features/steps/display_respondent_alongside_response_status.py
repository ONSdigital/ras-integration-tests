import logging

from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from splinter.exceptions import ElementDoesNotExist
from structlog import wrap_logger

from acceptance_tests import browser
from acceptance_tests.features.pages import reporting_unit, collection_exercise_details, \
    change_response_status, surveys_todo
from acceptance_tests.features.pages.surveys_history import go_to_history_tab
from acceptance_tests.features.steps.authentication import signed_in_internal, signed_in_respondent
from acceptance_tests.features.steps.change_response_status import go_to_reporting_unit_page
from controllers.collection_exercise_controller import map_ce_status

logger = wrap_logger(logging.getLogger(__name__))


@given('a user has completed a survey online')
def enrolling_onto_survey(context):
    signed_in_respondent(context)
    browser.click_link_by_id('access_survey_button_1')
    collection_exercise_details.upload_collection_instrument(
        test_file='resources/collection_instrument_files/064_201803_0001.xlsx')
    browser.find_by_id('upload_survey_button').click()


@given('an external user is enrolled onto a given survey')
def enrolled_respondent_but_not_completed(context):
    signed_in_respondent(context)


@given('a user has completed a survey via the telephone')
def user_completes_survey_by_telephone(context):
    signed_in_internal(context)
    go_to_reporting_unit_page(context)
    reporting_unit.click_data_panel(context.short_name)
    reporting_unit.click_change_response_status_link(survey=context.short_name, period=context.period)
    mapped_status = map_ce_status('Completed by phone')
    change_response_status.update_response_status(mapped_status)


@given('the status is set to "{status}"')
def survey_set_to_longer_required(context, status):
    signed_in_respondent(context)
    go_to_history_tab()
    assert browser.find_by_text(status)


@given('the status is set to In Progress')
def survey_set_to_in_progress(_):
    surveys_todo.go_to()
    status = WebDriverWait(browser, timeout=60, poll_frequency=5, ignored_exceptions=ElementDoesNotExist). \
        until(wait_for_text_on_screen)
    assert status[0].text == 'Downloaded'


def wait_for_text_on_screen(browser):
    browser.reload()
    elem = browser.find_by_text('Downloaded')
    if elem[0].text == 'Downloaded':
        return elem


@given('an internal user has set a given survey to "No longer required" for a given respondent')
def survey_is_set_to_no_longer_required(context):
    signed_in_internal(context)
    go_to_reporting_unit_page(context)
    reporting_unit.click_data_panel(context.short_name)
    reporting_unit.click_change_response_status_link(survey=context.short_name, period=context.period)
    mapped_status = map_ce_status('No longer required')
    change_response_status.update_response_status(mapped_status)


@given('a user has partially completed a survey (In progress)')
def respondent_partially_completes_survey(context):
    signed_in_respondent(context)
    browser.click_link_by_id('access_survey_button_1')
    browser.click_link_by_id('download_survey_button')


@given('has not initiated any changes to the "Not started" status')
def no_changes_have_been_made_to_collex(_):
    assert browser.find_by_text('Not started')


@given('the status is set to Completed')
def status_set_to_completed(_):
    surveys_todo.go_to()
    go_to_history_tab()
    assert browser.find_by_text('Complete')


@when('an internal user navigates to Reporting units for that Reference')
def navigating_to_reporting_units(context):
    signed_in_internal(context)
    go_to_reporting_unit_page(context)
    reporting_unit.click_data_panel(context.short_name)
    reporting_unit.click_change_response_status_link(survey=context.short_name, period=context.period)


@when('an internal user navigates to Reporting Units for the no longer required reference')
def collex_set_to_no_longer_required(context):
    signed_in_internal(context)
    go_to_reporting_unit_page(context)
    reporting_unit.click_data_panel(context.short_name)


@then('no longer required should be displayed in the survey collection exercise')
def no_longer_required_set_for_collex(_):
    assert 'No longer required' in browser.html


@then('no Respondent name should be displayed in the Respondent field')
def respondent_name_is_not_displayed(_):
    assert 'Respondent:' in browser.html
    assert browser.find_by_id('completed-respondent')[0].value == ''


@then('the Respondent details must be displayed in the Respondent field')
def respondent_name_is_displayed(_):
    assert 'Respondent:' in browser.html
    respondent = browser.find_by_id('completed-respondent')[0].value
    assert respondent == 'first_name last_name'
