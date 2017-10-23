import nose
from behave import given, then
from flask import json
import requests

from config import settings


@given('the user requests endpoint info')
def step_impl_requests_endpoint_info(context):
    context.response = requests.get(settings.SECURE_MESSAGING_SERVICE +
                                    settings.SECURE_MESSAGING_SERVICE_API.get('info'))


@then('the endpoint info is returned')
def step_impl_endpoint_info_is_returned(context):
    response = json.loads(context.response.text)
    nose.tools.assert_equal(response['name'], 'ras-secure-message')
    nose.tools.assert_equal(response['version'], '0.1.0')
