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


def upload_sample(collection_exercise_id, file, social=False, file_as_string=False):
    logger.info('Uploading sample file',
                collection_exercise_id=collection_exercise_id, sample_file=file)
    if social:
        sample_type = "SOCIAL"
    else:
        sample_type = "B"

    url = f'{Config.SAMPLE_SERVICE}/samples/{sample_type}/fileupload'
    if file_as_string:
        files = {"file": ('test_sample_file.xlxs', file.encode('utf-8'), 'text/csv')}
    else:
        files = {"file": ('test_sample_file.xlxs', open(file, 'rb'), 'text/csv')}

    response = requests.post(url=url, auth=Config.BASIC_AUTH, files=files)

    # Sample service *should* return something other than 201 when upload / ingest fails
    if response.status_code != 201:
        logger.error('Error uploading sample file',
                     collection_exercise_id=collection_exercise_id, status=response.status_code)
        raise Exception('Failed to upload sample')

    response_json = response.json()
    logger.info('Successfully uploaded sample file',
                collection_exercise_id=collection_exercise_id, sample_file=file)
    return response_json


def upload_unique_sample(collection_exercise_id, ru_ref, social=False):
    logger.info('Uploading sample file',
                collection_exercise_id=collection_exercise_id, ru_ref=ru_ref)
    if social:
        sample_type = "SOCIAL"
    else:
        sample_type = "B"

    url = f'{Config.SAMPLE_SERVICE}/samples/{sample_type}/fileupload'

    unique_sample = ru_ref + ':F:50300:50300:45320:45320:8478:801325:9900000576:1:E:FE:24/01/2017:RED BRICKS LTD:::' \
                             'RED BRICKS LTD::::::C:D:7:0001:S'
    files = {"file": ('test_sample_file.xlxs', unique_sample, 'text/csv')}

    response = requests.post(url=url, auth=Config.BASIC_AUTH, files=files)

    # Sample service *should* return something other than 201 when upload / ingest fails
    if response.status_code != 201:
        logger.error('Error uploading unique sample',
                     collection_exercise_id=collection_exercise_id, status=response.status_code)
        raise Exception('Failed to upload unique sample')

    response_json = response.json()
    logger.info('Successfully uploaded unique sample',
                collection_exercise_id=collection_exercise_id, sample_file=ru_ref)

    upload_response = {
        'ru_ref': ru_ref,
        'upload_response': response_json
    }

    return upload_response
