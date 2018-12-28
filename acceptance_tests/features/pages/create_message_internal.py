from acceptance_tests import browser
from acceptance_tests.features.pages.reporting_unit import click_data_panel
from config import Config


def go_to(context):
    browser.visit(f'{Config.RESPONSE_OPERATIONS_UI}'
                  "/reporting-units/"
                  f"{context.short_name}")
    click_data_panel(context.short_name)
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


def found_respondent_details(context):
    return {'ru_ref': context.short_name,
            'to': 'first_name last_name'}


def get_subject_and_body():
    form_text_fields = browser.find_by_id("create-message-form").first
    form_text_field_attributes = {'subject': form_text_fields.find_by_id('secure-message-subject').value,
                                  'body': form_text_fields.find_by_id('secure-message-body').value}
    return form_text_field_attributes


def click_message_send_button():
    browser.find_by_id('btn-send-message').click()


def click_cancel_button():
    browser.find_by_id('btn-cancel').click()


def click_back_lnk():
    browser.find_by_id('back-link').click()


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


def click_close_conversation_button():
    browser.find_by_id('btn-close-conversation').click()


def click_confirm_close_conversation_button():
    browser.driver.find_element_by_xpath("//*[@class='btn u-mt-m']").click()


def click_reopen_conversation_button():
    browser.find_by_id('btn-reopen-conversation').click()
