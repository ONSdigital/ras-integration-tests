from behave import given, when, then

from acceptance_tests import browser
from acceptance_tests.features.pages import surveys_todo, add_a_survey
from common.browser_utilities import wait_for_element_by_id


@when('the respondent views the survey list todo page')
@when('access to do list in my surveys')
def surveys_to_do_list(context):
    surveys_todo.go_to()


@given('selects to add a new survey')
@when('they add a new survey')
@then('they are able to add a new survey')
def add_a_new_survey(context):
    browser.find_by_id('add_survey_button').click()


@then('they are able to enter an enrolment code')
def enter_enrolment_code(context):
    browser.find_by_id('ENROLMENT_CODE_FIELD')


@given('the user has entered a valid enrolment code')
@when('they enter a valid enrolment code')
def enter_valid_enrolment_code(context):
    add_a_survey.go_to()
    browser.driver.find_element_by_id('ENROLEMENT_CODE_FIELD').send_keys(context.iac)
    browser.find_by_id('continue_button').click()


@then('they are to be presented with the survey and organisation that they are enrolling for')
def view_confirmation_page(context):
    browser.find_by_id('confirm-org-title')


@when('they enter an invalid enrolment code')
def enter_invalid_enrolment_code(context):
    browser.driver.find_element_by_id('ENROLEMENT_CODE_FIELD').send_keys('222thu78nj7m')
    browser.find_by_id('continue_button').click()


@then('they are to be notified')
def invalid_enrolment_code_notification(context):
    browser.find_by_id('error_notification')


@when('they continue and confirm that the organisation and survey that they are enrolling for is correct')
def confirm_organisation_and_continue(context):
    browser.find_by_id('confirm_survey_button').click()


@then('the new survey is to be listed in My Surveys and confirmation is presented to the user')
def confirmation_presented_for_new_survey(context):
    wait_for_element_by_id('NEW_SURVEY_NOTIF', timeout=20, retry=1)
    assert browser.find_by_id('NEW_SURVEY_NOTIF')


@when('they navigate to the confirm organisation page and click cancel')
def click_cancel(context):
    browser.find_by_id('cancel_button').click()


@then('the user is navigated back to their "To do" list and they have not enrolled for that survey')
def view_todo_list(context):
    browser.find_by_id('SURVEY_TODO_TAB')\
        .first.has_class('btn btn--secondary btn--border navigation-tabs__tab navigation-tabs__tab--active')


@given('the user has entered a valid enrolment code for a survey they have already added')
def enter_second_enrolment_code(context):
    add_a_survey.go_to()
    browser.driver.find_element_by_id('ENROLEMENT_CODE_FIELD').send_keys(context.second_iac)
    browser.find_by_id('continue_button').click()


@then('the user is notified they have already added the survey')
def already_added_notification_presented_to_user(context):
    assert browser.find_by_id('ALREADY_ADDED_NOTIF').text,\
                'You have already added that survey'
