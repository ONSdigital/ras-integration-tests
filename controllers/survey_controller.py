import logging

import requests
from structlog import wrap_logger

from config import Config


logger = wrap_logger(logging.getLogger(__name__))


def get_survey_by_shortname(short_name):
    logger.debug('Retrieving survey', short_name=short_name)

    url = f'{Config.SURVEY_SERVICE}/surveys/shortname/{short_name}'
    response = requests.get(url, auth=Config.BASIC_AUTH)
    response.raise_for_status()

    logger.debug('Successfully retrieved survey', short_name=short_name)
    return response.json()
