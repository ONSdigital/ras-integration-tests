from behave import given
from controllers.case_controller import get_case_by_iac


@given('a social survey exists')
def create_social_survey(context):
    context.case = get_case_by_iac(context.iac)
