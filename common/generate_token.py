from itsdangerous import URLSafeTimedSerializer
from logging import getLogger

import config
from structlog import wrap_logger


logger = wrap_logger(getLogger(__name__))


def generate_email_token(email):
    secret_key = config.Config.SECRET_KEY
    email_token_salt = config.Config.EMAIL_TOKEN_SALT

    if secret_key is None or email_token_salt is None:
        msg = "SECRET_KEY or EMAIL_TOKEN_SALT are not configured."
        logger.error(msg)

    timed_serializer = URLSafeTimedSerializer(secret_key)
    return timed_serializer.dumps(email, salt=email_token_salt)
