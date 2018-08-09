from datetime import datetime, timedelta
from logging import getLogger
from uuid import uuid4
from random import randint

from behave import given, when
from structlog import wrap_logger

from controllers.collection_exercise_controller import create_and_execute_collection_exercise
from controllers.survey_controller import create_survey, create_classifiers

logger = wrap_logger(getLogger(__name__))


def create_social_survey_cases(context):

    test_unique_id = str(randint(100000, 200000))

    # Create unique survey
    context.test_unique_id = test_unique_id

    survey_short_name = f'ShortName-' + test_unique_id
    survey_long_name = f'LongName-' + test_unique_id
    survey_legal_basis = 'Vol'
    survey_type = 'Social'

    context.survey_name = survey_long_name

    response = create_survey(survey_ref=test_unique_id, short_name=survey_short_name, long_name=survey_long_name,
                             legal_basis=survey_legal_basis, survey_type=survey_type)
    survey_id = response['id']

    create_classifiers(survey_id)

    period = '1'

    user_description = 'UserDescription-' + test_unique_id
    dates = generate_collection_exercise_dates()

    return create_and_execute_collection_exercise(survey_id, period, user_description, dates, social='social')


def generate_collection_exercise_dates():
    """Generates and returns collection exercise dates."""

    now = datetime.utcnow()

    dates = {
        'mps': now + timedelta(seconds=5),
        'go_live': now + timedelta(minutes=1),
        'return_by': now + timedelta(days=10),
        'exercise_end': now + timedelta(days=11)
    }

    return dates
