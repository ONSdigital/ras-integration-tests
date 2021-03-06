import requests
from behave import given, when, then

from config import Config


@given('services are running')
def services_running(_):
    pass


@when('the system requests action endpoint info')
def requests_action_endpoint_info(context):
    context.response = requests.get(Config.ACTION_SERVICE + Config.INFO)


@when('the system requests action exporter endpoint info')
def requests_action_exporter_endpoint_info(context):
    context.response = requests.get(Config.ACTION_EXPORTER_SERVICE + Config.INFO)


@when('the system requests case endpoint info')
def requests_case_endpoint_info(context):
    context.response = requests.get(Config.CASE_SERVICE + Config.INFO)


@when('the system requests collection exercise endpoint info')
def requests_collection_exercise_endpoint_info(context):
    context.response = requests.get(Config.COLLECTION_EXERCISE_SERVICE + Config.INFO)


@when('the system requests collection instrument endpoint info')
def requests_collection_instrument_endpoint_info(context):
    context.response = requests.get(Config.COLLECTION_INSTRUMENT_SERVICE + Config.INFO)


@when('the system requests django endpoint info')
def requests_django_endpoint_info(context):
    context.response = requests.get(Config.AUTH_SERVICE + Config.INFO)


@when('the system requests frontstage endpoint info')
def requests_frontstage_endpoint_info(context):
    context.response = requests.get(Config.FRONTSTAGE_SERVICE + Config.INFO)


@when('the system requests iac endpoint info')
def requests_iac_endpoint_info(context):
    context.response = requests.get(Config.IAC_SERVICE + Config.INFO)


@when('the system requests notify gateway endpoint info')
def requests_notify_gateway_endpoint_info(context):
    context.response = requests.get(Config.NOTIFY_GATEWAY_SERVICE + Config.INFO)


@when('the system requests party endpoint info')
def requests_party_endpoint_info(context):
    context.response = requests.get(Config.PARTY_SERVICE + Config.INFO)


@when('the system requests response operations ui endpoint info')
def requests_response_operations_ui_endpoint_info(context):
    context.response = requests.get(Config.RESPONSE_OPERATIONS_UI + Config.INFO)


@when('the system requests respondent home ui endpoint info')
def requests_respondent_home_ui_endpoint_info(context):
    context.response = requests.get(Config.RESPONDENT_HOME_UI + Config.INFO)


@when('the system requests sample endpoint info')
def requests_sample_endpoint_info(context):
    context.response = requests.get(Config.SAMPLE_SERVICE + Config.INFO)


@when('the system requests secure message endpoint info')
def requests_secure_message_endpoint_info(context):
    context.response = requests.get(Config.SECURE_MESSAGE_SERVICE + Config.INFO)


@when('the system requests survey endpoint info')
def requests_survey_endpoint_info(context):
    context.response = requests.get(Config.SURVEY_SERVICE + Config.INFO)


@then('a success status code (200) is returned')
def success_returned(context):
    assert context.response.status_code == 200, context.response.status_code
