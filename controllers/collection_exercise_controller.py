import logging

import requests
from structlog import wrap_logger

from config import Config


logger = wrap_logger(logging.getLogger(__name__))


def execute_collection_exercise(survey_id, period):
    logger.info('Executing collection exercise')
    collection_exercise_id = get_collection_exercise(survey_id, period)['id']

    url = f'{Config.COLLECTION_EXERCISE}/collectionexerciseexecution/{collection_exercise_id}'
    response = requests.post(url=url, auth=Config.BASIC_AUTH)
    if response.status_code != 200:
        logger.error('Failed to post collection exercise execution', status=response.status_code)
        raise Exception(f'Failed to post collection exercise {collection_exercise_id}')

    logger.info('Collection exercise executed')


def get_collection_exercise(survey_id, period):
    logger.info('Retrieving collection exercises', survey_id=survey_id, exercise_ref=period)
    url = f'{Config.COLLECTION_EXERCISE}/collectionexercises/survey/{survey_id}'
    response = requests.get(url=url, auth=Config.BASIC_AUTH)
    response.raise_for_status()
    collection_exercises = response.json()
    for ce in collection_exercises:
        if ce['exerciseRef'] == period:
            collection_exercise = ce
            break
    else:
        raise Exception(f'No collection exercise found with exerciseRef {period}')
    logger.info('Successfully retrieved collection exercises', survey_id=survey_id, exercise_ref=period)
    return collection_exercise


def get_survey_collection_exercises(survey_id):
    url = f'{Config.COLLECTION_EXERCISE}/collectionexercises/survey/{survey_id}'
    response = requests.get(url=url, auth=Config.BASIC_AUTH)
    response.raise_for_status()
    collection_exercises = response.json()

    return collection_exercises


def get_events_for_collection_exercise(survey_id, period, event_tag=None):
    collection_exercise_id = get_collection_exercise(survey_id, period)['id']
    logger.info('Getting events', collection_exercise_id=collection_exercise_id, event_tag=event_tag)

    url = f'{Config.COLLECTION_EXERCISE}/collectionexercises/{collection_exercise_id}/events/'
    if event_tag:
        url += event_tag
    response = requests.get(url, auth=Config.BASIC_AUTH)
    if not response.ok:
        logger.error('Failed to get events', status=response.status_code)
        raise Exception(f'Failed to get events {collection_exercise_id}')

    logger.info('Successfully retrieved events', collection_exercise_id=collection_exercise_id, event_tag=event_tag)
    return response.json()


def post_event_to_collection_exercise(survey_id, period, event_tag, date_str):
    collection_exercise_id = get_collection_exercise(survey_id, period)['id']
    logger.info('Adding an event', collection_exercise_id=collection_exercise_id, event_tag=event_tag)

    url = f'{Config.COLLECTION_EXERCISE}/collectionexercises/{collection_exercise_id}/events'
    post_data = {'tag': event_tag, 'timestamp': date_str}
    response = requests.post(url, auth=Config.BASIC_AUTH, json=post_data)
    # 409: event already exists, which we count as permissable for testing
    if response.status_code not in (201, 409):
        logger.error('Failed to post event', status=response.status_code)
        raise Exception(f'Failed to post event {collection_exercise_id}')

    logger.info('Event added')


def update_event_for_collection_exercise(survey_id, period, event_tag, date_str):
    collection_exercise_id = get_collection_exercise(survey_id, period)['id']
    logger.info('Updating an event', collection_exercise_id=collection_exercise_id, event_tag=event_tag)

    url = f'{Config.COLLECTION_EXERCISE}/collectionexercises/{collection_exercise_id}/events/{event_tag}'
    response = requests.put(url, auth=Config.BASIC_AUTH, data=date_str, headers={'content-type': 'text/plain'})
    # 409: event already exists, which we count as permissable for testing
    if response.status_code not in (201, 204, 409):
        logger.error('Failed to post event', status=response.status_code)
        raise Exception(f'Failed to update event {collection_exercise_id}')

    logger.info('Event updated')


def delete_collection_exercise_event(survey_id, period, event_tag):
    collection_exercise_id = get_collection_exercise(survey_id, period)['id']
    logger.info('Deleting an event', collection_exercise_id=collection_exercise_id, event_tag=event_tag)

    url = f'{Config.COLLECTION_EXERCISE}/collectionexercises/{collection_exercise_id}/events/{event_tag}'
    response = requests.delete(url, auth=Config.BASIC_AUTH)
    # 409: event already exists, which we count as permissable for testing
    if response.status_code not in (202, 204, 404):
        logger.error('Failed to delete event', status=response.status_code)
        raise Exception(f'Failed to delete event {collection_exercise_id}')

    logger.info('Event deleted')
