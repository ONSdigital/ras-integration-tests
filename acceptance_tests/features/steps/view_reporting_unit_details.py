import time
from logging import getLogger

from behave import given, when, then
from structlog import wrap_logger

from acceptance_tests import browser
from acceptance_tests.features.pages import edit_respondent_details_form, reporting_unit
from controllers.party_controller import get_party_by_ru_ref, get_respondent_details

logger = wrap_logger(getLogger(__name__))


@given('a reporting unit is in the system')
def reporting_unit_is_in_the_system(_):
    pass


@given('the respondent "first_name" is enrolled')
def respondent_first_name_is_enrolled(context):
    business = get_party_by_ru_ref(context.short_name)
    respondent_id = business['associations'][0]['partyId']
    respondent = get_respondent_details(respondent_id)
    if respondent['firstName'] != 'first_name' \
            or respondent['lastName'] != 'last_name' \
            or respondent['telephone'] != context.phone_number:
        reporting_unit.go_to(context.short_name)
        reporting_unit.click_data_panel(context.short_name)
        reporting_unit.click_edit_details(context.short_name, context.respondent_email)
        edit_respondent_details_form.edit_first_name('first_name')
        edit_respondent_details_form.edit_last_name('last_name')
        edit_respondent_details_form.edit_contact_number(context.phone_number)
        edit_respondent_details_form.click_save()


@when('the internal user views the reporting unit page')
def internal_user_views_the_reporting_unit_page(context):
    reporting_unit.go_to(context.short_name)


@when('the internal user opens the data panel')
def internal_user_views_the_survey_page(context):
    reporting_unit.click_data_panel(context.short_name)


@then('the internal user is displayed the correct reporting unit details')
def internal_user_views_correct_reporting_unit_details(context):
    ru_details = reporting_unit.get_ru_details()
    assert ru_details['ru_ref'] == context.short_name
    assert ru_details['name'] == 'RED BRICKS LTD'


@then('the internal user is presented with the associated surveys')
def internal_internal_user_presented_correct_associated_surveys(context):
    associated_surveys = reporting_unit.get_associated_surveys()
    assert f'{context.survey_ref} {context.short_name}' in associated_surveys


@then('the internal user is presented with the associated collection exercises')
def internal_internal_user_presented_correct_associated_collection_exercises(context):
    associated_ces = reporting_unit.get_associated_collection_exercises(context.short_name)
    # Status updated async so wait until updated
    for _ in range(5):
        if 'Not started' in associated_ces[0]['status']:
            break
        browser.reload()
        associated_ces = reporting_unit.get_associated_collection_exercises('Bricks')
        time.sleep(1)
    exercise = reporting_unit.get_collection_exercise(context.period, context.short_name)
    assert exercise['exercise_ref'] == context.period
    assert exercise['company_name'] == 'RED BRICKS LTD'
    assert exercise['company_region'] == 'GB'
    assert 'Not started' in exercise['status'], exercise['status']


@then('the internal user is presented with the associated respondents')
def internal_internal_user_presented_correct_associated_respondents(context):
    # Status updated async so wait until updated
    respondent = reporting_unit.get_respondent(context.short_name, context.respondent_email)
    assert respondent['enrolmentStatus'] == 'Enabled'
    assert respondent['name'] == 'first_name last_name'
    assert respondent['email'] == context.respondent_email
    assert respondent['phone'] == context.phone_number
    assert respondent['accountStatus'] == 'Active'


@then('the "trading as" name should be displayed on the RU details')
def trading_as_name_is_displayed(context):
    assert context.short_name in browser.driver.find_element_by_id('RU_DETAILS').text, \
        f'Could not find trading as name "{context.short_name}" in respondent details page'


@then('the "trading as" name should not appear on the RU details')
def trading_as_name_does_not_appear(context):
    assert 'Trading as:' not in browser.driver.find_element_by_id('RU_DETAILS').text,\
        '"Trading as" is displayed when the business has no trading name'
