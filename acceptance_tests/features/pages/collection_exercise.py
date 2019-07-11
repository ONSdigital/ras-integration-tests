from functools import partial

from acceptance_tests import browser
from config import Config

from common.browser_utilities import wait_for, wait_for_element_by_id, wait_for_url_matches
from logging import getLogger
from structlog import wrap_logger

logger = wrap_logger(getLogger(__name__))


def _is_state(first_state, second_state):
    return first_state.lower() == second_state.lower()


is_created = partial(_is_state, second_state='Created')
is_scheduled = partial(_is_state, second_state='Scheduled')
is_ready_for_review = partial(_is_state, second_state='Ready for review')
is_setting_ready_for_live = partial(_is_state, second_state='Setting ready for live')
is_ready_for_live = partial(_is_state, second_state='Ready for live')
is_live = partial(_is_state, second_state='Live')


def go_to(survey):
    target_url = f'{Config.RESPONSE_OPERATIONS_UI}/surveys/{survey}'
    logger.info(f'at {browser.url} and about to go to {target_url}')

    browser.visit(target_url)
    wait_for_url_matches(target_url, timeout=10, retry=1, post_change_delay=0.5)


def get_page_title():
    return browser.title


def get_survey_attributes():
    target_url = 'survey-attributes'
    wait_for_element_by_id(target_url, timeout=5, retry=1)
    survey_data = browser.find_by_id(target_url).first
    survey_attributes = {
        'survey_id': survey_data.find_by_name('survey-id').value,
        'survey_title': survey_data.find_by_name('survey-title').value,
        'survey_abbreviation': survey_data.find_by_name('survey-abbreviation').value,
        'survey_legal_basis': survey_data.find_by_name('survey-legal-basis').value,
    }
    return survey_attributes


def get_row_attributes(row):
    return {
        'exercise_ref': row.find_by_name('tbl-ce-period').value,
        'user_description': row.find_by_name('tbl-ce-shown-as').value,
        'state': row.find_by_name('tbl-ce-status').value,
    }


def get_collection_exercises():
    return [get_row_attributes(row) for row in get_table_rows()]


def get_table():
    wait_for_element_by_id('tbl-collection-exercise', timeout=5, retry=1)
    return browser.find_by_id('tbl-collection-exercise').first


def get_table_headers():
    return get_table().find_by_tag('thead').value


def get_table_rows():
    return get_table().find_by_tag('tbody').find_by_tag('tr')


def get_table_row_by_period(period):
    wait_for(get_collection_exercises, 16, 2)
    for row in get_collection_exercises():
        if row['exercise_ref'] == period:
            return row


def click_ce_link(period):
    link = browser.find_by_name(f'ce-link-{period}')
    link.click()


def click_create_ce_link():
    link = browser.find_by_id('create-collection-exercise')
    link.click()


def get_collection_exercise_created_banner():
    return browser.find_by_id('newly_created_ce_link').text


def click_collection_exercise_created_banner():
    link = browser.find_by_id('newly_created_ce_link')
    link.click()
