from behave import given, when, then

from acceptance_tests.features.pages import collection_exercise_details


@given('the 201803 collection exercise for the QIFDI survey has been created')
def qifdi_201803_exists(_):
    pass


@when('the internal user navigates to the collection exercise details page for QIFDI 201803')
def internal_user_views_collection_exercise(_):
    collection_exercise_details.go_to('QIFDI', '201803')


@when('the internal user selects a non xlsx file')
def internal_user_selects_non_xlsx_file(_):
    collection_exercise_details.select_wrong_file_type('resources/collection_instrument_files/wrong_ci_type.html')


@when('the internal user loads a non xlsx file')
def internal_user_uploads_non_xlsx_file(_):
    collection_exercise_details.load_collection_instrument('resources/collection_instrument_files/wrong_ci_type.html')


@then('the user is able to load the collection instruments')
def load_collection_instruments(_):
    collection_exercise_details.load_collection_instrument(
        test_file='resources/collection_instrument_files/064_201803_0001.xlsx')
    success_text = collection_exercise_details.get_success_panel_text()
    assert success_text == 'Collection instrument loaded'


@then('an error message is displayed to the user')
def incorrect_file_type_message_shown(_):
    error_text = collection_exercise_details.get_collection_instrument_error_text()
    assert error_text == "Incorrect file type. Please choose a file type XLSX"


@then('an error message is displayed to the user at the top of the screen')
def incorrect_file_type_message_shown_at_top(_):
    error_text = collection_exercise_details.get_error_header()
    assert error_text == "Error: wrong file type for collection instrument"
