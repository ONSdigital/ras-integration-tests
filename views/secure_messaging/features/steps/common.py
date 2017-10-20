import nose
from behave import given, then


@then('a success status code ({status_code}) is returned')
def step_impl_success_returned(context, status_code):
    nose.tools.assert_equal(context.response.status_code, int(status_code))
