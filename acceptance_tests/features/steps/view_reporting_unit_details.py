import time
from logging import getLogger

from behave import given, when, then
from structlog import wrap_logger

from acceptance_tests import browser
from acceptance_tests.features.pages import edit_respondent_details_form, reporting_unit
from acceptance_tests.features.steps.authentication import signed_in_internal
from config import Config
from controllers.party_controller import get_party_by_ru_ref, get_respondent_details

logger = wrap_logger(getLogger(__name__))


@given('the reporting unit 49900000001 is in the system')
def reporting_unit_49900000001_is_in_the_system(_):
    pass


@given('the respondent "first_name" is enrolled')
def respondent_first_name_is_enrolled(_):
    business = get_party_by_ru_ref('49900000001')
    respondent_id = business['associations'][0]['partyId']
    respondent = get_respondent_details(respondent_id)
    if respondent['firstName'] != 'first_name' \
            or respondent['lastName'] != 'last_name' \
            or respondent['telephone'] != "0987654321":
        reporting_unit.go_to('49900000001')
        reporting_unit.click_data_panel('Bricks')
        reporting_unit.click_edit_details('Bricks', Config.RESPONDENT_USERNAME)
        edit_respondent_details_form.edit_first_name('first_name')
        edit_respondent_details_form.edit_last_name('last_name')
        edit_respondent_details_form.edit_contact_number('0987654321')
        edit_respondent_details_form.click_save()


@given('the internal user is on the reporting unit page for 49900000003')
def internal_user_is_on_reporting_unit_page(_):
    signed_in_internal(_)
    reporting_unit.go_to('49900000003')


@when('the internal user views the 49900000001 reporting unit page')
def internal_user_views_the_reporting_unit_page(_):
    reporting_unit.go_to('49900000001')


@when('the internal user opens the Bricks data panel')
def internal_user_views_the_survey_page(_):
    reporting_unit.click_data_panel('Bricks')


@then('the internal user is displayed the correct reporting unit details')
def internal_user_views_correct_reporting_unit_details(_):
    ru_details = reporting_unit.get_ru_details()
    assert ru_details['ru_ref'] == '49900000001'
    assert ru_details['name'] == 'RUNAME1_COMPANY1 RUNNAME2_COMPANY1'


@then('the internal user is presented with the associated surveys')
def internal_internal_user_presented_correct_associated_surveys(_):
    associated_surveys = reporting_unit.get_associated_surveys()
    assert len(associated_surveys) == 2
    assert '074 Bricks' in associated_surveys
    assert '139 QBS' in associated_surveys


@then('the internal user is presented with the associated collection exercises')
def internal_internal_user_presented_correct_associated_collection_exercises(_):
    associated_ces = reporting_unit.get_associated_collection_exercises()
    # Status updated async so wait until updated
    for i in range(5):
        if 'Not started' in associated_ces[0]['status']:
            break
        browser.reload()
        associated_ces = reporting_unit.get_associated_collection_exercises()
        time.sleep(1)
    exercise_201801 = reporting_unit.get_collection_exercise('201801', associated_ces)
    assert exercise_201801['exercise_ref'] == '201801'
    assert exercise_201801['company_name'] == 'RUNAME1_COMPANY1 RUNNAME2_COMPANY1'
    assert exercise_201801['company_region'] == 'GB'
    assert 'Not started' in exercise_201801['status'], exercise_201801['status']


@then('the internal user is presented with the associated respondents')
def internal_internal_user_presented_correct_associated_respondents(_):
    # Status updated async so wait until updated
    respondent = reporting_unit.get_respondent('example@example.com')
    assert respondent['enrolmentStatus'] == 'Enabled'
    assert respondent['name'] == 'first_name last_name'
    assert respondent['email'] == 'example@example.com'
    assert respondent['phone'] == '0987654321'
    assert respondent['accountStatus'] == 'Active'


@then('the status \'Completed by phone\' is displayed back to the internal user')
def status_is_displayed_back_the_internal_user(_):
    associated_ces = reporting_unit.get_associated_collection_exercises()
    assert 'Completed by phone' in associated_ces[0]['status']
