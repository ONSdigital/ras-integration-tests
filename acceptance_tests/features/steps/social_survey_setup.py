from behave import given

from common.social_survey_setup import create_social_survey_cases


@given('a social survey exists')
def create_social_survey(context):
    context.social_iac = create_social_survey_cases(context)


@given('the case will launch a survey')
def use_different_sample(context):
    context.sample_file_name = 'enter_uac/sample_file_survey_launcher.csv'
