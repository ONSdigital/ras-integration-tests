import logging

import requests
from structlog import wrap_logger

from config import Config

logger = wrap_logger(logging.getLogger(__name__))


def get_survey_by_short_name(short_name):
    logger.debug("Attempting to find survey", short_name=short_name)

    url = f'{Config.SURVEY_SERVICE}/surveys/shortname/{short_name}'
    response = requests.get(url, auth=Config.BASIC_AUTH)

    if response.status_code == 204:
        return "No Survey"

    response.raise_for_status()

    logger.debug("Successfully found survey", short_name=short_name)
    return response.json()


def create_survey(survey_ref, short_name, long_name, legal_basis, survey_type='Business'):
    logger.info('Creating new survey',
                survey_ref=survey_ref, short_name=short_name,
                long_name=long_name, legal_basis=legal_basis,
                survey_type=survey_type)

    url = f'{Config.SURVEY_SERVICE}/surveys'

    survey_details = {
        "surveyRef": survey_ref,
        "longName": long_name,
        "shortName": short_name,
        "legalBasisRef": legal_basis,
        "surveyType": survey_type
    }

    response = requests.post(url, json=survey_details, auth=Config.BASIC_AUTH)

    response.raise_for_status()

    response_json = response.json()

    create_classifiers(response_json['id'])

    logger.info("Successfully created survey", short_name=short_name)

    return response_json


def create_classifiers(survey_id):
    logger.info('Creating classifiers', survey_id=survey_id)

    url = f'{Config.SURVEY_SERVICE}/surveys/{survey_id}/classifiers'

    classifier_details = {
        "name": 'COLLECTION_INSTRUMENT',
        "classifierTypes": ['COLLECTION_EXERCISE']
    }

    response = requests.post(url, json=classifier_details, auth=Config.BASIC_AUTH)

    response.raise_for_status()

    logger.info("Classifier created", classifier_details=classifier_details, survey_id=survey_id)

    return response.json()
