from behave import given, when, then

from acceptance_tests import browser
from acceptance_tests.features.pages import surveys_todo, create_message_external


@given('the respondent is on their todo list')
@when('the respondent navigates to their surveys todo list')
def surveys_todo_list(_):
    surveys_todo.go_to()


@then('the respondent is able to send a message')
def able_to_send_message_for_survey_ru(_):
    browser.find_by_id('create-message-link-1')


@given('the respondent chooses to send a message to ONS')
@given('the respondent is sending a message in relation to bricks')
@when('the respondent chooses to send a message for a specific RU and survey')
def select_create_message(_):
    surveys_todo.go_to()
    surveys_todo.select_to_create_message()


@then('the respondent is navigated to the create message page')
def assert_create_message_page(_):
    browser.find_by_id('secure-message-subject')


@when('the respondent enters a valid message')
def enter_valid_message(_):
    create_message_external.enter_valid_subject()
    create_message_external.enter_valid_body()


@then('the message will be sent to the internal Bricks mailbox')
def message_sent_to_bricks_workgroup(_):
    current_url = browser.driver.current_url
    assert 'survey=cb8accda-6118-4d3b-85a3-149e28960c54' in current_url


@when('the respondent enters more than 96 characters in the subject field')
def subject_field_too_long(_):
    create_message_external.enter_invalid_length_subject()
    create_message_external.enter_valid_body()


@when('chooses to send the message')
@when('the message is sent')
@when('selects to send message')
def click_send_message_btn(_):
    create_message_external.send_message()


@then('an error message appears specifying subject too long')
def check_for_error_subject_too_long(_):
    browser.driver.find_element_by_link_text('Subject field length must not be greater than 100')


@when('the respondent enters more than 10000 characters in the body field')
def body_too_long(_):
    create_message_external.enter_valid_subject()
    create_message_external.enter_invalid_length_body()


@then('an error message appears specifying body too long')
def check_for_body_too_long_error(_):
    browser.driver.find_element_by_link_text('Body field length must not be greater than 10000')


@when('the respondent tries to send the message without populating the body and subject fields')
def empty_subject_and_body_fields(_):
    create_message_external.empty_subject()
    create_message_external.empty_body()
    create_message_external.send_message()


@then('an error message appears specifying body and subject fields are required')
def error_require_body_and_subject(_):
    browser.driver.find_element_by_link_text('Please enter a subject')
    browser.driver.find_element_by_link_text('Please enter a message')


@then('the respondent is navigated to their inbox')
def navigated_to_inbox(_):
    browser.driver.find_element_by_css_selector("a#inbox-list.navigation-tabs__tab.navigation-tabs__tab--active")  # NOQA


@then('the respondent is navigated to their inbox and notified message sent successfully')
def navigated_to_inbox_show_message_sent_notif(_):
    browser.driver.find_element_by_css_selector("a#inbox-list.navigation-tabs__tab.navigation-tabs__tab--active")  # NOQA
    browser.driver.find_element_by_id("message-success-notif")


@when('the respondent populates the body field but not the subject')
def populate_body_not_subject(_):
    create_message_external.empty_subject()
    create_message_external.enter_valid_body()


@then('an error message appears specifying subject must be populated')
def assert_error_no_subject(_):
    browser.driver.find_element_by_link_text('Please enter a subject')


@when('the respondent populates the subject field but not the body field')
def populate_subject_no_body(_):
    create_message_external.enter_valid_subject()
    create_message_external.empty_body()


@then('an error message appears notifying the respondent a body must be supplied')
def assert_error_no_body(_):
    browser.driver.find_element_by_link_text('Please enter a message')
