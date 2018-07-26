from datetime import timedelta, datetime
from time import sleep

import paramiko
from behave import given, when, then

from acceptance_tests.features.environment import poll_database_for_iac
from config import Config
from controllers.collection_exercise_controller import create_and_execute_collection_exercise


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
    content, time = get_latest_file()
    while datetime.fromtimestamp(time) < context.start:
        content, time = get_latest_file()
        sleep(5)
    assert context.iac_code in content, content


def get_latest_file():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=Config.SFTP_HOST,
                port=int(Config.SFTP_PORT),
                username=Config.SFTP_USERNAME,
                password=Config.SFTP_PASSWORD)
    client = ssh.open_sftp()
    files = client.listdir_attr(Config.SFTP_DIR)
    files = sorted(files, key=lambda f: f.st_mtime, reverse=True)
    latest_file = client.open(f'{Config.SFTP_DIR}/{files[0].filename}')
    content = str(latest_file.read())
    client.close()
    return content, files[0].st_mtime
