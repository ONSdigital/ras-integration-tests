from behave import given

from acceptance_tests.features.pages import sign_in_internal


@given('The internal user is already signed in')
def signed_in(_):
    sign_in_internal.go_to()
    sign_in_internal.enter_correct_username()
    sign_in_internal.enter_correct_password()
    sign_in_internal.internal_sign_in_btn()
