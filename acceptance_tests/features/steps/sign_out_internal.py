from behave import given, then, when

from acceptance_tests.features.pages.sign_out_internal import signed_out_successfully_message, try_sign_out


@then('the user is logged out and shown the sign in page and they see a successfully signed out message')
def view_home_page(_):
    signed_out_successfully_message()


@given('the internal user signs out')
@when('the internal user signs out')
@then('the internal user signs out')
def sign_out(_):
    try_sign_out()
