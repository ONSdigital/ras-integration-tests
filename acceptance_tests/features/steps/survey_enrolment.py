from behave import given, when, then

from acceptance_tests.features.pages import enrolment_code, reporting_unit
from acceptance_tests.features.pages import home
from common.feature_helper import is_display_an_unused_active_code_scenario, is_generate_new_enrolment_code_scenario, \
    is_frontstage_can_see_the_survey_they_are_enrolling_in_scenario, is_frontstage_user_can_create_an_account_scenario
from common.survey_utilities import *
from reset_database import reset_database

logger = wrap_logger(getLogger(__name__))


@given("the respondent is ready to enrol in a survey")
def ready_to_enrol_in_survey(context):
    home.go_to_external_home()
    browser.find_by_id('create-account').click()


@given("a respondent has got their enrolment code")
def generate_enrolment_code(context):
    setup_survey_enrolment_for_test(context)


@then('an unused enrolment code is displayed back to the user')
def internal_user_views_unused_code(context):
    iac = enrolment_code.get_unused_iac()
    assert iac


@when('they enter their enrolment code')
def enter_enrolment_code(context):
    browser.driver.find_element_by_id('enrolment_code').send_keys(context.enrolment_code)
    browser.find_by_id('continue_button').click()


@then('they confirm the survey and organisation details')
@given('they confirm the survey and organisation details')
def confirm_correct_survey_selected(context):
    actual_enrolment_code = browser.find_by_id('enrolment_code').value
    actual_survey_name = browser.find_by_id('survey_name').value

    assert context.enrolment_code == actual_enrolment_code
    assert context.survey_name == actual_survey_name

    browser.find_by_id('confirm_button').click()


@given("a respondent has entered their enrolment code")
def respondent_enters_enrolment_code(context):
    setup_survey_enrolment_for_test(context)
    enter_enrolment_code(context)


@when('they enter their account details')
def complete_account_details(context):
    context.email = make_respondent_user_name(str(context.unique_id), context.survey_short_name)

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


@given('the internal user views the reporting unit page for a sample unit')
def internal_user_views_the_reporting_unit(context):
    setup_survey_enrolment_for_test(context)
    reporting_unit.go_to(context.unique_id)


@when('the internal user opens the survey data panel')
def internal_user_views_the_survey_page(context):
    reporting_unit.click_data_panel(context.survey_short_name)


@when('the user clicks generate enrolment code')
def internal_user_generates_new_code(context):
    reporting_unit.click_generate_new_code(context.survey_short_name)


@then('a new enrolment code is displayed back to the user')
def internal_user_views_generated_code(_):
    iac = enrolment_code.get_new_iac()
    assert iac


def setup_survey_enrolment_for_test(context):
    ''' Setup up a survey and collection exercise for enrolment tests '''

    # todo debug
    if context.standalone_mode:
        if is_display_an_unused_active_code_scenario(context.scenario_name):
            reset_database()

    period = create_period()
    context.unique_id = create_unique_ru_ref()
    survey_name = format_survey_name(context.feature_name)

    survey_response = setup_survey_for_test(context, period, survey_name)

    # Save values for use later
    context.survey_name = survey_response['survey_name']
    context.survey_short_name = survey_response['survey_short_name']
    context.enrolment_code = survey_response['enrolment_code']

    # Scenario specific setup
    if is_generate_new_enrolment_code_scenario(context.scenario_name):
        user_name = make_respondent_user_name(str(context.unique_id), context.survey_short_name)
        respondent_id = create_respondent(user_name=user_name, enrolment_code=context.enrolment_code)['id']
        create_user_login(user_name)
        enrol_respondent(respondent_id)
    elif is_display_an_unused_active_code_scenario(context.scenario_name):
        make_respondent_user_name(str(context.unique_id), context.survey_short_name)
    elif is_frontstage_can_see_the_survey_they_are_enrolling_in_scenario(context.scenario_name):
        pass
    elif is_frontstage_user_can_create_an_account_scenario(context.scenario_name):
        pass
