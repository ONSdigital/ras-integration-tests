import logging

import requests
from structlog import wrap_logger

from config import Config

logger = wrap_logger(logging.getLogger(__name__))


def verify_user(email_address):
    payload = {
        'client_id': Config.OAUTH_CLIENT_ID,
        'client_secret': Config.OAUTH_CLIENT_SECRET,
        'username': email_address,
        'account_verified': 'true'
    }

    url = Config.DJANGO_SERVICE + '/api/account/create'

    response = requests.put(url, auth=(Config.OAUTH_CLIENT_ID, Config.OAUTH_CLIENT_SECRET), data=payload)

    if response.status_code != 201:
        logger.error("Unable to set the user active on the OAuth2 server", status=response.status_code)
