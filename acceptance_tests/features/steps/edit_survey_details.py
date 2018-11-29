from behave import given, when, then

from acceptance_tests import browser
from acceptance_tests.features.pages import edit_survey_details_form, survey
from common.survey_utilities import create_data_for_survey


@given('the internal user is on the survey list page')
def check_user_on_surveys_page(_):
    survey.go_to()
    assert "Surveys | Survey Data Collection" in browser.title


@when('they request to edit/amend a specific surveys details')
def user_clicks_to_edit_survey_details_page_for_survey_in_context(context):
    btn_id = f"edit-survey-details-{context.survey_ref}"
    browser.click_link_by_id(btn_id)


@when('they edit/amend the survey details')
def edit_survey_details(context):
    survey_data = create_data_for_survey(context)
    short_name = survey_data['short_name']
    long_name = survey_data['long_name']

    edit_survey_details_form.edit_short_name(short_name)
    edit_survey_details_form.edit_long_name(long_name)

    context.expected_short_name = short_name
    context.expected_long_name = long_name

    edit_survey_details_form.click_save()


@then('the survey details match the updated values')
def survey_survey_details_match_updated_values(context):
    surveys = survey.get_surveys()
    test_survey = next(filter(lambda s: s['id'] == context.survey_ref, surveys))
    assert test_survey['short_name'] == context.expected_short_name
    assert test_survey['name'] == context.expected_long_name
