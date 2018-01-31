from acceptance_tests.features.pages import sign_in_internal
from behave import given, when, then


@given('The user has an active account and is assigned a username and password')
def go_to_sign_in(_):
    sign_in_internal.go_to()


@when('They enter the correct username and password')
def sign_in_correct_username_and_password(_):
    sign_in_internal.enter_correct_username()
    sign_in_internal.enter_correct_password()
    sign_in_internal.internal_sign_in_btn()


@when('They enter an incorrect username and correct password')
def sign_in_incorrect_username_and_correct_password(_):
    sign_in_internal.enter_incorrect_username()
    sign_in_internal.enter_correct_password()
    sign_in_internal.internal_sign_in_btn()


@when('They enter a correct username and incorrect password')
def sign_in_correct_username_and_incorrect_password(_):
    sign_in_internal.enter_correct_username()
    sign_in_internal.enter_incorrect_password()
    sign_in_internal.internal_sign_in_btn()


@when('They enter an incorrect username and password')
def sign_in_incorrect_username_and_password(_):
    sign_in_internal.enter_incorrect_username()
    sign_in_internal.enter_incorrect_password()
    sign_in_internal.internal_sign_in_btn()


@when('They enter a correct username and no password')
def sign_in_correct_username_and_no_password(_):
    sign_in_internal.enter_correct_username()
    sign_in_internal.internal_sign_in_btn()


@when('They enter no username and a correct password')
def sign_in_no_username_and_correct_password(_):
    sign_in_internal.enter_correct_password()
    sign_in_internal.internal_sign_in_btn()


@when('They enter no username and no password')
def sign_in_no_username_and_no_password(_):
    sign_in_internal.internal_sign_in_btn()


@then('The user is directed to their home page')
def sign_in_directed_to_home_page(_):
    pass


@then('The user is notified that an error has occurred')
def error_occurred(_):
    pass
