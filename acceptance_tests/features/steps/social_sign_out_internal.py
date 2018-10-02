from behave import then, when

from acceptance_tests.features.pages import sign_out_internal


@then('the user is logged out and shown the sign in page and they see a successfully signed out message (social)')
def view_home_page_social(_):
    sign_out_internal.signed_out_successfully_message()


@when('they click the sign out link (social)')
@then('the internal user signs out (social)')
def sign_out_social(_):
    sign_out_internal.sign_out()
