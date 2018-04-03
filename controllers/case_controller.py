import json
import logging

import requests
from structlog import wrap_logger

from config import Config

logger = wrap_logger(logging.getLogger(__name__))


def post_case_event(case_id, party_uuid, category, description):
    logger.debug('Post case event')

    url = f'{Config.CASE_SERVICE}/cases/{case_id}/events'
    payload = {
        'description': description,
        'category': category,
        'partyId': party_uuid,
        'createdBy': 'TESTS'
    }
    response = requests.post(url, json=payload, auth=Config.BASIC_AUTH)
    if response.status_code != 201:
        logger.error('Failed to post case event', status=response.status_code)

    return json.loads(response.text)


def generate_new_enrolment_code(collection_exercise_id, ru_ref):
    logger.debug('Generating new enrolment code', collection_exercise_id=collection_exercise_id, ru_ref=ru_ref)
    url = f'{Config.CASE_SERVICE}/cases/iac/{collection_exercise_id}/{ru_ref}'
    response = requests.post(url, auth=Config.BASIC_AUTH)
    response.raise_for_status()
    logger.debug('Successfully generated new enrolment code',
                 collection_exercise_id=collection_exercise_id, ru_ref=ru_ref)
    return response.json()
