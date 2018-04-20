from behave import given, when, then

from acceptance_tests.features.pages import collection_exercise_details
from common.browser_utilities import is_text_present_with_retry


@given('I am on the collection exercise details screen with a loaded CI')
def ce_details_page_with_loaded_ci(_):
    collection_exercise_details.go_to('RSI', '201804')
    collection_exercise_details.load_collection_instrument(
        test_file='resources/collection_instrument_files/064_201803_0001.xlsx')


@when('I click the remove loaded SEFT CI button')
def unselect_ci(_):
    collection_exercise_details.remove_ci()


@then('The loaded SEFT CI is removed')
def ci_removed_successfully(_):
    success_text = collection_exercise_details.get_collection_instrument_removed_success_text()
    assert success_text == 'Collection instrument removed'


@when("the collection exercise state is 'ready for live'")
def ce_state_ready_for_live(_):
    sample_file = 'resources/sample_files/business-survey-sample-date.csv'
    ci_path = 'resources/collection_instrument_files/064_201803_0001.xlsx'

    collection_exercise_details.load_collection_instrument(test_file=ci_path)
    collection_exercise_details.load_sample(sample_file)

    assert is_text_present_with_retry('Ready for review', 10)

    collection_exercise_details.click_ready_for_live_and_confirm()
    collection_exercise_details.click_refresh_link_until_ready_for_live()

    assert is_text_present_with_retry('Ready for live', 10)


@then('I am not able to remove the loaded SEFT CI')
def unable_to_remove_ci(_):
    assert not collection_exercise_details.is_able_to_remove_ci()
