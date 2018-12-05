from behave import given, when, then

import acceptance_tests.features.pages.view_and_reply_conversation_external as page_helpers
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
@given('the respondent is sending a message')
@when('the respondent chooses to send a message for a specific RU and survey')
def select_create_message(_):
    surveys_todo.go_to()
    surveys_todo.select_to_create_message()


@then('the respondent is navigated to the create message page')
def assert_create_message_page(_):
    browser.find_by_id('secure-message-subject')


@then('They are able to enter up to and including 10,000 characters')
def enter_text_body_up_to_10000_characters(_):
    # Check user can enter 10000 characters
    page_helpers.enter_text_in_conversation_reply_with_javascript('a' * 9900)
    page_helpers.enter_text_in_conversation_reply('a' * 100)
    assert page_helpers.get_text_from_reply_text_area() == 'a' * 10000

    # Check user cannot enter more than 10000 characters
    page_helpers.enter_text_in_conversation_reply('a' * 100)
    assert page_helpers.get_text_from_reply_text_area() == 'a' * 10000


@when('the respondent enters a valid message')
def enter_valid_message(_):
    create_message_external.enter_valid_subject('123')
    create_message_external.enter_valid_body('345')


@then('the message will be sent to the internal mailbox')
def message_sent_to_bricks_workgroup(context):
    current_url = browser.driver.current_url
    assert context.survey_id in current_url


@when('the respondent enters more than 96 characters in the subject field')
def subject_field_too_long(_):
    create_message_external.enter_invalid_length_subject()
    create_message_external.enter_valid_body('345')


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
    create_message_external.enter_valid_subject('123')
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


@then('the respondent is navigated to their inbox and notified message sent successfully')
def navigated_to_inbox_show_message_sent_notif(_):
    browser.driver.find_element_by_id("flashed-message-1")
    browser.driver.find_element_by_link_text("123")


@when('the respondent populates the body field but not the subject')
def populate_body_not_subject(_):
    create_message_external.empty_subject()
    create_message_external.enter_valid_body('345')


@then('an error message appears specifying subject must be populated')
def assert_error_no_subject(_):
    browser.driver.find_element_by_link_text('Please enter a subject')


@when('the respondent populates the subject field but not the body field')
def populate_subject_no_body(_):
    create_message_external.enter_valid_subject('123')
    create_message_external.empty_body()


@then('an error message appears notifying the respondent a body must be supplied')
def assert_error_no_body(_):
    browser.driver.find_element_by_link_text('Please enter a message')


@when("they enter text in the body of the external message")
def user_enters_text_in_message_body(_):
    create_message_external.enter_valid_body('Message body')
    assert create_message_external.get_message_body_text() == 'Message body'
    create_message_external.empty_body()
