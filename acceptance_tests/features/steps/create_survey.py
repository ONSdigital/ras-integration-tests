import logging

from behave import given, when, then
from structlog import wrap_logger

from acceptance_tests import browser
from acceptance_tests.features.pages import create_survey_form, survey
from common.string_utilities import substitute_context_values
from common.survey_utilities import create_ru_reference

logger = wrap_logger(logging.getLogger(__name__))


@given('the internal user has entered the create survey URL')
@when('the internal user has entered the create survey URL')
def check_user_on_survey_create_page(_):
    survey.go_to_create()
    expected_title = "Create survey"
    assert expected_title in browser.title, "Unexpected page title {} ({} expected)".format(browser.title,
                                                                                            expected_title)


@given("they enter new survey details with legal basis of '{legal_basis}'")
@when("they enter new survey details with legal basis of '{legal_basis}'")
def create_new_survey_details(context, legal_basis):

    create_survey_form.edit_survey_ref(context.survey_ref)
    create_survey_form.edit_short_name(context.short_name)
    create_survey_form.edit_long_name(context.long_name)

    create_survey_form.edit_legal_basis(legal_basis)
    context.legal_basis = legal_basis
    create_survey_form.click_save()


@given("they enter new survey details with legal basis of '{legal_basis}' and new short name")
@when("they enter new survey details with legal basis of '{legal_basis}' and new short name")
def create_new_survey_details_with_new_short_name(context, legal_basis):
    context.short_name = create_ru_reference()
    create_new_survey_details(context, legal_basis)


@then('they are taken to survey list page')
def they_are_taken_to_survey_list_page(context):
    expected_title = "Surveys | Survey Data Collection"
    assert expected_title in browser.title, "Unexpected page title {} ({} expected) - possible error: {}".format(
        browser.title, expected_title, create_survey_form.save_error())


@then('the new survey information is on the page')
def the_new_survey_information_is_on_the_page(context):
    surveys = survey.get_surveys()

    matching = [s for s in surveys if s['id'] == context.survey_ref]
    assert len(matching) > 0, "Failed to find survey with ref {}".format(context.survey_id)

    # We've checked it's length is greater than zero so this is safe
    matching_survey = matching[0]

    assert matching_survey['id'] == context.survey_ref, "Unexpected survey id {} ({} expected)".\
        format(matching_survey['id'], context.survey_ref)
    assert matching_survey['name'] == context.long_name, "Unexpected survey name {} ({} expected)".\
        format(matching_survey['id'], context.long_name)
    assert matching_survey['short_name'] == context.short_name, "Unexpected survey id {} ({} expected)".\
        format(matching_survey['short_name'], context.short_name)
    assert matching_survey['legal_basis'] == context.legal_basis, "Unexpected survey legal basis {} ({} expected)".\
        format(matching_survey['legal_basis'], context.legal_basis)


@then("they get an error message of '{match_string}'")
def check_error_message_matches(context, match_string):
    actual_error_message = create_survey_form.save_error()
    expected_error_message = substitute_context_values(context, match_string)
    assert expected_error_message == actual_error_message, \
        "expected:{expected_error_message} does not match {actual_error_message}"
