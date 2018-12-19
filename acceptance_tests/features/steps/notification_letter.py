import logging
from datetime import datetime, timedelta

import paramiko
from behave import given, when, then
from retrying import retry
from structlog import wrap_logger

from config import Config
from controllers.database_controller import get_all_iacs_for_collection_exercise

logger = wrap_logger(logging.getLogger(__name__))


@given('a reporting unit has been enrolled in a survey')
def reporting_unit_enrolled(context):
    context.start = datetime.now() + timedelta(minutes=-1)


@when('the survey goes live')
def survey_is_live(context):
    context.iac_codes = get_all_iacs_for_collection_exercise(context.collection_exercise_id)


@then('the reporting unit will receive a letter')
def letter_is_received(context):
    with _get_sftp_client() as client:
        assert _check_notification_files_have_iacs(client, context.start,
                                                   survey_ref=context.survey_ref, period=context.period,
                                                   expected_iacs=context.iac_codes),\
            "Unable to find all expected iac codes in Notification files on SFTP server"


def _get_sftp_client():
    logger.debug('Connecting to SFTP')
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=Config.SFTP_HOST,
                port=int(Config.SFTP_PORT),
                username=Config.SFTP_USERNAME,
                password=Config.SFTP_PASSWORD,
                look_for_keys=False,
                timeout=120)
    return ssh.open_sftp()


@retry(retry_on_exception=lambda e: isinstance(e, FileNotFoundError),
       wait_fixed=5000, stop_max_attempt_number=24)
def _check_notification_files_have_iacs(client, start_of_test, survey_ref, period, expected_iacs):
    logger.debug('Checking for files on SFTP server')
    files = _get_files_filtered_by_name_and_modified_time(client, survey_ref, period, start_of_test)
    if len(files) == 0:
        raise FileNotFoundError

    seen_iacs = []

    for file in files:
        file_path = f'{Config.SFTP_DIR}/{file.filename}'

        with client.open(file_path) as sftp_file:
            content = str(sftp_file.read())

            for iac in expected_iacs:
                if iac in content:
                    seen_iacs.append(iac)

    if set(seen_iacs) != set(expected_iacs):
        file_names = [f.filename for f in files]
        logger.info('Unable to find all iacs', files_found=file_names, seen_iacs=seen_iacs, expected_iacs=expected_iacs)
        raise FileNotFoundError

    return True


def _get_files_ordered_by_modified_time_desc(client):
    files = client.listdir_attr(Config.SFTP_DIR)
    files = sorted(files, key=lambda f: f.st_mtime, reverse=True)
    return files


def _get_files_filtered_by_name_and_modified_time(client, survey_ref, period, start_of_test):
    files = client.listdir_attr(Config.SFTP_DIR)
    start_of_test = _round_to_minute(start_of_test)
    files = list(filter(lambda f: f'{survey_ref}_{period}' in f.filename
                                  and start_of_test <= datetime.fromtimestamp(f.st_mtime), files))
    return files


def _round_to_minute(start_of_test):
    return datetime(start_of_test.year, start_of_test.month,
                    start_of_test.day, start_of_test.hour,
                    start_of_test.minute, second=0, microsecond=0)
