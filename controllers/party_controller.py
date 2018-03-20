import json
import logging

import requests
from structlog import wrap_logger

from config import Config

logger = wrap_logger(logging.getLogger(__name__))


def register_respondent(email_address, first_name, last_name, password, phone_number, enrolment_code):
    logger.debug('Post respondent to party service')

    registration_data = {
        'emailAddress': email_address,
        'firstName': first_name,
        'lastName': last_name,
        'password': password,
        'telephone': phone_number,
        'enrolmentCode': enrolment_code
    }

    url = Config.PARTY_SERVICE + '/party-api/v1/respondents'

    response = requests.post(url, json=registration_data, auth=Config.BASIC_AUTH)

    if response.status_code != 200:
        logger.error('Failed to register respondent', status=response.status_code)
        raise Exception('Failed to register respondent')

    return json.loads(response.text)


def get_respondent_details(respondent_id):
    url = f'{Config.PARTY_SERVICE}/party-api/v1/respondents/id/{respondent_id}'
    response = requests.get(url=url, auth=Config.BASIC_AUTH)
    response.raise_for_status()
    return response.json()


def get_party_by_ru_ref(ru_ref):
    logger.debug('Retrieving reporting unit', ru_ref=ru_ref)
    url = f'{Config.PARTY_SERVICE}/party-api/v1/parties/type/B/ref/{ru_ref}'
    response = requests.get(url, auth=Config.BASIC_AUTH)

    if response.status_code != 200:
        logger.error('Error retrieving reporting unit', ru_ref=ru_ref)
        raise Exception('Failed to retrieve reporting unit')

    logger.debug('Successfully retrieved reporting unit', ru_ref=ru_ref)
    return response.json()


def add_survey(party_id, enrolment_code):
    logger.debug('Adding a survey')
    url = f'{Config.PARTY_SERVICE}/party-api/v1/respondents/add_survey'
    request_json = {"party_id": party_id, "enrolment_code": enrolment_code}
    response = requests.post(url, json=request_json, auth=Config.BASIC_AUTH)

    if response.status_code != 200:
        logger.error('Failed to add survey', status=response.status_code)
        raise Exception('Failed to add survey')

    logger.debug('Successfully added a survey')


def get_party_by_email(email):
    logger.debug('Retrieving party by email address', email=email)
    url = f'{Config.PARTY_SERVICE}/party-api/v1/respondents/email/{email}'
    response = requests.get(url, auth=Config.BASIC_AUTH)

    if response.status_code == 404:
        logger.info('Email not found', email=email)
        return

    elif response.status_code != 200:
        logger.error('Error retrieving email address', email=email)
        raise Exception('Failed to retrieve email address')

    logger.debug('Successfully retrieved email address', email=email)
    return response.json()
