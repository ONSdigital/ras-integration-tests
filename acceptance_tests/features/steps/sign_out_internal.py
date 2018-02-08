from acceptance_tests.features.pages import sign_out_internal
from behave import then


@then('the user is logged out and shown the sign in page and they see a successfully signed out message')
def view_home_page(_):
    sign_out_internal.signed_out_successfully_message()
