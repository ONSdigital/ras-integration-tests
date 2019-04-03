from logging import getLogger

from behave import given, when, then
from structlog import wrap_logger

from acceptance_tests.features.pages import collection_exercise, collection_exercise_details  # NOQA

logger = wrap_logger(getLogger(__name__))


def _get_survey_id(survey):
    return {
        'rsi': '75b19ea0-69a4-4c58-8d7f-4458c8f43f5c',
        'bricks': 'cb8accda-6118-4d3b-85a3-149e28960c54',
    }.get(survey.lower())


@given('a collection exercise is in the ready for review state')
def prepare_collection_exercises(_):
    pass


@given('the user has confirmed that the collection exercise is ready for go live')
def confirmed_ready(context):
    collection_exercise_details.go_to(context.short_name, context.period)
    collection_exercise_details.click_ready_for_live_and_confirm()
    success_text = collection_exercise_details.get_success_panel_text()
    assert success_text == 'Collection exercise executed'


@given('the user has checked the contents of the collection exercise and it is all correct')
def user_checks_ce_contents(context):
    collection_exercise_details.go_to(context.short_name, context.period)
    ce_state = collection_exercise_details.get_status()
    assert collection_exercise.is_ready_for_review(ce_state), ce_state
    assert collection_exercise_details.ready_for_live_button_exists()
    assert len(collection_exercise_details.get_collection_instruments()) > 0
    sample = collection_exercise_details.get_loaded_sample()
    assert 'Total businesses' in sample
    assert 'Collection instruments' in sample
    assert '1' in sample


@when('they navigate to the collection exercise details screen')
def navigate_to_ce(context):
    collection_exercise_details.go_to(context.short_name, context.period)


@when('they confirm that the collection exercise is ready to go live')
def set_ready_for_live(_):
    collection_exercise_details.click_ready_for_live_and_confirm()
    success_text = collection_exercise_details.get_success_panel_text()
    assert success_text == 'Collection exercise executed'


@when('they choose to set the collection exercise as ready for live')
def click_set_ready(_):
    collection_exercise_details.click_ready_for_live()


@when('the system is setting the collection exercise as ready for live')
@then('the user is informed that the collection exercise is setting as ready for live')
@then('they are to be informed that the system is setting the status as Ready for Live')
def view_ready_for_live(_):
    ce_state = collection_exercise_details.get_status()
    assert collection_exercise.is_setting_ready_for_live(ce_state), ce_state
    info_panel = collection_exercise_details.get_processing_info()
    assert 'Processing' in info_panel


@then('when refreshing the page once processing has completed, the status is changed to Ready for Live')
def refresh_ready_for_live(_):
    collection_exercise_details.click_refresh_link_until_ready_for_live()
    ce_state = collection_exercise_details.get_status()
    assert collection_exercise.is_ready_for_live(ce_state), ce_state


@then('they are asked for confirmation before continuing')
def check_confirmation(_):
    alert = collection_exercise_details.get_confirmation_alert()
    assert alert.text == "This action cannot be undone.  Press 'OK' to continue, or 'Cancel' to go back."
    alert.dismiss()


@then('the user is able to refresh the page to see if there are any updates to the status')
def able_to_refresh(_):
    collection_exercise_details.click_refresh_link()
    assert collection_exercise_details.get_status() != ''


@then('they are no longer able to change the CIs, Sample or Mandatory Event Dates')
def locked_ci_sample_events(_):
    # NB: events are not currently editable
    assert not(collection_exercise_details.ready_for_live_button_exists())
    assert not(collection_exercise_details.form_select_ci_exists())
    assert not(collection_exercise_details.form_load_ci_exists())
    assert not(collection_exercise_details.form_load_sample_exists())
