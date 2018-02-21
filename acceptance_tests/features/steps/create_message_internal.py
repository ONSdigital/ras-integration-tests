from behave import given, when, then

from acceptance_tests import browser
from acceptance_tests.features.pages import create_message_internal


@when("they choose to send them a secure message and navigated to the 'send message' page")
@given("the user is on the send message page")
def navigate_to_send_message(_):
    # TODO This must be updated when the method of passing respondent details is finalised

    create_message_internal.go_to(create_message_internal.found_respondent_details())


@then("the \'To\' field is populated with the respondent's name")
def check_to_field(_):
    # TODO This must be updated when the method of passing respondent details is finalised
    to_field = create_message_internal.get_ru_details_attributes().get('to')
    assert str(to_field) == create_message_internal.found_respondent_details().get('to')


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


@then("they are able to enter free text up to and including 100 characters")
def user_able_to_enter_subject(_):

    # The assertion uses 96 characters because 're: ' may be appended for replies
    create_message_internal.enter_text_in_message_subject('1' * 100)
    assert create_message_internal.get_message_subject_text() == ('1' * 96)

    create_message_internal.enter_text_in_message_subject('1' * 200)
    assert len(create_message_internal.get_message_subject_text()) <= 100


@then("they are able to enter free text up to and including 10,000 characters")
def user_able_to_enter_message_body(_):
    create_message_internal.enter_text_in_message_body('1' * 10000)
    assert create_message_internal.get_message_body_text() == ('1' * 10000)

    create_message_internal.enter_text_in_message_body('1' * 20000)
    assert len(create_message_internal.get_message_body_text()) <= 10000


@when("they enter text in the subject and body of the message")
@given("the user has entered text in the subject and body of the message")
def user_has_entered_text_in_subject_and_body(_):
    create_message_internal.enter_text_in_message_subject('Message subject')
    create_message_internal.enter_text_in_message_body('Message body')


@then("they are able to send the message")
@when("they select send")
def user_is_able_to_send_message(_):
    create_message_internal.click_message_send_button()
    # TODO assert that the sending succeeds


@when("they choose to cancel out of sending a message")
def user_cancels_sending_message(_):
    create_message_internal.click_cancel_button()


@then("they are navigated back to the page in which they navigated from")
def user_is_navigated_back(_):
    # TODO this not implemented yet
    assert False  # Expected to fail, this is not implemented


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
