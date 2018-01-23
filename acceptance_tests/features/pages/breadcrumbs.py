from acceptance_tests import browser


def click_breadcrumb(number):
    browser.find_by_id(f'breadcrumb-{number}').click()


def get_breadcrumbs():
    return [browser.find_by_id(f'breadcrumb-{number}').text for number in range(1, 5)]
