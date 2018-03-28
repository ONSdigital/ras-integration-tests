import logging
from os.path import abspath

import requests
from structlog import wrap_logger

from acceptance_tests import browser
from config import Config


logger = wrap_logger(logging.getLogger(__name__))


def load_sample(survey_name, period, test_file):
    browser.visit(f'{Config.RESPONSE_OPERATIONS_UI}/surveys/{survey_name}/{period}')
    browser.driver.find_element_by_id('sampleFile').send_keys(abspath(test_file))
    browser.driver.find_element_by_id('btn-load-sample').click()


def upload_sample(collection_exercise_id, file_path):
    logger.info('Uploading sample file',
                collection_exercise_id=collection_exercise_id, sample_file=file_path)
    url = f'{Config.SAMPLE_SERVICE}/samples/B/fileupload'
    files = {"file": ('test_sample_file.xlxs', open(file_path, 'rb'), 'text/csv')}

    response = requests.post(url=url, auth=Config.BASIC_AUTH, files=files)

    # Sample service *should* return something other than 201 when upload / ingest fails
    if response.status_code != 201:
        logger.error('Error uploading sample file',
                     collection_exercise_id=collection_exercise_id, status=response.status_code)
        raise Exception('Failed to upload sample')

    response_json = response.json()
    logger.info('Successfully uploaded sample file',
                collection_exercise_id=collection_exercise_id, sample_file=file_path)
    return response_json
