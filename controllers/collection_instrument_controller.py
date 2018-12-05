import json
import logging

import requests
from structlog import wrap_logger

from config import Config

logger = wrap_logger(logging.getLogger(__name__))


def upload_seft_collection_instrument(collection_exercise_id, file_path, form_type=None):
    logger.debug('Uploading SEFT collection instrument', collection_exercise_id=collection_exercise_id)
    url = f'{Config.COLLECTION_INSTRUMENT_SERVICE}/' \
          f'collection-instrument-api/1.0.2/upload/{collection_exercise_id}'
    mimetype = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    files = {"file": ('test_collection_instrument.xlxs', open(file_path, 'rb'), mimetype)}

    params = dict()
    if form_type:
        classifiers = {
            "form_type": form_type,
        }
        params['classifiers'] = json.dumps(classifiers)

    response = requests.post(url=url, auth=Config.BASIC_AUTH, files=files, params=params)
    response.raise_for_status()
    logger.debug('Successfully uploaded collection instrument', collection_exercise_id=collection_exercise_id)


def upload_eq_collection_instrument(survey_id, form_type, eq_id):
    logger.debug('Uploading eQ collection instrument', survey_id=survey_id, form_type=form_type)
    url = f'{Config.COLLECTION_INSTRUMENT_SERVICE}/' \
          f'collection-instrument-api/1.0.2/upload'

    classifiers = {
        "form_type": form_type,
        "eq_id": eq_id
    }

    params = {
        "classifiers": json.dumps(classifiers),
        "survey_id": survey_id
    }
    response = requests.post(url=url, auth=Config.BASIC_AUTH, params=params)
    response.raise_for_status()
    logger.debug('Successfully uploaded eQ collection instrument', survey_id=survey_id, form_type=form_type)


def link_collection_instrument_to_exercise(collection_instrument_id, collection_exercise_id):
    logger.debug('Linking collection instrument to exercise',
                 collection_instrument_id=collection_instrument_id, collection_exercise_id=collection_exercise_id)
    url = f'{Config.COLLECTION_INSTRUMENT_SERVICE}/' \
          f'collection-instrument-api/1.0.2/link-exercise/{collection_instrument_id}/{collection_exercise_id}'

    response = requests.post(url=url, auth=Config.BASIC_AUTH)
    response.raise_for_status()

    logger.debug('Successfully linked collection instrument to exercise',
                 collection_instrument_id=collection_instrument_id, collection_exercise_id=collection_exercise_id)


def get_collection_instruments_by_classifier(survey_id=None, form_type=None):
    logger.debug('Retrieving collection instruments', survey_id=survey_id, form_type=form_type)
    url = f'{Config.COLLECTION_INSTRUMENT_SERVICE}/' \
          f'collection-instrument-api/1.0.2/collectioninstrument'

    classifiers = dict()

    if survey_id:
        classifiers['SURVEY_ID'] = survey_id
    if form_type:
        classifiers['form_type'] = form_type

    response = requests.get(url=url, auth=Config.BASIC_AUTH, params={'searchString': json.dumps(classifiers)})

    response.raise_for_status()

    logger.debug('Successfully retrieved collection instruments', survey_id=survey_id, form_type=form_type)
    return json.loads(response.text)


def load_and_link_eq_collection_instrument(survey_id, collection_exercise_id, form_type, eq_id):
    upload_eq_collection_instrument(survey_id, form_type, eq_id)
    collection_instrument_id = get_collection_instruments_by_classifier(survey_id, form_type)[0]['id']
    link_collection_instrument_to_exercise(collection_instrument_id, collection_exercise_id)
