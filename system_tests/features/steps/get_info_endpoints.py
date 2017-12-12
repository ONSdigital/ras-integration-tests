import nose
import requests

from config import Config
from behave import given, when
from flask import json


@given('the system requests action endpoint info')
def requests_action_endpoint_info(context):
    context.response = requests.get(Config.ACTION_SERVICE + Config.INFO)


@given('the system requests action exporter endpoint info')
def requests_action_exporter_endpoint_info(context):
    context.response = requests.get(Config.ACTION_EXPORTER + Config.INFO)


@given('the system requests backstage endpoint info')
def requests_backstage_endpoint_info(context):
    context.response = requests.get(Config.BACKSTAGE_SERVICE + Config.INFO)


@given('the system requests case endpoint info')
def requests_case_endpoint_info(context):
    context.response = requests.get(Config.CASE_SERVICE + Config.INFO)


@given('the system requests collection exercise endpoint info')
def requests_collection_exercise_endpoint_info(context):
    context.response = requests.get(Config.COLLECTION_EXERCISE + Config.INFO)


@given('the system requests collection instrument endpoint info')
def requests_collection_instrument_endpoint_info(context):
    context.response = requests.get(Config.COLLECTION_INSTRUMENT_SERVICE + Config.INFO)


@given('the system requests django endpoint info')
def requests_django_endpoint_info(context):
    context.response = requests.get(Config.DJANGO_SERVICE + Config.INFO)


@given('the system requests frontstage-api endpoint info')
def requests_frontstage_api_endpoint_info(context):
    context.response = requests.get(Config.FRONTSTAGE_API_SERVICE + Config.INFO)


@given('the system requests frontstage endpoint info')
def requests_frontstage_endpoint_info(context):
    context.response = requests.get(Config.FRONTSTAGE_SERVICE + Config.INFO)


@given('the system requests iac endpoint info')
def requests_iac_endpoint_info(context):
    context.response = requests.get(Config.IAC_SERVICE + Config.INFO)


@given('the system requests notify gateway endpoint info')
def requests_notify_gateway_endpoint_info(context):
    context.response = requests.get(Config.NOTIFY_GATEWAY_SERVICE + Config.INFO)


@given('the system requests party endpoint info')
def requests_party_endpoint_info(context):
    context.response = requests.get(Config.PARTY_SERVICE + Config.INFO)


@given('the system requests response operations ui endpoint info')
def requests_response_operations_ui_endpoint_info(context):
    context.response = requests.get(Config.RESPONSE_OPERATIONS_UI + Config.INFO)


@given('the system requests sample endpoint info')
def requests_sample_endpoint_info(context):
    context.response = requests.get(Config.SAMPLE_SERVICE + Config.INFO)


@given('the system requests secure message endpoint info')
def requests_secure_message_endpoint_info(context):
    context.response = requests.get(Config.SECURE_MESSAGE_SERVICE + Config.INFO)


@given('the system requests survey endpoint info')
def requests_survey_endpoint_info(context):
    context.response = requests.get(Config.SURVEY_SERVICE + Config.INFO)


@when('the action endpoint info is returned')
def action_endpoint_info_is_returned(context):
    response = json.loads(context.response.text)
    nose.tools.assert_equal(response['name'], 'actionsvc')
    nose.tools.assert_equal(response['version'], '10.49.4-SNAPSHOT')


@when('the action exporter endpoint info is returned')
def action_exporter_endpoint_info_is_returned(context):
    response = json.loads(context.response.text)
    nose.tools.assert_equal(response['name'], 'actionexportersvc')
    nose.tools.assert_equal(response['version'], '10.49.1-SNAPSHOT')


@when('the backstage endpoint info is returned')
def backstage_endpoint_info_is_returned(context):
    response = json.loads(context.response.text)
    nose.tools.assert_equal(response['name'], 'RAS Int Backstage Service')
    nose.tools.assert_equal(response['version'], '0.0.1')


@when('the case endpoint info is returned')
def case_endpoint_info_is_returned(context):
    response = json.loads(context.response.text)
    nose.tools.assert_equal(response['name'], 'casesvc')
    nose.tools.assert_equal(response['version'], '10.49.1-SNAPSHOT')


@when('the collection exercise endpoint info is returned')
def collection_exercise_endpoint_info_is_returned(context):
    response = json.loads(context.response.text)
    nose.tools.assert_equal(response['name'], 'collectionexercisesvc')
    nose.tools.assert_equal(response['version'], '10.49.2-SNAPSHOT')


@when('the collection instrument endpoint info is returned')
def collection_instrument_endpoint_info_is_returned(context):
    response = json.loads(context.response.text)
    nose.tools.assert_equal(response['name'], 'ras-collection-instrument')
    nose.tools.assert_equal(response['version'], '1.0.2')


@when('the django endpoint info is returned')
def django_endpoint_info_is_returned(context):
    response = json.loads(context.response.text)
    nose.tools.assert_equal(response['name'], 'ras-django')
    nose.tools.assert_equal(response['version'], '1.0.0')


@when('the frontstage-api endpoint info is returned')
def frontstage_api_endpoint_info_is_returned(context):
    response = json.loads(context.response.text)
    nose.tools.assert_equal(response['name'], 'ras-frontstage-api')
    nose.tools.assert_equal(response['version'], '0.0.1')


@when('the frontstage endpoint info is returned')
def frontstage_endpoint_info_is_returned(context):
    response = json.loads(context.response.text)
    nose.tools.assert_equal(response['name'], 'ras-frontstage')
    nose.tools.assert_equal(response['version'], '0.2.0')


@when('the iac endpoint info is returned')
def iac_endpoint_info_is_returned(context):
    response = json.loads(context.response.text)
    nose.tools.assert_equal(response['name'], 'iacsvc')
    nose.tools.assert_equal(response['version'], '10.49.1-SNAPSHOT')


@when('the notify gateway endpoint info is returned')
def notify_gateway_endpoint_info_is_returned(context):
    response = json.loads(context.response.text)
    nose.tools.assert_equal(response['name'], 'notifygatewaysvc')
    nose.tools.assert_equal(response['version'], '10.49.2-SNAPSHOT')


@when('the party endpoint info is returned')
def party_endpoint_info_is_returned(context):
    response = json.loads(context.response.text)
    nose.tools.assert_equal(response['name'], 'ras-party')
    nose.tools.assert_equal(response['version'], '1.0.0')


@when('the response operations ui endpoint info is returned')
def response_operations_ui_endpoint_info_is_returned(context):
    response = json.loads(context.response.text)
    nose.tools.assert_equal(response['name'], 'response-operations-ui')
    nose.tools.assert_equal(response['version'], '0.0.1')


@when('the sample endpoint info is returned')
def sample_endpoint_info_is_returned(context):
    response = json.loads(context.response.text)
    nose.tools.assert_equal(response['name'], 'samplesvc')
    nose.tools.assert_equal(response['version'], '10.49.2-SNAPSHOT')


@when('the secure message endpoint info is returned')
def secure_message_endpoint_info_is_returned(context):
    response = json.loads(context.response.text)
    nose.tools.assert_equal(response['name'], 'ras-secure-message')
    nose.tools.assert_equal(response['version'], '0.1.0')


@when('the survey endpoint info is returned')
def survey_endpoint_info_is_returned(context):
    response = json.loads(context.response.text)
    nose.tools.assert_equal(response['name'], 'surveysvc')
    nose.tools.assert_equal(response['version'], '10.47.0')


