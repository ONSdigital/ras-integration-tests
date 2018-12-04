import time
from datetime import datetime, timedelta

from acceptance_tests import browser


def is_text_present_with_retry(text, retries=3, delay=1):
    for attempt in range(retries):
        if browser.is_text_present(text, wait_time=delay):
            return True
        browser.reload()
    return False


def wait_for(fn, timeout_secs, retry_secs=3.0):
    """run function multiple times within a timeout window until it returns a truthy value
    Not done as a decorator as fn could be called from several places"""

    ret_val = None
    timeout = datetime.utcnow() + timedelta(seconds=timeout_secs)

    while not ret_val and datetime.utcnow() < timeout:
        ret_val = fn()
        if not ret_val:
            time.sleep(retry_secs)
    return ret_val
