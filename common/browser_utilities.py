import time
from datetime import datetime, timedelta

from acceptance_tests import browser
from selenium.common.exceptions import NoSuchElementException


def is_text_present_with_retry(text, retries=3, delay=1):
    for attempt in range(retries):
        if browser.is_text_present(text, wait_time=delay):
            return True
        browser.reload()
    return False


def wait_for_text_present(search_text, timeout=10, retry=1):
    """Waits for specific text in the body , returns True if found else False

    Parameters:
        search_text (string): The text to look for
        timeout (int): Total amount of time in seconds to wait before returning asserting
        retry (int): Time in seconds after one attempt to check if text is on the screen.

    Returns:
        boolean: True if element found else False
        """
    return wait_for(_text_on_page, timeout, retry, search_text)


def wait_for_text_present_with_reloads(search_text, timeout=10, retry=1, reload_count=3):
    """Waits for specific text in the body , returns True if found else asserts

    Parameters:
        search_text (string): The text to look for
        timeout (int): Total amount of time in seconds to wait before returning asserting
        retry (int): Time in seconds after one attempt to check if text is on the screen.
        reload_count (int): Maximum number of iterations of wait_for_text_present before asserting if still False

    Returns:
        boolean: True if element found else asserts
        """
    ret_val = False
    while not ret_val and reload_count > 0:
        ret_val = wait_for_text_present(search_text, timeout, retry)
        browser.reload()
        reload_count -= 1

    assert ret_val, f"text {search_text} not found on page {browser.url}"

    return ret_val


def wait_for_element_by_name(name, timeout=10, retry=1):
    """Waits for the named element to appear on the page, asserts if not present after timeout

    Parameters:
        name (string): The name of the element to wait for
        timeout (int): Total amount of time in seconds to wait before returning a default of False
        retry (int): Time in seconds after one attempt to check if element is on the screen.

    Returns:
        boolean: True if element found else asserts
        """

    ret_val = wait_for(_named_element_on_page, timeout, retry, name)

    assert ret_val, f"element named {name} not found on page {browser.url}"

    return ret_val


def wait_for_element_by_class_name(name, timeout=10, retry=1):
    """Waits for the named class to appear on the page, asserts if not present after timeout

    Parameters:
        name (string): The name of the element to wait for
        timeout (int): Total amount of time in seconds to wait before returning a default of False
        retry (int): Time in seconds after one attempt to check if element is on the screen.

    Returns:
        boolean: True if element found else asserts
        """

    ret_val = wait_for(_named_class_on_page, timeout, retry, name)

    assert ret_val, f"class name {name} not found on page {browser.url}"

    return ret_val


def wait_for_element_by_id(element_id, timeout=10, retry=1):
    """Waits for the element with the specific id to appear on the page, asserts if not present after timeout

    Parameters:

        element_id (string): The id of the element to wait for
        timeout (int): Total amount of time in seconds to wait before returning a default of False
        retry (int): Time in seconds after one attempt to check if element is on the screen.

    Returns:
        boolean: True if element found else asserts
    """
    ret_val = wait_for(_element_by_id_on_page, timeout, retry, element_id)
    assert ret_val, f"element id {element_id} not found on page {browser.url}"

    return ret_val


def wait_for(fn, timeout, retry, *argv):
    """run function multiple times within a timeout window until it returns a truthy value
    Not done as a decorator as fn could be called from several places

    Parameters :

    timeout (int): Total amount of time in seconds to wait before returning a default of False
    retry (int): Time in seconds after one attempt will execute function again.
    fn (function): The function that will be called should return True or False,
                   typically True indicating something on page
    *argv : Optional variable arguments to pass to fn

    Returns:
    fn return value should be Truthy or Falsy
    """

    ret_val = False
    last_timeout = datetime.utcnow() + timedelta(seconds=timeout)

    while not ret_val and datetime.utcnow() < last_timeout:
        try:
            ret_val = fn(*argv) if argv else fn()
        except NoSuchElementException:
            pass
        if not ret_val:
            time.sleep(retry)

    return ret_val


def _named_element_on_page(name):
    """Returns True if element of name:name is on current page, else False"""
    try:
        return True if browser.find_by_name(name) else False
    except NoSuchElementException:
        return False


def _named_class_on_page(name):
    """Returns True if class of name:name is on current page, else False"""
    try:
        browser.driver.find_element_by_class_name(name)
        return True
    except NoSuchElementException:
        return False


def _element_by_id_on_page(element_id):
    """Returns True if element of id:element_id is on current page, else False"""
    try:
        return True if browser.find_by_id(element_id) else False
    except NoSuchElementException:
        return False


def _text_on_page(search_text):
    """Returns True if text in the body of the page , else False"""
    try:
        return browser.is_text_present(search_text)
    except NoSuchElementException:
        return False


def try_wait_for_url_contains(desired_url, timeout=2, retry=1, post_change_delay=0.1):
    """ Waits for either timeout or for the url to get to a value that contains with the expected value,
    whichever comes first. If the browser gets to the url then waits a further post_change_delay
    ( intended to allow page load to complete)
    Intended to replace blind sleeps
    Uses starts with to cope with redirects around sign in pages where <some_url>/sign-in goes to <some_url> if
    useralready signed in
    Parameters :

    desired_url (str): The url we wish to get to
    timeout (int or float): Total amount of time in seconds to wait before returning a default of False
    retry (int or float): Time in seconds after one attempt will execute function again.
    post_change_delay (int or float): How long to delay after a change to allow for page load completion

    Returns:
    True if target url achieved within the time_to_wait , else False
    """

    if _does_url_contain_target(desired_url):  # If already at target then enforce post change delay
        time.sleep(post_change_delay)
        return True

    ret_val = wait_for(_does_url_contain_target, timeout, retry, desired_url)
    if ret_val:
        time.sleep(post_change_delay)

    return ret_val


def assert_url_contains(desired_url, timeout=2, retry=1, post_change_delay=0.1):
    """Waits for url to contain a desired string, for up to the timeout, asserts if it does not do this """
    assert try_wait_for_url_contains(desired_url=desired_url,
                                     timeout=timeout,
                                     retry=retry,
                                     post_change_delay=post_change_delay),  \
        f"Url did not contain {desired_url} after {timeout} seconds current url={browser.url}"


def _does_url_contain_target(target_url):
    return target_url in browser.url
