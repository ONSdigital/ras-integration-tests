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


def add_survey(party_id, enrolment_code):
    logger.debug('Adding a survey')
    url = f'{Config.PARTY_SERVICE}/party-api/v1/respondents/add_survey'
    request_json = {"party_id": party_id, "enrolment_code": enrolment_code}
    response = requests.post(url, json=request_json, auth=Config.BASIC_AUTH)

    if response.status_code != 200:
        logger.error('Failed to add survey', status=response.status_code)
        raise Exception('Failed to add survey')

    logger.debug('Successfully added a survey')
