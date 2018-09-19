from datetime import datetime


def create_utc_timestamp():
    return datetime.utcnow().strftime('%Y-%m-%d-%H-%M-%S-%f')


def concatenate_strings(left_part, right_part, separator=''):
    return left_part + separator + right_part
