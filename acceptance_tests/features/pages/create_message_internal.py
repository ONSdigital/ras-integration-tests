from acceptance_tests import browser
from common.respondent_details import RESPONDENT_DETAILS
from config import Config


def go_to():
    browser.visit(f'{Config.RESPONSE_OPERATIONS_UI}'
                  "/reporting-units/"
                  f"{RESPONDENT_DETAILS.get_ru_ref()}")
    browser.find_by_id("create-message-button-1").click()
    assert "messages/create-message" in browser.url


def get_ru_details_attributes():
    ru_details_table = browser.find_by_id("create-message-form").first
    ru_details_table_attributes = {'survey': ru_details_table.find_by_id('hidden_survey').value,
                                   'ru_ref': ru_details_table.find_by_id('hidden_ru_ref').value,
                                   'business': ru_details_table.find_by_id('hidden_business').value,
                                   'to': ru_details_table.find_by_id('hidden_to').value,
                                   'to_uuid': ru_details_table.find_by_id('hidden_to_uuid').value,
                                   'to_ru_id': ru_details_table.find_by_id('hidden_to_ru_id').value}
    return ru_details_table_attributes


def found_respondent_details():
    return {'ru_ref': RESPONDENT_DETAILS.get_ru_ref(),
            'to': 'first_name last_name',
            'to_uuid': RESPONDENT_DETAILS.get_respondent_id(),
            'to_ru_id': RESPONDENT_DETAILS.get_ru_id()}


def get_subject_and_body():
    form_text_fields = browser.find_by_id("create-message-form").first
    form_text_field_attributes = {'subject': form_text_fields.find_by_id('secure-message-subject').value,
                                  'body': form_text_fields.find_by_id('secure-message-body').value}
    return form_text_field_attributes


def click_message_send_button():
    browser.find_by_id('btn-send-message').click()


def click_cancel_button():
    browser.find_by_id('btn-cancel').click()


def enter_text_in_message_subject(text):
    browser.driver.find_element_by_id('secure-message-subject').send_keys(text)


def enter_text_in_message_body(text):
    browser.driver.find_element_by_id('secure-message-body').send_keys(text)


def enter_text_in_message_body_with_javascript(text):
    browser.execute_script(f'document.getElementById("secure-message-body").value="{text}";')


def get_message_subject_text():
    return get_subject_and_body().get('subject')


def get_message_body_text():
    return get_subject_and_body().get('body')


def clear_message_subject_text():
    browser.driver.find_element_by_id('secure-message-subject').clear()


def clear_message_body_text():
    browser.driver.find_element_by_id('secure-message-body').clear()


def get_first_flashed_message():
    return browser.find_by_id("flashed-message-1").value
