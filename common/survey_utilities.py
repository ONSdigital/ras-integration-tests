from logging import getLogger
from random import randint

from structlog import wrap_logger

from common.common_utilities import create_utc_timestamp
from common.string_utilities import compact_string
from controllers import survey_controller

FIELD_SEPARATOR = '-'

SURVEY_NAME_SOCIAL_PREFIX = 'SOCIAL'
SURVEY_NAME_BUSINESS_PREFIX = 'BUSINESS'

SURVEY_REFERENCE_PREFIX = '9'
SURVEY_REFERENCE_START = 1001
SURVEY_REFERENCE_END = 99999

logger = wrap_logger(getLogger(__name__))


def is_social_survey(survey_type):
    return survey_type == 'Social'


def format_survey_name(survey_name_in, social_survey, max_field_length):
    timestamp = create_utc_timestamp()

    if social_survey:
        name = FIELD_SEPARATOR.join((SURVEY_NAME_SOCIAL_PREFIX, survey_name_in, timestamp))
    else:
        name = FIELD_SEPARATOR.join((SURVEY_NAME_BUSINESS_PREFIX, survey_name_in, timestamp))

    return compact_string(name, max_field_length)


def create_survey_reference():
    ref = str(randint(SURVEY_REFERENCE_START, SURVEY_REFERENCE_END))
    return f"{SURVEY_REFERENCE_PREFIX}{ref}"


def create_test_survey(long_name, short_name, survey_ref, survey_type, legal_basis):
    logger.debug('Creating survey', test_name=long_name)

    response = survey_controller.create_survey(survey_type=survey_type, survey_ref=survey_ref,
                                               short_name=short_name,
                                               long_name=long_name,
                                               legal_basis=legal_basis)

    survey_id = response['id']

    logger.debug('Survey created - ', survey_id=survey_id, long_name=long_name, short_name=short_name)

    return survey_id
