from acceptance_tests import browser


def click_breadcrumb(number):
    browser.find_by_id(f'breadcrumb-{number}').find_by_tag('a').click()


def breadcrumbs_exists():
    return browser.is_element_present_by_id('breadcrumbs')


def get_breadcrumbs():
    return [element.text for element in browser.find_by_id('breadcrumbs').find_by_tag('li')]
