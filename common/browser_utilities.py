import time
from datetime import datetime, timedelta

from acceptance_tests import browser


def is_text_present_with_retry(text, retries=3, delay=1):
    for attempt in range(retries):
        if browser.is_text_present(text, wait_time=delay):
            return True
        browser.reload()
    return False


def wait_for_element_by_name(name, timeout, retry):
    """Waits for the named element to appear on the page

    Parameters:
        name (string): The name of the element to wait for
        timeout (int): Total amount of time in seconds to wait before returning a default of False
        retry (int): Time in seconds after one attempt to check if element is on the screen.

    Returns:
        boolean: True if element found else False
        """
    return wait_for(_named_element_on_page, timeout, retry, name)


def wait_for_element_by_id(element_id, timeout, retry):
    """Waits for the element with the specific id to appear on the page

    Parameters:

        element_id (string): The id of the element to wait for
        timeout (int): Total amount of time in seconds to wait before returning a default of False
        retry (int): Time in seconds after one attempt to check if element is on the screen.

    Returns:
        boolean: True if element found else False
    """
    return wait_for(_element_by_id_on_page, timeout, retry, element_id)


def wait_for(fn, timeout, retry_after, *argv):
    """run function multiple times within a timeout window until it returns a truthy value
    Not done as a decorator as fn could be called from several places

    Parameters :

    timeout (int): Total amount of time in seconds to wait before returning a default of False
    retry_after (int): Time in seconds after one attempt will execute function again.
    fn (function): The function that will be called should return True or False,
                   typically True indicating something on page
    *argv : Optional variable arguments to pass to fn

    Returns:
    fn return value should be Truthy or Falsy
    """

    ret_val = False
    last_timeout = datetime.utcnow() + timedelta(seconds=timeout)

    while not ret_val and datetime.utcnow() < last_timeout:
        ret_val = fn(*argv) if argv else fn()
        if not ret_val:
            time.sleep(retry_after)
    return ret_val


def _named_element_on_page(name):
    """Returns True if element of name:name is on current page, else False"""
    return True if browser.find_by_name(name) else False


def _element_by_id_on_page(element_id):
    """Returns True if element of id:element_id is on current page, else False"""
    return True if browser.find_by_id(element_id) else False
