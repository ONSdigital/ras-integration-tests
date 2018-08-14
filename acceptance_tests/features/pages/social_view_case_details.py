from acceptance_tests import browser


def get_reference_number():
    return browser.driver.find_element_by_id('case_ref').text


def get_status():
    return browser.driver.find_element_by_id('case-group-status').text


def get_address():
    address_details = {
        "prem1": browser.find_by_id('case-prem1').text,
        "prem2": browser.find_by_id('case-prem2').text,
        "prem3": browser.find_by_id('case-prem3').text,
        "prem4": browser.find_by_id('case-prem4').text,
        "district": browser.find_by_id('case-district').text,
        "post_town": browser.find_by_id('case-post_town').text,
        "postcode": browser.find_by_id('case-postcode').text
    }
    return address_details
