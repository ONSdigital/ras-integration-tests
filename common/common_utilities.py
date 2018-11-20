import signal
from datetime import datetime

import psutil
from psutil import NoSuchProcess


def create_utc_timestamp():
    return datetime.utcnow().strftime('%Y-%m-%d-%H-%M-%S-%f')


def compact_string(string_in, max_length):
    string_out = string_in

    # Retain as much of the string as possible, init cap all words, remove spaces and truncate if necessary
    if len(string_in) > max_length:
        string_out = string_out.title()
        string_out = string_out.replace(' ', '')

        if len(string_out) > max_length:
            string_out = string_out[:max_length]

    return string_out


def concatenate_strings(left_part, right_part, separator=''):
    return left_part + separator + right_part


def create_behave_tags(tags):
    behave_tags = ''

    for t in tags.split(' '):
        behave_tags += f' --tags={t}'

    return behave_tags


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
