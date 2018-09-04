from behave import then, when

from acceptance_tests.features.pages import sign_out_internal


@then('the user is logged out and shown the sign in page and they see a successfully signed out message')
def view_home_page(_):
    sign_out_internal.signed_out_successfully_message()


@when('they click the sign out link')
@then('the internal user signs out')
def sign_out(_):
    sign_out_internal.sign_out()
