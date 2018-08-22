from logging import getLogger

from behave import given, when, then
from structlog import wrap_logger

from acceptance_tests import browser
from acceptance_tests.features.pages import enrolment_code, reporting_unit
from acceptance_tests.features.pages import home
from common.enrolment_helper import generate_new_iac_code


logger = wrap_logger(getLogger(__name__))


@given("the respondent is ready to enrol in a survey")
def ready_to_enrol_in_survey(context):
    home.go_to_external_home()
    browser.find_by_id('create-account').click()


@given("a respondent has got their enrolment code")
def generate_enrolment_code(context):
    context.iac = generate_new_iac_code(context)


@when('they enter their enrolment code')
def enter_enrolment_code(context):
    browser.driver.find_element_by_id('enrolment_code').send_keys(context.iac)
    browser.find_by_id('continue_button').click()


@then('they confirm the survey and organisation details')
@given('they confirm the survey and organisation details')
def confirm_correct_survey_selected(context):
    actual_iac = browser.find_by_id('enrolment_code').value
    actual_survey_name = browser.find_by_id('survey_name').value

    assert context.iac == actual_iac
    assert context.survey_name == actual_survey_name

    browser.find_by_id('confirm_button').click()


@given("a respondent has entered their enrolment code")
def respondent_enters_enrolment_code(context):
    generate_enrolment_code(context)
    enter_enrolment_code(context)


@when('they enter their account details')
def complete_account_details(context):
    context.email = context.test_unique_id + '@somewhere.com'

    browser.driver.find_element_by_id('first_name').send_keys('FirstName')
    browser.driver.find_element_by_id('last_name').send_keys('LastName')
    browser.driver.find_element_by_id('email_address').send_keys(context.email)
    browser.driver.find_element_by_id('password').send_keys('A234567_')
    browser.driver.find_element_by_id('password_confirm').send_keys('A234567_')
    browser.driver.find_element_by_id('phone_number').send_keys('01172345678')

    browser.find_by_id('continue_button').click()


@then('they are sent a verification email')
def confirm_verification_email(context):
    actual_email_confirmation = browser.find_by_id('email_confirmation_sent').value

    assert context.email in actual_email_confirmation


@given('the internal user views the 49900000001 reporting unit page')
def internal_user_views_the_reporting_unit(_):
    reporting_unit.go_to('49900000001')


@when('the user clicks generate enrolment code')
def internal_user_generates_new_code(_):
    reporting_unit.click_generate_new_code()


@then('a new enrolment code is displayed back to the user')
def internal_user_views_generated_code(_):
    iac = enrolment_code.get_iac()
    assert iac
