import logging
import string
import time
from datetime import datetime
from random import choice, randint

import requests
from structlog import wrap_logger

import common
from config import Config
from controllers import collection_instrument_controller as ci_controller, \
    sample_controller
from controllers.action_controller import create_social_action_rule
from controllers.collection_instrument_controller import get_collection_instruments_by_classifier
from controllers.database_controller import poll_collection_exercise_until_state_changed

COLLECTION_EXERCISE_CREATED = 'CREATED'
COLLECTION_EXERCISE_SCHEDULED = 'SCHEDULED'
COLLECTION_EXERCISE_READY_FOR_REVIEW = 'READY_FOR_REVIEW'
COLLECTION_EXERCISE_READY_FOR_LIVE = 'READY_FOR_LIVE'
COLLECTION_EXERCISE_LIVE = 'LIVE'

logger = wrap_logger(logging.getLogger(__name__))


def execute_collection_exercise(survey_id, period):
    logger.debug('Executing collection exercise', survey_id=survey_id, period=period)
    collection_exercise_id = get_collection_exercise(survey_id, period)['id']

    url = f'{Config.COLLECTION_EXERCISE_SERVICE}/collectionexerciseexecution/{collection_exercise_id}'
    response = requests.post(url=url, auth=Config.BASIC_AUTH)
    if response.status_code != 200:
        logger.error('Failed to post collection exercise execution', status=response.status_code)
        raise Exception(f'Failed to post collection exercise {collection_exercise_id}')

    logger.debug('Collection exercise executed', survey_id=survey_id, period=period)


def get_collection_exercise(survey_id, period):
    logger.debug('Retrieving collection exercise', survey_id=survey_id, exercise_ref=period)
    url = f'{Config.COLLECTION_EXERCISE_SERVICE}/collectionexercises/survey/{survey_id}'
    response = requests.get(url=url, auth=Config.BASIC_AUTH)
    response.raise_for_status()
    collection_exercises = response.json()
    for ce in collection_exercises:
        if ce['exerciseRef'] == period:
            collection_exercise = ce
            break
    else:
        return None
    logger.debug('Successfully retrieved collection exercise', survey_id=survey_id, exercise_ref=period)
    return collection_exercise


def get_survey_collection_exercises(survey_id):
    logger.debug('Retrieving collection exercises', survey_id=survey_id)
    url = f'{Config.COLLECTION_EXERCISE_SERVICE}/collectionexercises/survey/{survey_id}'
    response = requests.get(url=url, auth=Config.BASIC_AUTH)
    response.raise_for_status()
    collection_exercises = response.json()
    logger.debug('Successfully retrieved collection exercises', survey_id=survey_id)
    return collection_exercises


def link_sample_summary_to_collection_exercise(collection_exercise_id, sample_summary_id):
    logger.debug('Linking sample summary to collection exercise',
                 collection_exercise_id=collection_exercise_id,
                 sample_summary_id=sample_summary_id)
    url = f'{Config.COLLECTION_EXERCISE_SERVICE}/collectionexercises/link/{collection_exercise_id}'
    payload = {'sampleSummaryIds': [str(sample_summary_id)]}
    response = requests.put(url, auth=Config.BASIC_AUTH, json=payload)

    response.raise_for_status()
    logger.debug('Successfully linked sample summary with collection exercise',
                 collection_exercise_id=collection_exercise_id,
                 sample_summary_id=sample_summary_id)
    return response.json()


def get_events_for_collection_exercise(survey_id, period, event_tag=None):
    collection_exercise_id = get_collection_exercise(survey_id, period)['id']
    logger.debug('Getting collection exercise events',
                 collection_exercise_id=collection_exercise_id, event_tag=event_tag)

    url = f'{Config.COLLECTION_EXERCISE_SERVICE}/collectionexercises/{collection_exercise_id}/events/'
    if event_tag:
        url += event_tag
    response = requests.get(url, auth=Config.BASIC_AUTH)
    if not response.ok:
        logger.error('Failed to get events', status=response.status_code)
        raise Exception(f'Failed to get events {collection_exercise_id}')

    logger.debug('Successfully retrieved events', collection_exercise_id=collection_exercise_id, event_tag=event_tag)
    return response.json()


def post_event_to_collection_exercise(collection_exercise_id, event_tag, date_str):
    logger.debug('Adding a collection exercise event',
                 collection_exercise_id=collection_exercise_id, event_tag=event_tag)

    url = f'{Config.COLLECTION_EXERCISE_SERVICE}/collectionexercises/{collection_exercise_id}/events'
    post_data = {'tag': event_tag, 'timestamp': date_str}
    response = requests.post(url, auth=Config.BASIC_AUTH, json=post_data)
    # 409: event already exists, which we count as permissable for testing
    if response.status_code not in (201, 409):
        logger.error('Failed to post event', status=response.status_code)
        raise Exception(f'Failed to post event {collection_exercise_id}')

    logger.debug('Successfully added event', collection_exercise_id=collection_exercise_id, event_tag=event_tag)


def update_event_for_collection_exercise(survey_id, period, event_tag, date_str):
    collection_exercise_id = get_collection_exercise(survey_id, period)['id']
    logger.debug('Updating an event', collection_exercise_id=collection_exercise_id, event_tag=event_tag, date=date_str)

    url = f'{Config.COLLECTION_EXERCISE_SERVICE}/collectionexercises/{collection_exercise_id}/events/{event_tag}'
    response = requests.put(url, auth=Config.BASIC_AUTH, data=date_str, headers={'content-type': 'text/plain'})
    # 409: event already exists, which we count as permissable for testing
    if response.status_code not in (201, 204, 409):
        logger.error('Failed to post event', status=response.status_code, date_str=date_str)
        raise Exception(f'Failed to update event {collection_exercise_id}')

    logger.debug('Event updated')


def delete_collection_exercise_event(survey_id, period, event_tag):
    collection_exercise_id = get_collection_exercise(survey_id, period)['id']
    logger.debug('Deleting an event', collection_exercise_id=collection_exercise_id, event_tag=event_tag)

    url = f'{Config.COLLECTION_EXERCISE_SERVICE}/collectionexercises/{collection_exercise_id}/events/{event_tag}'
    response = requests.delete(url, auth=Config.BASIC_AUTH)
    # 409: event already exists, which we count as permissable for testing
    if response.status_code not in (202, 204, 404):
        logger.error('Failed to delete event', status=response.status_code)
        raise Exception(f'Failed to delete event {collection_exercise_id}')

    logger.debug('Event deleted')


def create_collection_exercise(survey_id, period, user_description):
    logger.debug('Creating collection exercise', survey_id=survey_id, period=period)
    url = f'{Config.COLLECTION_EXERCISE_SERVICE}/collectionexercises'
    json = {
        "surveyId": survey_id,
        "exerciseRef": period,
        "userDescription": user_description
    }
    response = requests.post(url, auth=Config.BASIC_AUTH, json=json)

    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        logger.exception('Failed to create collection exercise', survey_id=survey_id, period=period)
        raise Exception(f'Failed to create collection exercise {period}')

    logger.debug('Successfully created collection exercise', survey_id=survey_id, period=period)


def create_and_execute_collection_exercise(survey_id, period, user_description, dates):
    create_collection_exercise(survey_id, period, user_description)
    collection_exercise = get_collection_exercise(survey_id, period)
    collection_exercise_id = collection_exercise['id']

    post_event_to_collection_exercise(collection_exercise_id, 'mps',
                                      convert_datetime_for_event(dates['mps']))
    post_event_to_collection_exercise(collection_exercise_id, 'go_live',
                                      convert_datetime_for_event(dates['go_live']))
    post_event_to_collection_exercise(collection_exercise_id, 'return_by',
                                      convert_datetime_for_event(dates['return_by']))
    post_event_to_collection_exercise(collection_exercise_id, 'exercise_end',
                                      convert_datetime_for_event(dates['exercise_end']))

    sample_summary = sample_controller.upload_sample(collection_exercise['id'],
                                                     'resources/sample_files/business-survey-sample-date.csv')

    link_sample_summary_to_collection_exercise(collection_exercise['id'], sample_summary['id'])

    ci_controller.upload_seft_collection_instrument(collection_exercise['id'],
                                                    'resources/collection_instrument_files/064_201803_0001.xlsx',
                                                    form_type='0001')

    poll_collection_exercise_until_state_changed(collection_exercise['id'], 'READY_FOR_REVIEW')
    execute_collection_exercise(survey_id, period)
    iac = common.collection_exercise_utilities.poll_database_for_iac(survey_id, period)

    return iac


def create_and_execute_collection_exercise_with_unique_sample(survey_id, period, user_description, dates, ru_ref,
                                                              stop_at_state, eq_ci=False):
    collection_exercise = None
    iac = None

    if stop_at_state == COLLECTION_EXERCISE_CREATED:
        collection_exercise = create_business_collection_exercise_to_created_state(survey_id, period, user_description)
    elif stop_at_state == COLLECTION_EXERCISE_SCHEDULED:
        collection_exercise = create_business_collection_exercise_to_scheduled_state(survey_id, period,
                                                                                     user_description, dates)
    elif stop_at_state == COLLECTION_EXERCISE_READY_FOR_REVIEW:
        collection_exercise = create_business_collection_exercise_to_ready_for_review_state(survey_id, period,
                                                                                            user_description, dates,
                                                                                            ru_ref, eq_ci)
    elif stop_at_state == COLLECTION_EXERCISE_READY_FOR_LIVE:
        collection_exercise = create_and_execute_business_collection_exercise_to_ready_for_live_state(survey_id, period,
                                                                                                      user_description,
                                                                                                      dates,
                                                                                                      ru_ref, eq_ci)
    elif stop_at_state == COLLECTION_EXERCISE_LIVE:
        response = create_and_execute_business_collection_exercise_to_live_state(survey_id, period,
                                                                                 user_description,
                                                                                 dates, ru_ref, eq_ci)
        collection_exercise = response['collection_exercise']
        iac = response['iac']

    return {'collection_exercise': collection_exercise,
            'iac': iac}


def create_business_collection_exercise(survey_id, period, user_description):
    create_collection_exercise(survey_id, period, user_description)

    return get_collection_exercise(survey_id, period)


def create_business_collection_exercise_to_created_state(survey_id, period, user_description):
    return create_business_collection_exercise(survey_id, period, user_description)


def create_business_collection_exercise_to_scheduled_state(survey_id, period, user_description, dates):
    collection_exercise = create_business_collection_exercise_to_created_state(survey_id, period, user_description)
    collection_exercise_id = collection_exercise['id']

    post_event_to_collection_exercise(collection_exercise_id, 'mps',
                                      convert_datetime_for_event(dates['mps']))
    post_event_to_collection_exercise(collection_exercise_id, 'go_live',
                                      convert_datetime_for_event(dates['go_live']))
    post_event_to_collection_exercise(collection_exercise_id, 'ref_period_start',
                                      convert_datetime_for_event(dates['go_live']))
    post_event_to_collection_exercise(collection_exercise_id, 'return_by',
                                      convert_datetime_for_event(dates['return_by']))
    post_event_to_collection_exercise(collection_exercise_id, 'ref_period_end',
                                      convert_datetime_for_event(dates['return_by']))
    post_event_to_collection_exercise(collection_exercise_id, 'exercise_end',
                                      convert_datetime_for_event(dates['exercise_end']))
    return collection_exercise


def create_business_collection_exercise_to_ready_for_review_state(survey_id, period, user_description, dates, ru_ref,
                                                                  eq_ci):
    collection_exercise = create_business_collection_exercise_to_scheduled_state(survey_id, period, user_description,
                                                                                 dates)
    collection_exercise_id = collection_exercise['id']

    upload_response = sample_controller.upload_unique_sample(collection_exercise_id, ru_ref)

    sample_summary = upload_response['upload_response']

    link_sample_summary_to_collection_exercise(collection_exercise_id, sample_summary['id'])

    if eq_ci:
        ci_controller.load_and_link_eq_collection_instrument(survey_id, collection_exercise_id,
                                                             form_type=ru_ref, eq_id=ru_ref)
    else:
        ci_controller.upload_seft_collection_instrument(collection_exercise['id'],
                                                        'resources/collection_instrument_files/064_201803_0001.xlsx')

    return collection_exercise


def create_and_execute_business_collection_exercise_to_ready_for_live_state(survey_id, period, user_description, dates,
                                                                            ru_ref, eq_ci):
    collection_exercise = create_business_collection_exercise_to_ready_for_review_state(survey_id, period,
                                                                                        user_description,
                                                                                        dates, ru_ref, eq_ci)
    time.sleep(5)
    execute_collection_exercise(survey_id, period)
    wait_for_collection_exercise_state(survey_id, period, COLLECTION_EXERCISE_READY_FOR_LIVE)

    return collection_exercise


def create_and_execute_business_collection_exercise_to_live_state(survey_id, period, user_description, dates, ru_ref,
                                                                  eq_ci):
    collection_exercise = create_and_execute_business_collection_exercise_to_ready_for_live_state(survey_id, period,
                                                                                                  user_description,
                                                                                                  dates,
                                                                                                  ru_ref,
                                                                                                  eq_ci)
    wait_for_collection_exercise_state(survey_id, period, 'LIVE')

    iac = common.collection_exercise_utilities.poll_database_for_iac(survey_id, period)

    return {'collection_exercise': collection_exercise,
            'iac': iac}


def create_and_execute_social_collection_exercise(context, survey_id, period, user_description, dates, short_name=None):
    create_collection_exercise(survey_id, period, user_description)
    collection_exercise = get_collection_exercise(survey_id, period)
    collection_exercise_id = collection_exercise['id']
    context.collection_exercise_id = collection_exercise_id

    post_event_to_collection_exercise(collection_exercise_id, 'mps',
                                      convert_datetime_for_event(dates['mps']))
    post_event_to_collection_exercise(collection_exercise_id, 'go_live',
                                      convert_datetime_for_event(dates['go_live']))
    post_event_to_collection_exercise(collection_exercise_id, 'return_by',
                                      convert_datetime_for_event(dates['return_by']))
    post_event_to_collection_exercise(collection_exercise_id, 'exercise_end',
                                      convert_datetime_for_event(dates['exercise_end']))

    sample_summary = sample_controller.upload_sample(collection_exercise['id'],
                                                     generate_social_sample(context=context),
                                                     social=True,
                                                     file_as_string=True)

    link_sample_summary_to_collection_exercise(collection_exercise['id'], sample_summary['id'])

    ci_controller.upload_eq_collection_instrument(survey_id=survey_id,
                                                  form_type='1', eq_id='lms')
    collection_instruments = get_collection_instruments_by_classifier(survey_id, form_type='1')
    for collection_instrument in collection_instruments:
        ci_controller.link_collection_instrument_to_exercise(collection_instrument['id'], collection_exercise['id'])

    if short_name:
        create_social_action_rule(short_name, period)

    # We are seeing intermittent test failures when executing the collex - HTTP 500
    time.sleep(5)
    execute_collection_exercise(survey_id, period)
    iac = common.collection_exercise_utilities.poll_database_for_iac(survey_id, period, social=True)

    return iac


def generate_social_sample(context) -> str:
    context.address = {
        'postcode': generate_random_postcode(),
        'reference': str(randint(1000000, 9999999)),
        'address_line1': 'Office for National Statistics',
        'address_line2': 'Cardiff Road',
        'locality': 'Gwent District',
        'town_name': 'Newport',
        'UPRN': '123456',
        'TLA': 'OHS',
        'country': 'W'

    }
    return (f'TLA,REFERENCE,COUNTRY,ORGANISATION_NAME,ADDRESS_LINE1,ADDRESS_LINE2,LOCALITY,TOWN_NAME,POSTCODE,UPRN\n'
            f'{context.address["TLA"]},'
            f'{context.address["reference"]},'
            f'{context.address["country"]},,'
            f'{context.address["address_line1"]},'
            f'{context.address["address_line2"]},'
            f'{context.address["locality"]},'
            f'{context.address["town_name"]},'
            f'{context.address["postcode"]},'
            f'{context.address["UPRN"]}')


def generate_random_postcode() -> str:
    return ''.join([choice(string.ascii_uppercase + string.digits) for _ in range(7)])


def convert_datetime_for_event(date_time):
    return datetime.strftime(date_time, '%Y-%m-%dT%H:%M:%S.000Z')


def convert_event_for_datetime(date_time):
    return datetime.strftime(date_time, '%A %d %b %Y %H:%M')


def convert_event_for_date(date_time):
    return datetime.strftime(date_time, '%A %d %b %Y')


def map_ce_status(status):
    return {
        "Completed by phone": "COMPLETED_BY_PHONE",
        "No longer required": "NO_LONGER_REQUIRED",
    }.get(status, status)


def wait_for_collection_exercise_state(survey_id, period, expected_state):
    logger.debug('Waiting for collection exercise state', survey_id=survey_id, period=period,
                 expected_state=expected_state)

    while True:
        collection_exercise = get_collection_exercise(survey_id, period)

        if collection_exercise['state'] == expected_state:
            logger.debug(f'Collection exercise is now [{expected_state}]')
            break
        time.sleep(3)
