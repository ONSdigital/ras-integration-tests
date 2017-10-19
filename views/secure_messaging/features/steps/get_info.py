import nose
from behave import given, then
from flask import json
import requests


@given('the user requests endpoint info')
def step_impl_requests_endpoint_info(context):
    context.response = requests.get('http://ras-secure-messaging-int.apps.devtest.onsclofo.uk/info')


@then('the endpoint info is returned')
def step_impl_endpoint_info_is_returned(context):
    response = json.loads(context.response.data)
    nose.tools.assert_equal(response['name'], 'ras-secure-message')
    nose.tools.assert_equal(response['version'], '0.1.0')


@then('a success status code (200) is returned')
def step_impl_success_returned(context):
    nose.tools.assert_equal(context.response.status_code, 200)
