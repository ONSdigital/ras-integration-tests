import nose
import requests

from config import Config
from behave import given, when
from flask import json


@given('the user requests secure message endpoint info')
def step_impl_requests_sm_endpoint_info(context):
    context.response = requests.get(Config.RAS_SECURE_MESSAGE_INFO)


@given('the user requests frontstage endpoint info')
def step_impl_requests_fs_endpoint_info(context):
    context.response = requests.get(Config.RAS_FRONTSTAGE_INFO)


@when('the secure message endpoint info is returned')
def step_impl_sm_endpoint_info_is_returned(context):
    response = json.loads(context.response.text)
    nose.tools.assert_equal(response['name'], 'ras-secure-message')
    nose.tools.assert_equal(response['version'], '0.1.0')


@when('the frontstage endpoint info is returned')
def step_impl_fs_endpoint_info_is_returned(context):
    response = json.loads(context.response.text)
    nose.tools.assert_equal(response['name'], 'ras-frontstage')
    nose.tools.assert_equal(response['version'], '0.2.0')
