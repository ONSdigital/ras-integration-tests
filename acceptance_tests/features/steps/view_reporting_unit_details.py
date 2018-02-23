import time
from logging import getLogger

from behave import given, when, then
from structlog import wrap_logger

from acceptance_tests import browser
from acceptance_tests.features.pages import reporting_unit

logger = wrap_logger(getLogger(__name__))


@given('the reporting unit 49900000001 is in the system')
def reporting_unit_49900000001_is_in_the_system(_):
    pass


@when('the internal user views the 49900000001 reporting unit page')
def internal_user_views_the_survey_page(_):
    reporting_unit.go_to('49900000001')


@then('the internal user is displayed the correct reporting unit details')
def internal_user_views_correct_reporting_unit_details(_):
    ru_details = reporting_unit.get_ru_details()
    assert ru_details['ru_ref'] == '49900000001'
    assert ru_details['name'] == 'RUNAME1_COMPANY1 RUNNAME2_COMPANY1'


@then('the internal user is presented with the associated surveys')
def internal_internal_user_presented_correct_associated_surveys(_):
    associated_surveys = reporting_unit.get_associated_surveys()
    assert len(associated_surveys) == 1
    assert '074 Bricks' in associated_surveys


@then('the internal user is presented with the associated collection exercises')
def internal_internal_user_presented_correct_associated_collection_exercises(_):
    associated_ces = reporting_unit.get_associated_collection_exercises()
    # Status updated async so wait until updated
    for i in range(5):
        if associated_ces[0]['status'] == 'Not started':
            break
        browser.reload()
        associated_ces = reporting_unit.get_associated_collection_exercises()
        time.sleep(1)
    assert len(associated_ces) == 1
    assert associated_ces[0]['exercise_ref'] == '201801'
    assert associated_ces[0]['company_name'] == 'RUNAME1_COMPANY1 RUNNAME2_COMPANY1'
    assert associated_ces[0]['company_region'] == 'GB'
    assert associated_ces[0]['status'] == 'Not started', associated_ces[0]['status']


@then('the internal user is presented with the associated respondents')
def internal_internal_user_presented_correct_associated_respondents(_):
    associated_respondents = reporting_unit.get_associated_respondents()
    # Status updated async so wait until updated
    for i in range(5):
        if associated_respondents[0]['accountStatus'] == 'Created':
            break
        browser.reload()
        associated_respondents = reporting_unit.get_associated_respondents()
        time.sleep(1)
    assert len(associated_respondents) == 1
    assert associated_respondents[0]['enrolementStatus'] == 'Enabled'
    assert associated_respondents[0]['name'] == 'first_name last_name'
    assert associated_respondents[0]['email'] == 'example@example.com'
    assert associated_respondents[0]['phone'] == '0987654321'
    assert associated_respondents[0]['accountStatus'] == 'Created'
