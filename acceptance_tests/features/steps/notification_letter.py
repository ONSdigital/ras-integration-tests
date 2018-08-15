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
                                           dates)


@when('the survey goes live')
def survey_is_live(context):
    context.iac_code = poll_database_for_iac('cb8accda-6118-4d3b-85a3-149e28960c54', '0718')


@then('the reporting unit will receive a letter')
def letter_is_received(context):
    with _get_sftp_client() as client:
        file_path = _get_path_of_latest_notification_file(client, context.start, survey_ref='074', period='0718')

        with client.open(file_path) as sftp_file:
            content = str(sftp_file.read())
            assert context.iac_code in content, content
            client.remove(file_path)  # Only delete file if test passes


def _get_sftp_client():
    logger.info('Connecting to SFTP')
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=Config.SFTP_HOST,
                port=int(Config.SFTP_PORT),
                username=Config.SFTP_USERNAME,
                password=Config.SFTP_PASSWORD,
                look_for_keys=False)
    return ssh.open_sftp()


@retry(retry_on_exception=lambda e: isinstance(e, FileNotFoundError), wait_fixed=1000, stop_max_attempt_number=120)
def _get_path_of_latest_notification_file(client, start_of_test, survey_ref, period):
    logger.info('Loading file from SFTP')
    files = _get_files_ordered_by_modified_time_desc(client)
    if not files:
        raise FileNotFoundError

    latest_file_attributes = files[0]
    filename = latest_file_attributes.filename
    if f'{survey_ref}_{period}' not in filename:
        raise FileNotFoundError

    modified_time_of_file = datetime.fromtimestamp(latest_file_attributes.st_mtime)
    start_of_test = _round_to_minute(start_of_test)  # Time on SFTP on CI is only precise to the minute
    if start_of_test > modified_time_of_file:
        raise FileNotFoundError

    return f'{Config.SFTP_DIR}/{filename}'


def _get_files_ordered_by_modified_time_desc(client):
    files = client.listdir_attr(Config.SFTP_DIR)
    files = sorted(files, key=lambda f: f.st_mtime, reverse=True)
    return files


def _round_to_minute(start_of_test):
    return datetime(start_of_test.year, start_of_test.month, start_of_test.day, start_of_test.hour,
                    start_of_test.minute, second=0, microsecond=0)
