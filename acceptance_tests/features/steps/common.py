from behave import given

from acceptance_tests.features.environment import register_respondent
from controllers.party_controller import get_party_by_email

# Temporary place to keep common steps


@given('the respondent with email "{email}" is enrolled')
def respondent_ail_is_enrolled(_, email):
    create_respondent(email)


def create_respondent(email):
    email_in_use = get_party_by_email(email)
    if not email_in_use:
        register_respondent(survey_id='cb8accda-6118-4d3b-85a3-149e28960c54', period='201801',
                            username=email, ru_ref=49900000001)
