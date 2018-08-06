import logging
from datetime import timedelta, datetime

import paramiko
from behave import given, when, then
from retrying import retry
from structlog import wrap_logger

from acceptance_tests.features.environment import poll_database_for_iac
from config import Config
from controllers.collection_exercise_controller import create_and_execute_collection_exercise

logger = wrap_logger(logging.getLogger(__name__))


@given('a reporting unit has been enrolled in a survey')
def reporting_unit_enrolled(context):
    now = datetime.utcnow()
    context.start = datetime.now()
    dates = {
        "mps": now + timedelta(seconds=5),
        "go_live": now + timedelta(seconds=10),
        "return_by": now + timedelta(days=10),
        "exercise_end": now + timedelta(days=11),
    }
    # Create action rule
    create_and_execute_collection_exercise('cb8accda-6118-4d3b-85a3-149e28960c54', '0718', 'Testing notification file',
                                           dates, short_name='Bricks')


@when('the survey goes live')
def survey_is_live(context):
    context.iac_code = poll_database_for_iac('cb8accda-6118-4d3b-85a3-149e28960c54', '0718')


@then('the reporting unit will receive a letter')
def letter_is_received(context):
    content = get_file_after_time(context.start)
    assert context.iac_code in content, content


def get_file_after_time(start_of_test):
    logger.info('Connecting to SFTP')
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=Config.SFTP_HOST,
                port=int(Config.SFTP_PORT),
                username=Config.SFTP_USERNAME,
                password=Config.SFTP_PASSWORD)
    with ssh.open_sftp() as client:
        return retrying_get_file_after_time(client, start_of_test)


@retry(retry_on_result=lambda r: not r, wait_fixed=1000, stop_max_delay=120000)
def retrying_get_file_after_time(client, start_of_test):
    logger.info('Loading file from SFTP')
    files = client.listdir_attr(Config.SFTP_DIR)
    files = sorted(files, key=lambda f: f.st_mtime, reverse=True)
    if not files:
        return None

    latest_file_attributes = files[0]
    with client.open(f'{Config.SFTP_DIR}/{latest_file_attributes.filename}') as latest_file:
        start_of_test = round_to_minute(start_of_test) # SFTP time is only accurate to the minute
        return str(latest_file.read()) if datetime.fromtimestamp(
            latest_file_attributes.st_mtime) >= start_of_test else None


def round_to_minute(start_of_test):
    return datetime(start_of_test.year, start_of_test.month, start_of_test.day, start_of_test.hour,
                    start_of_test.minute, second=0, microsecond=0)
