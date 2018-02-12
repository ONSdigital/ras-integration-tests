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
