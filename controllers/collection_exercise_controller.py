import json
import logging

import requests
from structlog import wrap_logger

from config import Config


logger = wrap_logger(logging.getLogger(__name__))


def execute_collection_exercise(survey_id, period):
    url = f'{Config.COLLECTION_EXERCISE}/collectionexercises/survey/{survey_id}'
    response = requests.get(url=url, auth=Config.BASIC_AUTH)
    collection_exercises = json.loads(response.text)
    for collection_exercise in collection_exercises:
        if collection_exercise['exerciseRef'] == period:
            collection_exercise_id = collection_exercise['id']
            url = Config.COLLECTION_EXERCISE + '/collectionexerciseexecution/' + collection_exercise_id
            response = requests.post(url=url, auth=Config.BASIC_AUTH)

            if response.status_code != 200:
                logger.error('Failed to post collection exercise execution', status=response.status_code)

            logger.info('Exercises execution process finished')


def get_collection_exercise(survey_id, exercise_ref):
    logger.info('Retrieving collection exercises', survey_id=survey_id, exercise_ref=exercise_ref)
    url = f'{Config.COLLECTION_EXERCISE}/collectionexercises/survey/{survey_id}'
    response = requests.get(url=url, auth=Config.BASIC_AUTH)
    response.raise_for_status()
    collection_exercises = response.json()
    for ce in collection_exercises:
        if ce['exerciseRef'] == exercise_ref:
            collection_exercise = ce
            break
    else:
        raise Exception(f'No collection exercise found with exerciseRef {exercise_ref}')
    logger.info('Successfully retrieved collection exercises', survey_id=survey_id, exercise_ref=exercise_ref)
    return collection_exercise
