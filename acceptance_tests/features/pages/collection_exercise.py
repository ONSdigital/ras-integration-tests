from acceptance_tests import browser
from config import Config


def go_to(survey):
    browser.visit(Config.RESPONSE_OPERATIONS_UI_COLLECTION_EXERCISE.format(survey))


def get_survey_attributes():
    attributes = []
    survey_data = browser.find_by_css('.survey-info').first

    # Figure out more elegant way of getting at the list attributes in the page then via CSS search
