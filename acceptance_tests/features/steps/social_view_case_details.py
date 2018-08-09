from behave import given, when, then

from acceptance_tests.features.pages import social_view_case_details
from common.social_survey_setup import create_social_survey_cases


@given("a social survey case exists")
def create_social_survey(context):
    context.survey = create_social_survey_cases(context)


# TODO implement other steps once UI completed


@then('They can see all the above case details')
def internal_sel_user_can_view_social_case_details(context):
    social_view_case_details.go_to()
    actual_social_ref_number = social_view_case_details.get_reference_number()
    actual_social_status = social_view_case_details.get_status()
    actual_social_address = social_view_case_details.get_address()

    assert context.social_ref_number == actual_social_ref_number
    assert context.social_status == actual_social_status
    assert context.social_address['prem1'] == actual_social_address
