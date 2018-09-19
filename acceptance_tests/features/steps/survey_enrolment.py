from behave import given, when, then

from acceptance_tests import browser
from acceptance_tests.features.pages import enrolment_code, reporting_unit, home
from common import respondent_utilities


@given("the respondent is ready to enrol in a survey")
def ready_to_enrol_in_survey(context):
    home.go_to_external_home()
    browser.find_by_id('create-account').click()


@given("a respondent has got their enrolment code")
def generate_enrolment_code(context):
    pass


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
    enter_enrolment_code(context)


@when('they enter their account details')
def complete_account_details(context):
    context.email = respondent_utilities.make_respondent_user_name(str(context.unique_id),
                                                                   context.survey_short_name)

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
    # setup_survey_enrolment_for_test(context)
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


def scenario_setup_display_an_unused_enrolment_code(context):
    respondent_utilities.make_respondent_user_name(str(context.unique_id), context.survey_short_name)


def scenario_setup_make_a_request_for_a_new_code(context):
    user_name = respondent_utilities.make_respondent_user_name(str(context.unique_id), context.survey_short_name)
    respondent_id = \
        respondent_utilities.create_respondent(user_name=user_name, enrolment_code=context.enrolment_code)['id']
    respondent_utilities.create_respondent_user_login_account(user_name)
    respondent_utilities.enrol_respondent(respondent_id)


def scenario_setup_frontstage_can_see_the_survey_they_are_enrolling_in(context):
    pass


def scenario_setup_frontstage_user_can_create_an_account(context):
    pass


def feature_setup_survey_enrolment_for_test(context):
    # Scenario specific setup

    scenarios[context.scenario_name](context)


# Add each Scenario name + data setup method handler here
scenarios = {
    'Display an unused active code': scenario_setup_display_an_unused_enrolment_code,
    'Make a request for a new code': scenario_setup_make_a_request_for_a_new_code,
    'Frontstage can see the survey they are enrolling in': scenario_setup_frontstage_can_see_the_survey_they_are_enrolling_in,
    'Frontstage user can create an account': scenario_setup_frontstage_user_can_create_an_account
}
