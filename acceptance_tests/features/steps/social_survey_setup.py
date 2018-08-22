from behave import given

from common.social_survey_setup import create_social_survey_cases


@given('a social survey exists')
def create_social_survey(context):
    context.social_iac = create_social_survey_cases(context)