import logging

import requests
from structlog import wrap_logger

from config import Config


logger = wrap_logger(logging.getLogger(__name__))


def reset_database(sql_script_file_path):
    logger.debug('Executing SQL script', file_path=sql_script_file_path)
    url = Config.CF_DATABASE_TOOL + '/sql'
    headers = {
        'Content-Type': 'text/plain'
    }
    with open(sql_script_file_path, 'r') as sqlScriptFile:
        sql_script = sqlScriptFile.read().replace('\n', '')

    response = requests.post(url, auth=Config.BASIC_AUTH, headers=headers, data=sql_script)

    if response.status_code != 201:
        logger.error('Database reset failed', status=response.status_code)

    logger.debug('Database is successfully reset')
    return response.text
