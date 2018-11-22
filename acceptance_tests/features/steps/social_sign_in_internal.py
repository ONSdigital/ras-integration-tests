import logging

from behave import given, when, then
from structlog import wrap_logger

from acceptance_tests.features.pages import social_sign_in_internal, social_home, social_sign_out_internal

logger = wrap_logger(logging.getLogger(__name__))


@given('the user has an active account and is assigned a username and password (social)')
def go_to_sign_in(_):
    social_home.go_to()
    try_sign_out()
    social_sign_in_internal.go_to()


def try_sign_out():
    """
    Sign out if already signed in
    :return:
    """
    try:
        social_sign_out_internal.sign_out()
    except AttributeError:
        pass


@when('they enter the correct username and password (social)')
def sign_in_correct_username_and_password(context):
    social_sign_in_internal.enter_correct_username(context.internal_user_name)
    social_sign_in_internal.enter_correct_password()
    social_sign_in_internal.click_internal_sign_in_button()


@when('they enter an incorrect username and correct password (social)')
def sign_in_incorrect_username_and_correct_password(_):
    social_sign_in_internal.enter_incorrect_username()
    social_sign_in_internal.enter_correct_password()
    social_sign_in_internal.click_internal_sign_in_button()


@when('they enter a correct username and incorrect password (social)')
def sign_in_correct_username_and_incorrect_password(context):
    social_sign_in_internal.enter_correct_username(context.internal_user_name)
    social_sign_in_internal.enter_incorrect_password()
    social_sign_in_internal.click_internal_sign_in_button()


@when('they enter an incorrect username and password (social)')
def sign_in_incorrect_username_and_password(_):
    social_sign_in_internal.enter_incorrect_username()
    social_sign_in_internal.enter_incorrect_password()
    social_sign_in_internal.click_internal_sign_in_button()


@when('they enter a correct username and no password (social)')
def sign_in_correct_username_and_no_password(context):
    social_sign_in_internal.enter_correct_username(context.internal_user_name)
    social_sign_in_internal.click_internal_sign_in_button()


@when('they enter no username and a correct password (social)')
def sign_in_no_username_and_correct_password(_):
    social_sign_in_internal.enter_correct_password()
    social_sign_in_internal.click_internal_sign_in_button()


@when('they enter no username and no password (social)')
def sign_in_no_username_and_no_password(_):
    social_sign_in_internal.click_internal_sign_in_button()


@then('the user is directed to their home page (social)')
def sign_in_directed_to_home_page(_):
    assert social_sign_in_internal.get_page_title() == "Find a case | Social Survey Data Collection"


@then('the user is notified that a username is required (social)')
def sign_in_username_required(_):
    social_sign_in_internal.check_username_required()


@then('The user is notified that a password is required (social)')
def sign_in_password_required(_):
    social_sign_in_internal.check_password_required()


@then('the user is notified that a username and password is required (social)')
def sign_in_username_and_password_required(_):
    social_sign_in_internal.check_username_required()
    social_sign_in_internal.check_password_required()


@then('the user is notified that an authentication error has occurred (social)')
def authentication_error_occurred(_):
    social_sign_in_internal.check_authentication_error_message()
