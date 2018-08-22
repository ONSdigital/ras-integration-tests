from datetime import datetime, timedelta
from logging import getLogger
from random import randint

from structlog import wrap_logger

from controllers.collection_exercise_controller import create_and_execute_collection_exercise
from controllers.survey_controller import create_survey, create_classifiers


logger = wrap_logger(getLogger(__name__))


def generate_new_iac_code(context):
    """Generates and returns a unique iac code."""

    test_unique_id = str(randint(100000, 200000))

    context.test_unique_id = test_unique_id

    survey_short_name = 'ShortName-' + test_unique_id
    survey_long_name = 'LongName-' + test_unique_id
    survey_legal_basis = 'STA1947'

    context.survey_name = survey_long_name

    response = create_survey(survey_ref=test_unique_id, short_name=survey_short_name, long_name=survey_long_name,
                             legal_basis=survey_legal_basis)
    survey_id = response['id']

    logger.info('survey_id = ' + survey_id)

    create_classifiers(survey_id)

    period = '204901'

    user_description = 'UserDescription-' + test_unique_id
    dates = generate_collection_exercise_dates()

    return create_and_execute_collection_exercise(survey_id, period, user_description, dates)


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
