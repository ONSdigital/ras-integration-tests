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


@given('the user requests backstage endpoint info')
def step_impl_requests_bs_endpoint_info(context):
    context.response = requests.get(Config.RAS_BACKSTAGE_INFO)


@given('the user requests party endpoint info')
def step_impl_requests_party_endpoint_info(context):
    context.response = requests.get(Config.RAS_PARTY_INFO)


@given('the user requests collection instrument endpoint info')
def step_impl_requests_ci_endpoint_info(context):
    context.response = requests.get(Config.RAS_COLLECTION_INSTRUMENT_INFO)


@given('the user requests django endpoint info')
def step_impl_requests_django_endpoint_info(context):
    context.response = requests.get(Config.RAS_DJANGO_INFO)


@given('the user requests api gateway endpoint info')
def step_impl_requests_api_gw_endpoint_info(context):
    context.response = requests.get(Config.RAS_API_GATEWAY_INFO)


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


@when('the backstage endpoint info is returned')
def step_impl_bs_endpoint_info_is_returned(context):
    response = json.loads(context.response.text)
    nose.tools.assert_equal(response['name'], 'ras-backstage')
    nose.tools.assert_equal(response['version'], '0.0.1')


@when('the party endpoint info is returned')
def step_impl_party_endpoint_info_is_returned(context):
    response = json.loads(context.response.text)
    nose.tools.assert_equal(response['name'], 'ras-party')
    nose.tools.assert_equal(response['version'], '1.0.0')


@when('the collection instrument endpoint info is returned')
def step_impl_ci_endpoint_info_is_returned(context):
    response = json.loads(context.response.text)
    nose.tools.assert_equal(response['name'], 'collectioninstrumentsvc')
    nose.tools.assert_equal(response['version'], '0.1.1')


@when('the django endpoint info is returned')
def step_impl_django_endpoint_info_is_returned(context):
    response = json.loads(context.response.text)
    nose.tools.assert_equal(response['name'], 'ras-django')
    nose.tools.assert_equal(response['version'], '1.0.0')


@when('the api gateway endpoint info is returned')
def step_impl_api_gw_endpoint_info_is_returned(context):
    response = json.loads(context.response.text)
    nose.tools.assert_equal(response['name'], 'apigatewaysvc')
    nose.tools.assert_equal(response['version'], '0.1.0')
