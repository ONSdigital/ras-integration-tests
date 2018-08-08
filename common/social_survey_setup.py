from logging import getLogger
from uuid import uuid4

from behave import given
from structlog import wrap_logger

from controllers.survey_controller import create_survey

logger = wrap_logger(getLogger(__name__))


@given("a social survey case exists")
def create_social_survey_cases(context):

    test_unique_id = str(uuid4())

    # Create unique survey
    context.test_unique_id = test_unique_id

    survey_short_name = f'ShortName-{test_unique_id}'
    survey_long_name = f'LongName-{test_unique_id}'
    survey_legal_basis = 'Vol'
    survey_type = 'Social'

    context.survey_name = survey_long_name

    response = create_survey(survey_ref=test_unique_id, short_name=survey_short_name, long_name=survey_long_name,
                             legal_basis=survey_legal_basis, survey_type=survey_type)
    survey_id = response['id']

    # Create unique collex

    #



