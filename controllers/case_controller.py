import logging

import requests
from structlog import wrap_logger

from config import Config

logger = wrap_logger(logging.getLogger(__name__))


def get_case_by_id(case_id):
    logger.debug('Retrieving case by id', case_id=case_id)
    url = f'{Config.CASE_SERVICE}/cases/{case_id}'
    response = requests.get(url, auth=Config.BASIC_AUTH)
    response.raise_for_status()
    logger.debug('Successfully retrieved case', case_id=case_id)
    return response.json()


def post_case_event(case_id, party_id, category, description):
    logger.debug('Posting case event', case_id=case_id, party_id=party_id, category=category)

    url = f'{Config.CASE_SERVICE}/cases/{case_id}/events'
    payload = {
        'description': description,
        'category': category,
        'partyId': party_id,
        'createdBy': 'TESTS'
    }
    response = requests.post(url, json=payload, auth=Config.BASIC_AUTH)
    if response.status_code != 201:
        logger.error('Failed to post case event', status=response.status_code)

    logger.debug('Successfully posted case event',
                 case_id=case_id, party_id=party_id, category=category)
    return response.json()


def generate_new_enrolment_code(collection_exercise_id, business_id):
    logger.debug('Generating new enrolment code',
                 business_id=business_id, collection_exercise_id=collection_exercise_id)

    # Have to make a few calls to retrieve the right case for posting case event
    casegroups = get_casegroups_by_party_id(business_id)
    casegroup = next(casegroup
                     for casegroup in casegroups
                     if collection_exercise_id == casegroup['collectionExerciseId'])
    cases = get_cases_by_casegroup(casegroup['id'])
    earliest_case = sorted(cases, key=lambda case: case['createdDateTime'], reverse=True)[0]

    post_case_event(earliest_case['id'],
                    business_id,
                    'GENERATE_ENROLMENT_CODE',
                    'Generate new enrolment code')

    # After posting the case event we also need to retrieve that case again to get the iac
    updated_case = get_case_by_id(earliest_case['id'])
    logger.debug('Successfully generated new enrolment code',
                 business_id=business_id, collection_exercise_id=collection_exercise_id)
    return updated_case['iac']


def get_cases_by_casegroup(casegroup_id):
    logger.debug('Retrieving cases by casegroup', casegroup_id=casegroup_id)
    url = f'{Config.CASE_SERVICE}/cases/casegroupid/{casegroup_id}'
    response = requests.get(url, auth=Config.BASIC_AUTH)
    response.raise_for_status()
    logger.debug('Successfully retrieved cases by casegroup', casegroup_id=casegroup_id)
    return response.json()


def get_casegroups_by_party_id(party_id):
    logger.debug('Retrieving casegroups for party', party_id=party_id)
    url = f'{Config.CASE_SERVICE}/casegroups/partyid/{party_id}'
    response = requests.get(url, auth=Config.BASIC_AUTH)
    response.raise_for_status()
    logger.debug('Successfully retrieved casegroups for party', party_id=party_id)
    return response.json()


def get_case_by_party_id(party_id):
    logger.debug('Retrieving cases for party', party_id=party_id)
    url = f'{Config.CASE_SERVICE}/cases/partyid/{party_id}'
    response = requests.get(url, auth=Config.BASIC_AUTH)
    response.raise_for_status()
    logger.debug('Successfully retrieved cases for party', party_id=party_id)
    return response.json()


def update_case_group_status(collection_exercise_id, ru_ref, case_group_event):
    logger.debug('Updating status', collection_exercise_id=collection_exercise_id, ru_ref=ru_ref,
                 case_group_event=case_group_event)
    url = f'{Config.CASE_SERVICE}/casegroups/transitions/{collection_exercise_id}/{ru_ref}'
    response = requests.put(url, auth=Config.BASIC_AUTH, json={'event': case_group_event})

    response.raise_for_status()
    logger.debug('Successfully updated status', collection_exercise_id=collection_exercise_id, ru_ref=ru_ref,
                 case_group_event=case_group_event)
