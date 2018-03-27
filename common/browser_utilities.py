def is_text_present_with_retry(browser, retries: int, text: str, delay: int) -> bool:
    for attempt in range(retries):
        if not browser.is_text_present(text, wait_time=delay):
            browser.reload()
            retry = retries - 1
            is_text_present_with_retry(browser, retry, text, delay)
        else:
            return True
    return False
