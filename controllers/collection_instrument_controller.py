import json
import logging

import requests
from structlog import wrap_logger

from config import Config


logger = wrap_logger(logging.getLogger(__name__))


def upload_seft_collection_instrument(collection_exercise_id, file_path):
    logger.info('Uploading SEFT collection instrument', collection_exercise_id=collection_exercise_id)
    url = f'{Config.COLLECTION_INSTRUMENT_SERVICE}/' \
          f'collection-instrument-api/1.0.2/upload/{collection_exercise_id}'
    mimetype = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    files = {"file": ('test_collection_instrument.xlxs', open(file_path, 'rb'), mimetype)}
    response = requests.post(url=url, auth=Config.BASIC_AUTH, files=files)
    response.raise_for_status()
    logger.info('Successfully uploaded collection instrument', collection_exercise_id=collection_exercise_id)


def upload_eq_collection_instrument(survey_id, form_type, eq_id):
    logger.info('Uploading eQ collection instrument', survey_id=survey_id, form_type=form_type)
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
    logger.info('Successfully uploaded eQ collection instrument', survey_id=survey_id, form_type=form_type)
