import nose
import config
import requests

from config import Config
from behave import given, then
from flask import json


@given('the user requests endpoint info')
def step_impl_requests_endpoint_info(context):
    context.response = requests.get(Config.RAS_SECURE_MESSAGE_SERVICE_API)


@then('the endpoint info is returned')
def step_impl_endpoint_info_is_returned(context):
    response = json.loads(context.response.text)
    nose.tools.assert_equal(response['name'], 'ras-secure-message')
    nose.tools.assert_equal(response['version'], '0.1.0')
