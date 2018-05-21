from acceptance_tests import browser


def is_text_present_with_retry(text, retries=3, delay=1):
    for attempt in range(retries):
        if browser.is_text_present(text, wait_time=delay):
            return True
        browser.reload()
    return False


def is_element_present_by_id_with_retry(id, retries=3, delay=1):
    for attempt in range(retries):
        if browser.is_element_present_by_id(id, wait_time=delay):
            return True
        browser.reload()
    return False
