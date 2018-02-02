import json
import logging
import time

import requests
from structlog import wrap_logger

from config import Config

logger = wrap_logger(logging.getLogger(__name__))


def execute_collection_exercise():
    url = Config.COLLECTION_EXERCISE + '/collectionexercises/survey/cb8accda-6118-4d3b-85a3-149e28960c54'
    response = requests.get(url=url, auth=Config.BASIC_AUTH)
    collection_exercises = json.loads(response.text)
    for collection_exercise in collection_exercises:
        if collection_exercise['exerciseRef'] == '201801':
            collection_exercise_id = collection_exercise['id']
            url = Config.COLLECTION_EXERCISE + '/collectionexerciseexecution/' + collection_exercise_id
            response = requests.post(url=url, auth=Config.BASIC_AUTH)

            if response.status_code != 200:
                logger.error('Failed to post collection exercise execution', status=response.status_code)

            logger.info('Waiting for collection exercises execution process to finish...')
            time.sleep(240)
            logger.info('Exercises execution process finished')
