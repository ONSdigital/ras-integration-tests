from behave import given, when, then

from acceptance_tests import browser
from acceptance_tests.features.pages import create_message_internal
from common.collection_exercise_utilities import find_case_by_enrolment_code


@given("The internal user has found the associated respondent")
def user_has_found_respondent(context):
    context.party_id = find_case_by_enrolment_code(context.iac)['partyId']

    assert context.respondent_email is not None
    assert context.party_id is not None
    assert context.short_name is not None


@when("they choose to send them a secure message and navigated to the send message page")
@given("the user is on the send message page")
def navigate_to_send_message(context):
    create_message_internal.go_to(context)


@then("the To field is populated with the respondent's name")
def check_to_field(context):
    to_field = create_message_internal.get_ru_details_attributes().get('to')
    assert str(to_field) == create_message_internal.found_respondent_details(context).get('to')


@when("they enter text in the subject of the message")
def user_enters_text_in_subject(_):
    create_message_internal.enter_text_in_message_subject('Message subject')
    assert create_message_internal.get_message_subject_text() == 'Message subject'
    create_message_internal.clear_message_subject_text()


@when("they enter text in the body of the message")
def user_enters_text_in_message_body(_):
    create_message_internal.enter_text_in_message_body('Message body')
    assert create_message_internal.get_message_body_text() == 'Message body'
    create_message_internal.clear_message_body_text()


@then("they are able to enter free text up to and including 96 characters")
def user_able_to_enter_subject(_):
    create_message_internal.enter_text_in_message_subject('a' * 96)
    assert create_message_internal.get_message_subject_text() == ('a' * 96)

    create_message_internal.enter_text_in_message_subject('a' * 10)
    assert len(create_message_internal.get_message_subject_text()) <= 96
    create_message_internal.clear_message_subject_text()


@then("they are able to enter free text up to and including 10,000 characters")
def user_able_to_enter_message_body(_):
    create_message_internal.enter_text_in_message_body_with_javascript('a' * 9990)
    create_message_internal.enter_text_in_message_body('a' * 10)
    assert create_message_internal.get_message_body_text() == ('a' * 10000)

    create_message_internal.clear_message_body_text()
    create_message_internal.enter_text_in_message_body_with_javascript('a' * 10000)
    create_message_internal.enter_text_in_message_body('a' * 10)
    assert len(create_message_internal.get_message_body_text()) == 10000
    create_message_internal.clear_message_body_text()


@when("they enter text in the subject and body of the message")
@given("the user has entered text in the subject and body of the message")
def user_has_entered_text_in_subject_and_body(_):
    create_message_internal.enter_text_in_message_subject('Message subject')
    create_message_internal.enter_text_in_message_body('Message body')


@then("they are able to send the message")
@when("they select send")
def user_is_able_to_send_message(_):
    create_message_internal.click_message_send_button()
    user_is_navigated_to_inbox(_)


@when("they choose to cancel out of sending a message")
def user_cancels_sending_message(_):
    create_message_internal.click_cancel_button()


@then("they are navigated back to the page in which they navigated from")
def user_is_navigated_back(context):
    assert f"reporting-units/{context.short_name}" in browser.url


@then("they are navigated to the inbox of messages")
@when("they are navigated to the inbox of messages")
def user_is_navigated_to_inbox(_):
    assert 'messages/' in browser.url
    user_is_given_message_sent_confirmation(_)


@given("the user has sent a secure message")
def user_sent_secure_message(_):
    user_has_entered_text_in_subject_and_body(_)
    user_is_able_to_send_message(_)


@then("they are presented with confirmation that the message has been sent")
def user_is_given_message_sent_confirmation(_):
    assert create_message_internal.get_first_flashed_message() == "Message sent."
