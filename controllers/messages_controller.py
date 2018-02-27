import json
import jwt
import logging


import requests
from structlog import wrap_logger

from config import Config

logger = wrap_logger(logging.getLogger(__name__))


def create_message(msg_to, subject, body, ru_id):
    logger.debug('Creating secure message')

    message = {
        'msg_from': "BRES",
        'msg_to': msg_to,
        'subject': subject,
        'body': body,
        'thread_id': "",
        'collection_case': "",
        'survey': "cb0711c3-0ac8-41d3-ae0e-567e5ea1ef87",
        'ru_id': ru_id}

    url = Config.SECURE_MESSAGE_SERVICE + '/message/send'

    response = requests.post(url, headers={'Authorization': _get_jwt(), 'Content-Type': 'application/json',
                                           'Accept': 'application/json'}, json=message)

    if response.status_code != 201:
        logger.error('Failed create message', status=response.status_code)
        raise Exception('Failed create message')

    return json.loads(response.text)


def _get_jwt():
    return jwt.encode({'user': 'BRES', 'party_id': 'BRES', 'role': 'internal'}, 'testsecret', algorithm='HS256')
