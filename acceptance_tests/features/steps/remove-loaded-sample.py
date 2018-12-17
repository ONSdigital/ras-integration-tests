from behave import given, then, when

from acceptance_tests.features.pages import collection_exercise_details, confirm_remove_sample


@given('user on the collection exercise details screen')
@given('user has proceeded to remove loaded sample')
def check_user_is_on_collection_exercise_details_page(context):
    collection_exercise_details.go_to(context.short_name, context.period)
    collection_exercise_details.load_sample('resources/sample_files/business-survey-sample-date.csv')
    collection_exercise_details.get_sample_success_text()


@given('user wants to remove a loaded sample from a collection exercise')
def user_wants_to_remove_loaded_sample(context):
    collection_exercise_details.go_to(context.short_name, context.period)


@when('they click on remove loaded sample')
def click_on_remove_sample(_):
    collection_exercise_details.remove_sample()


@when('the loaded sample has been removed')
@when('confirm they want to proceed with the action')
def click_to_confirm_removal_of_sample(_):
    confirm_remove_sample.click_remove_sample()


@when('the collection exercise has status is ready for live')
def collection_exercise_has_hit_ready_for_live(_):
    ce_status = collection_exercise_details.get_status()
    assert ce_status == "Ready for live"


@then('they are presented with a successful sample removal message')
@then('the loaded sample is removed')
def check_sample_removed_success_message(_):
    collection_exercise_details.get_sample_removed_success_text()


@then('check sample content is displayed instead of remove loaded sample')
def check_sample_is_displayed_instead_of_remove_sample(_):
    message = collection_exercise_details.get_check_sample_contents()
    assert message == "Check sample contents"


@then('the collection exercise status will reflect the sample has been removed')
def collection_exercise_returns_to_scheduled(_):
    ce_status = collection_exercise_details.get_status()
    assert ce_status == "Scheduled"


@then('remove loaded sample must not be displayed')
def remove_sample_must_not_be_displayed(_):
    assert not collection_exercise_details.check_remove_sample()
