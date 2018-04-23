import logging
from acceptance_tests.features.pages import sign_in_internal, home, sign_out_internal
from behave import given, when, then

from structlog import wrap_logger

logger = wrap_logger(logging.getLogger(__name__))


@given('the user has an active account and is assigned a username and password')
def go_to_sign_in(_):
    home.go_to()
    try_sign_out()
    sign_in_internal.go_to()


def try_sign_out():
    """
    Sign out if already signed in
    :return:
    """
    try:
        sign_out_internal.sign_out()
    except AttributeError:
        pass


@when('they enter the correct username and password')
def sign_in_correct_username_and_password(_):
    sign_in_internal.enter_correct_username()
    sign_in_internal.enter_correct_password()
    sign_in_internal.click_internal_sign_in_button()


@when('they enter an incorrect username and correct password')
def sign_in_incorrect_username_and_correct_password(_):
    sign_in_internal.enter_incorrect_username()
    sign_in_internal.enter_correct_password()
    sign_in_internal.click_internal_sign_in_button()


@when('they enter a correct username and incorrect password')
def sign_in_correct_username_and_incorrect_password(_):
    sign_in_internal.enter_correct_username()
    sign_in_internal.enter_incorrect_password()
    sign_in_internal.click_internal_sign_in_button()


@when('they enter an incorrect username and password')
def sign_in_incorrect_username_and_password(_):
    sign_in_internal.enter_incorrect_username()
    sign_in_internal.enter_incorrect_password()
    sign_in_internal.click_internal_sign_in_button()


@when('they enter a correct username and no password')
def sign_in_correct_username_and_no_password(_):
    sign_in_internal.enter_correct_username()
    sign_in_internal.click_internal_sign_in_button()


@when('they enter no username and a correct password')
def sign_in_no_username_and_correct_password(_):
    sign_in_internal.enter_correct_password()
    sign_in_internal.click_internal_sign_in_button()


@when('they enter no username and no password')
def sign_in_no_username_and_no_password(_):
    sign_in_internal.click_internal_sign_in_button()


@then('the user is directed to their home page')
def sign_in_directed_to_home_page(_):
    # TODO: Update to check for a more distinct hope page feature when implemented
    assert sign_in_internal.get_page_title() == "Home | Survey Data Collection"
    logger.info("page title", title = sign_in_internal.get_page_title())
    #home.click_surveys_link()


@then('the user is notified that a username is required')
def sign_in_username_required(_):
    sign_in_internal.check_username_required()


@then('The user is notified that a password is required')
def sign_in_password_required(_):
    sign_in_internal.check_password_required()


@then('the user is notified that a username and password is required')
def sign_in_username_and_password_required(_):
    sign_in_internal.check_username_required()
    sign_in_internal.check_password_required()


@then('the user is notified that an authentication error has occurred')
def authentication_error_occurred(_):
    sign_in_internal.check_authentication_error_message()
