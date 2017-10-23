import nose
from behave import then


@then('a success status code (200) is returned')
def step_impl_success_returned(context):
    nose.tools.assert_equal(context.response.status_code, 200)
