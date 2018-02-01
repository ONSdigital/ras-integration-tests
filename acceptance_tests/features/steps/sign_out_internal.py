from acceptance_tests.features.pages import sign_out_internal
from behave import given, when, then


@when('They click the sign out link')
def click_sign_out_link():
    sign_out_internal.internal_sign_out_link()


@then('The user is logged out and shown the homepage')
def view_home_page():
    pass
