import time
from datetime import datetime, timedelta
from selenium.common.exceptions import NoSuchElementException    
from logging import getLogger
from structlog import wrap_logger
from urllib.parse  import urlparse
from acceptance_tests import browser

logger = wrap_logger(getLogger(__name__))


def is_text_present_with_retry(text, retries=3, delay=1):
    """Waits <delay> seconds to see if test is present, if not then issues browser reload.
    will repeat this up to <retries> times or return if text found.
     Parameters:
         text: Text to look for
         retries: The maximum number of reloads that may be attempted
         delay: The amount of time to check if the text is present.
    Returns: True if text found else False
    """
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
    """Waits for specific text in the body , returns True if found else asserts.

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


def wait_for_url_matches_one_of(desired_url, alternate_url=None, timeout=2, retry=1, post_change_delay=0.1):
    """Waits for url to be either of two specific urls, for up to the timeout, asserts if it does not do this """
    url_match = _wait_for_url_matches(desired_url=desired_url,
                                      alternate_url=alternate_url,
                                      timeout=timeout,
                                      retry=retry,
                                      post_change_delay=post_change_delay)

    if alternate_url:
        assert url_match, \
            f"Url did not contain {desired_url} or {alternate_url} after {timeout} seconds current url={browser.url}"
    else:
        assert url_match, \
            f"Url did not contain {desired_url} after {timeout} seconds current url={browser.url}"


def wait_for_url_path_or_query_changed(initial_url, timeout=2, retry=1, post_change_delay=0.1):
    """Waits for url to change from an initial value, for up to the timeout, asserts if it does not do this """
    url_match = _wait_for_path_or_query_not_matching(initial_url=initial_url,
                                                     timeout=timeout,
                                                     retry=retry,
                                                     post_change_delay=post_change_delay)

    assert url_match, \
        f"Url did not change from {initial_url} after {timeout} seconds"


def wait_for_url_matches(desired_url, timeout=2, retry=1, post_change_delay=0.1):
    """waits for a specific url to be in the browser and page load complete"""
    wait_for_url_matches_one_of(desired_url, alternate_url=None, timeout=timeout,
                                retry=retry, post_change_delay=post_change_delay)


def wait_for(fn, timeout, retry, *argv):
    """run function multiple times within a timeout window or until it returns a truthy value

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


def _wait_for_url_matches(desired_url, alternate_url=None, timeout=2, retry=1, post_change_delay=0.1):
    """ Waits for either timeout or for the url to get to a value that matches the expected value,
    whichever comes first. If the browser gets to the url then waits a further post_change_delay
    ( intended to allow page load to complete)
    Intended to replace blind sleeps
    Uses starts with to cope with redirects around sign in pages where <some_url>/sign-in goes to <some_url> if
    user already signed in
    Parameters :

    desired_url (str): The url we wish to get to
    alternate_url (str): A valid alternate url ( to allow for redirection , logged out etc)
    timeout (int or float): Total amount of time in seconds to wait before returning a default of False
    retry (int or float): Time in seconds after one attempt will execute function again.
    post_change_delay (int or float): How long to delay after a change to allow for page load completion

    Returns:
    True if target url achieved within the time_to_wait , else False
    """

    if _does_url_match(desired_url, alternate_url):  # If already at target then enforce post change delay
        time.sleep(post_change_delay)
        return True

    ret_val = wait_for(_does_url_match, timeout, retry, desired_url, alternate_url)
    if ret_val:
        time.sleep(post_change_delay)

    return ret_val


def _wait_for_path_or_query_not_matching(initial_url, timeout=2, retry=1, post_change_delay=0.1):
    """ Waits for either timeout or for the url to get to change (path and query string) from an initial value based on
    whichever comes first. If the url changes then waits a further post_change_delay
    ( intended to allow page load to complete)
    Intended to replace blind sleeps

    Parameters :

    initial_url (str): The url we wish to move from
    timeout (int or float): Total amount of time in seconds to wait before returning a default of False
    retry (int or float): Time in seconds after one attempt will execute function again.
    post_change_delay (int or float): How long to delay after a change to allow for page load completion

    Returns:
    True if target url achieved within the time_to_wait , else False
    """

    if _does_path_and_query_not_match(initial_url):  # If url changed on entry then enforce post change delay
        time.sleep(post_change_delay)
        return True

    ret_val = wait_for(_does_path_and_query_not_match, timeout, retry, initial_url)
    if ret_val:
        time.sleep(post_change_delay)

    return ret_val


def _does_url_match(target_url, alternate_url):
    """returns true if the current browser url matches either of the two urls supplied and page load is complete"""

    if alternate_url:
        ret_val = (_do_paths_match(target_url, browser.url) or _do_paths_match(alternate_url, browser.url)) \
                  and browser.driver.execute_script('return document.readyState;') == 'complete'
    else:
        ret_val = _do_paths_match(target_url, browser.url) and browser.driver.execute_script(
            'return document.readyState;') == 'complete'

    return ret_val


def _does_path_and_query_not_match(target_url):
    """Returns true if document is ready and either paths do not match or query strings do not match"""
    return browser.driver.execute_script('return document.readyState;') == 'complete' and \
           not (_do_paths_match(target_url, browser.url) and _do_query_strings_match(target_url, browser.url))


def _do_paths_match(a, b):
    """returns true if the path part of the 2 urls are equal
    a url being <scheme>:<location><path>?<querystring>"""

    return urlparse(a).path == urlparse(b).path


def _do_query_strings_match(a, b):
    """returns true if the query strings of 2 urls match"""
    return urlparse(a).query == urlparse(b).query
