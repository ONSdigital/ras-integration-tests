import logging

import requests
from structlog import wrap_logger

from config import Config

logger = wrap_logger(logging.getLogger(__name__))


def get_survey_by_short_name(short_name):
    logger.debug("Attempting to find survey", short_name=short_name)

    url = f'{Config.SURVEY_SERVICE}/surveys/shortname/{short_name}'
    response = requests.get(url, auth=Config.BASIC_AUTH)

    if response.status_code == 204:
        return "No Survey"

    response.raise_for_status()

    logger.debug("Successfully found survey", short_name=short_name)
    return response.json()
