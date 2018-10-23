from behave import given

from common.social_survey_setup import create_social_survey_cases
from controllers.case_controller import get_case_by_iac


@given('a social survey exists')
def create_social_survey(context):
    context.iac = create_social_survey_cases(context)
    context.case = get_case_by_iac(context.iac)
