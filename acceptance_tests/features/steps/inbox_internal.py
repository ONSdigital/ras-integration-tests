from datetime import datetime

from behave import given, when, then

from acceptance_tests.features.pages import home, inbox_internal
from acceptance_tests.features.pages.internal_conversation_view import go_to_thread
from acceptance_tests.features.steps.authentication import signed_in_internal
from config import Config
from controllers import messages_controller, database_controller


@given('the user has access to secure messaging')
def verify_messages_link_present(_):
    assert home.verify_messages_link_present()


@given('the user has got messages in their inbox')
def populate_database_with_messages(_):

    subject = "This is the subject of the message"
    body = "This is the body of the message"
    messages_controller.create_message_internal_to_external(subject, body)

    inbox_internal.go_to()


@given("the user has got '{number_of_messages}' messages in their inbox")
def populate_database_with_number_of_messages(_, number_of_messages):
    for i in range(0, int(number_of_messages)):
        subject = str(i) + ": This is the subject of the message"
        body = str(i) + ": This is the body of the message"
        messages_controller.create_message_internal_to_external(subject, body)

    inbox_internal.go_to()


@given('the user has no messages in their inbox')
def user_has_no_messages_in_inbox(_):
    database_controller.execute_sql('resources/database/database_reset_secure_message.sql',
                                    database_uri=Config.SECURE_MESSAGE_DATABASE_URI)


@when('they navigate to the inbox messages')
def internal_user_views_messages(_):
    inbox_internal.go_to()


@then('they are informed that there are no messages')
def informed_of_no_messages(_):
    assert inbox_internal.get_no_messages_text()


@when('they navigate to closed conversations')
def internal_user_views_closed_messages(_):
    inbox_internal.go_to_closed()


@then('they are informed that there are no closed conversations')
def informed_of_no_closed_conversations(_):
    assert inbox_internal.get_no_closed_conversations_text()


@then('they are able to view all received messages')
def test_presence_of_messages(_):
    assert len(inbox_internal.get_messages()) > 0


@then("they are able to view '{number_of_messages}' messages")
def test_presence_of_number_of_messages(_, number_of_messages):
    assert inbox_internal.get_message_link_index(number_of_messages)


@then('they are able to view the RU Ref, Subject, From, To, Date and time for each message')
def test_inbox_headings(_):
    assert inbox_internal.get_table_heading() == "RU Ref Business name Subject From To Date and time"


@then('they are able to view all received messages in reverse chronological order/latest first')
def test_message_order(_):
    messages = inbox_internal.get_messages()
    first_message_date = datetime.strptime(messages[0].get('received').split(' ')[2], '%H:%M')
    second_message_date = datetime.strptime(messages[1].get('received').split(' ')[2], '%H:%M')
    assert first_message_date >= second_message_date


@when('they navigate to the select survey page')
def test_view_select_survey_page(_):
    inbox_internal.go_to_select_survey()


@then('they are able to view a dropdown list of surveys')
def test_select_survey_page_view(_):
    assert inbox_internal.get_filter_page_title()
    assert inbox_internal.get_dropdown_list()


@when('the user has an unread message in their inbox')
def internal_user_has_unread_message_in_inbox(context):
    messages_controller.create_message_external_to_internal(context, 'message subject', 'message body')

    # Sending external to internal may sign out the internal user
    signed_in_internal(None)


@then('they are able to distinguish that the message is unread')
def internal_user_can_distinguish_the_message_is_unread(_):
    assert len(inbox_internal.get_unread_messages()) > 0


@when('they view the unread message')
def internal_user_views_unread_message(_):
    go_to_thread()


@then('the message is no longer marked as unread')
def message_is_no_longer_marked_unread_in_internal_inbox(_):
    assert len(inbox_internal.get_unread_messages()) == 0


@then('the pagination links are available')
def pagination_links_available(_):
    assert inbox_internal.get_pagination_previous_link()
    assert inbox_internal.get_pagination_next_link()


@then('they can see the closed tab')
def closed_tab_is_visible(_):
    assert inbox_internal.closed_tab_present()
