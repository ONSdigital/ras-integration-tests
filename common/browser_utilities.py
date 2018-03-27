from acceptance_tests import browser

def is_text_present_with_retry(text, retries=3, delay=1):
    for attempt in range(retries):
        if not browser.is_text_present(text, wait_time=delay):
            browser.reload()
        else:
            return True

    return False
