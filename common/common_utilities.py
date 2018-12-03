import signal
from datetime import datetime
from distutils.util import strtobool

import psutil
from psutil import NoSuchProcess


def create_utc_timestamp():
    return datetime.utcnow().strftime('%Y-%m-%d-%H-%M-%S-%f')


def create_behave_stop_argument(stop_on_failure):
    try:
        arg = strtobool(stop_on_failure)

        if arg:
            return '--stop'
        else:
            return ''
    except ValueError:
        raise Exception(f'Invalid "stop_on_failure" value "{stop_on_failure}"')


def create_behave_show_skipped_tests_argument(show_skipped_tests):
    try:
        arg = strtobool(show_skipped_tests)

        if not arg:
            return '--no-skipped'
        else:
            return ''
    except ValueError:
        raise Exception(f'Invalid "show_skipped_tests" value "{show_skipped_tests}"')


def create_behave_log_level_argument(log_level):
    if not log_level.upper() in ('DEBUG', 'INFO', 'WARN', 'WARNING', 'ERROR', 'FATAL', 'CRITICAL'):
        raise Exception(f'Invalid "log_level" value "{log_level}"')

    return f'--logging-level {log_level.upper()}'


def create_behave_format_argument(behave_format):
    return f'--format {behave_format}'


def create_behave_tags_argument(tags):
    behave_tags = ''

    for t in tags.split(' '):
        behave_tags += f' --tags={t}'

    return behave_tags


def create_behave_acceptance_feature_directory_argument(features_directory):
    return features_directory


def get_child_processes(parent_pid):
    try:
        child_processes = psutil.Process(parent_pid).children(recursive=True)
    except NoSuchProcess:
        return

    return child_processes


def kill_all_processes(children):
    if not children:
        return

    try:
        for process in children:
            process.send_signal(signal.SIGTERM)
    except NoSuchProcess:
        pass
