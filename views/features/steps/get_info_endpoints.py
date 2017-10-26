import nose
import requests

from config import Config
from behave import given, when
from flask import json


@given('the system requests secure message endpoint info')
def requests_secure_message_endpoint_info(context):
    context.response = requests.get(Config.RAS_SECURE_MESSAGE_SERVICE + Config.RAS_INFO)


@given('the system requests frontstage endpoint info')
def requests_frontstage_endpoint_info(context):
    context.response = requests.get(Config.RAS_FRONTSTAGE_SERVICE + Config.RAS_INFO)


@given('the system requests backstage endpoint info')
def requests_backstage_endpoint_info(context):
    context.response = requests.get(Config.RAS_BACKSTAGE_SERVICE + Config.RAS_INFO)


@given('the system requests party endpoint info')
def requests_party_endpoint_info(context):
    context.response = requests.get(Config.RAS_PARTY_SERVICE + Config.RAS_INFO)


@given('the system requests collection instrument endpoint info')
def requests_collection_instrument_endpoint_info(context):
    context.response = requests.get(Config.RAS_COLLECTION_INSTRUMENT_SERVICE + Config.RAS_INFO)


@given('the system requests django endpoint info')
def requests_django_endpoint_info(context):
    context.response = requests.get(Config.RAS_DJANGO_SERVICE + Config.RAS_INFO)


@given('the system requests api gateway endpoint info')
def requests_api_gateway_endpoint_info(context):
    context.response = requests.get(Config.RAS_API_GATEWAY_SERVICE + Config.RAS_INFO)


@when('the secure message endpoint info is returned')
def secure_message_endpoint_info_is_returned(context):
    response = json.loads(context.response.text)
    nose.tools.assert_equal(response['name'], 'ras-secure-message')
    nose.tools.assert_equal(response['version'], '0.1.0')


@when('the frontstage endpoint info is returned')
def frontstage_endpoint_info_is_returned(context):
    response = json.loads(context.response.text)
    nose.tools.assert_equal(response['name'], 'ras-frontstage')
    nose.tools.assert_equal(response['version'], '0.2.0')


@when('the backstage endpoint info is returned')
def backstage_endpoint_info_is_returned(context):
    response = json.loads(context.response.text)
    nose.tools.assert_equal(response['name'], 'RAS Int Backstage Service')
    nose.tools.assert_equal(response['version'], '0.0.1')


@when('the party endpoint info is returned')
def party_endpoint_info_is_returned(context):
    response = json.loads(context.response.text)
    nose.tools.assert_equal(response['name'], 'ras-party')
    nose.tools.assert_equal(response['version'], '1.0.0')


@when('the collection instrument endpoint info is returned')
def collection_instrument_endpoint_info_is_returned(context):
    response = json.loads(context.response.text)
    nose.tools.assert_equal(response['name'], 'collectioninstrumentsvc')
    nose.tools.assert_equal(response['version'], '0.1.1')


@when('the django endpoint info is returned')
def django_endpoint_info_is_returned(context):
    response = json.loads(context.response.text)
    nose.tools.assert_equal(response['name'], 'ras-django')
    nose.tools.assert_equal(response['version'], '1.0.0')


@when('the api gateway endpoint info is returned')
def api_gateway_endpoint_info_is_returned(context):
    response = json.loads(context.response.text)
    nose.tools.assert_equal(response['name'], 'apigatewaysvc')
    nose.tools.assert_equal(response['version'], '0.1.0')
