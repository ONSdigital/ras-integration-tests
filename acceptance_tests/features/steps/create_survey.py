import logging

from behave import given, when, then

from acceptance_tests import browser
from acceptance_tests.features.pages import create_survey_form, survey
from structlog import wrap_logger

logger = wrap_logger(logging.getLogger(__name__))


@given('the internal user has entered the create survey URL')
def check_user_on_survey_create_page(_):
    survey.go_to_create()
    expected_title = "Create survey"
    assert expected_title in browser.title, "Unexpected page title {} ({} expected)".format(browser.title,
                                                                                            expected_title)


@when('they enter the new survey details')
def create_survey_details(_):
    create_survey_form.edit_survey_ref('9999')
    create_survey_form.edit_short_name('CREATE')
    create_survey_form.edit_long_name('Test Survey')
    create_survey_form.edit_legal_basis('STA1947')

    create_survey_form.click_save()


@then('they can view the newly created survey details')
def view_updated_survey_details(context):
    expected_title = "Surveys | Survey Data Collection"
    assert expected_title in browser.title, "Unexpected page title {} ({} expected)".format(browser.title,
                                                                                            expected_title)
    surveys = survey.get_surveys()

    for row in context.table:
        matching = filter(lambda s: s['id'] == row['survey_id'], surveys)
        assert len(list(matching)) > 0, "Failed to find survey with ref {}".format(row['survey_id'])
        survey_by_id = next(matching)

        test_data = row['survey_id']
        assert survey_by_id['id'] == test_data, "Unexpected survey id {} ({} expected)".format(survey_by_id['id'],
                                                                                               test_data)
        test_data = row['survey_title']
        assert survey_by_id['name'] == test_data, "Unexpected survey name {} ({} expected)".format(survey_by_id['id'],
                                                                                                   test_data)
        test_data = row['survey_abbreviation']
        assert survey_by_id['short_name'] == test_data, "Unexpected survey id {} ({} expected)".format(
            survey_by_id['short_name'], test_data)
        test_data = row['survey_legal_basis']
        assert survey_by_id['legal_basis'] == test_data, "Unexpected survey legal basis {} ({} expected)".format(
            survey_by_id['legal_basis'], test_data)
