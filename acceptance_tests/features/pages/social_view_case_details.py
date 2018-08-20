from acceptance_tests import browser


def get_reference_number():
    return browser.driver.find_element_by_id('case_ref').text


def get_status():
    return browser.driver.find_element_by_id('case-group-status').text


def get_address():
    address_details = {
        "address_line_1": browser.find_by_id('case-address-line-1').text,
        "address_line_2": browser.find_by_id('case-address-line-2').text,
        "locality": browser.find_by_id('case-locality').text,
        "town": browser.find_by_id('case-town-name').text,
        "postcode": browser.find_by_id('case-postcode').text
    }
    return address_details
