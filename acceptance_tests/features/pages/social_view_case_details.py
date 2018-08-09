from acceptance_tests import browser
from config import Config

case_id = "7a321aa2-a46b-4637-b7a9-35f3d1b94dea"


def go_to():
    browser.visit(f"{Config.RESPONSE_OPERATIONS_UI}/social/case/{case_id}")


def get_page_title():
    return browser.title


def get_reference_number():
    return browser.driver.find_element_by_id('case_ref').value


def get_status():
    return browser.driver.find_element_by_id('case-group-status').value


def get_address():
    address_details = {
        "prem1": browser.find_by_id('case-prem1').value,
        "prem2": browser.find_by_id('case-prem2').value,
        "prem3": browser.find_by_id('case-prem3').value,
        "prem4": browser.find_by_id('case-prem4').value,
        "district": browser.find_by_id('case-district').value,
        "post_town": browser.find_by_id('case-post_town').value,
        "postcode": browser.find_by_id('case-postcode').value
    }
    return address_details
