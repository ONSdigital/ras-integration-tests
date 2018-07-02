import logging

import requests
from structlog import wrap_logger

from config import Config


logger = wrap_logger(logging.getLogger(__name__))


def get_iac(iac):
    logger.debug('Retrieving iac', iac=iac)
    response = requests.get(f'{Config.IAC_SERVICE}/iacs/{iac}', auth=Config.BASIC_AUTH)
    response.raise_for_status()
    logger.debug('Successfully retrieved iac', iac=iac)
    return response.json()
