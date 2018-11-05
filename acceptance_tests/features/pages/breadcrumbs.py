from acceptance_tests import browser

driver = browser.driver


def click_breadcrumb(number):
    browser.find_by_id(f'breadcrumb-{number}').find_by_tag('a').click()


def breadcrumbs_exists():
    return bool( len(driver.find_elements_by_css_selector('.breadcrumb')) )


def get_breadcrumbs():
    breadcrumbs_items = driver.find_elements_by_css_selector('.breadcrumb li')
    return [element.text for element in breadcrumbs_items]
