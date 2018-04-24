from behave import given, when, then

from acceptance_tests import browser
from acceptance_tests.features.pages import edit_survey_details_form, survey


@given('the internal user is on the survey list page')
def check_user_on_surveys_page(_):
    survey.go_to()
    assert "Surveys | Survey Data Collection" in browser.title


@when('they request to edit/amend a surveys details')
def user_navigates_to_edit_survey_details_page_for_nbs(_):
    survey.click_edit_survey_details_button()


@when('they edit/amend the survey details')
def edit_survey_details(_):
    edit_survey_details_form.edit_short_name('NBS_2.0')
    edit_survey_details_form.edit_long_name('National Balance Sheet 2.0')
    edit_survey_details_form.click_save()


@then('they can view the updated survey details')
def view_updated_survey_details(context):
    surveys = survey.get_surveys()

    for row in context.table:
        survey_by_id = next(filter(lambda s: s['id'] == row['survey_id'], surveys))
        assert survey_by_id['id'] == "199"
        assert survey_by_id['name'] == "National Balance Sheet 2.0"
        assert survey_by_id['short_name'] == "NBS_2.0"
        assert survey_by_id['legal_basis'] == "Voluntary Not Stated"

# This is only a temporary measure to reset the data back to the way it initalially was to allow other features to pass correctly


@then('they request to reset survey details')
@when('they request to reset survey details')
def reset_survey_details_page_for_nbs(_):
    survey.click_edit_survey_details_button()


@then('the data is reset')
def reset_survey_details(_):
    edit_survey_details_form.edit_short_name('NBS')
    edit_survey_details_form.edit_long_name('National Balance Sheet')
    edit_survey_details_form.click_save()
