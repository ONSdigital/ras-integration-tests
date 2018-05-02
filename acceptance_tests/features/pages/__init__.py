from acceptance_tests import browser


def scroll_to(element):
    elementY = element._element.location['y']
    browser.execute_script(f"window.scrollTo(0, {elementY});")
    return element
