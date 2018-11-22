import logging
from pprint import pprint

import time
from behave import given, when, then
from structlog import wrap_logger

from acceptance_tests import browser
from acceptance_tests.features.pages import reporting_unit, collection_exercise_details, sign_in_respondent
from acceptance_tests.features.steps.authentication import signed_in_respondent, signed_in_internal
from acceptance_tests.features.steps.change_response_status import go_to_reporting_unit_page
from config import Config

logger = wrap_logger(logging.getLogger(__name__))


@given('an external user is enrolled onto a given survey')
def enrolling_onto_survey(context):
    enrolled_respondent_sign_in(context)
    browser.click_link_by_id('access_survey_button_1')
    collection_exercise_details.upload_collection_instrument(
        test_file='resources/collection_instrument_files/064_201803_0001.xlsx')
    browser.find_by_id('upload_survey_button').click()


def enrolled_respondent_sign_in(context):
    sign_in_respondent.go_to()
    # Only attempt to sign in if not already signed in otherwise implicitly redirected to homepage
    if '/sign-in' in browser.url:
        browser.driver.find_element_by_id('username').send_keys(context.user_name)
        browser.driver.find_element_by_id('inputPassword').send_keys(Config.RESPONDENT_PASSWORD)
        time.sleep(40)
        browser.find_by_id('sign_in_button').click()


@given('has not initiated any changes to the "Not started" status')
def no_changes_have_been_made_to_collex(_):
    pass


@given('the status is set to Completed')
def status_set_to_completed(_):
    pass


@when('an internal user navigates to Reporting units for that Reference')
def navigating_to_reporting_units(context):
    signed_in_internal(())
    go_to_reporting_unit_page(context)
    reporting_unit.click_data_panel(context.short_name)
    reporting_unit.click_change_response_status_link(survey=context.short_name, period=context.period)


@then('no Respondent name should be displayed in the Respondent field')
def respondent_name_is_not_displayed(context):
    assert 'Respondent:' in browser.html
