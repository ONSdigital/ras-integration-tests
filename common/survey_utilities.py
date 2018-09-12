from datetime import timedelta
from random import randint

from acceptance_tests.features.environment import *
from controllers.collection_exercise_controller import *
from controllers.survey_controller import create_survey

logger = wrap_logger(getLogger(__name__))


def setup_survey_for_test(context, period, survey_name):
    ''' Creates a new Survey based on the values supplied '''

    survey_ref = str(randint(1001, 9999))
    response = create_survey_for_test(survey_name, context.unique_id, survey_ref)

    survey_id = response['survey_id']

    enrolment_code = create_collection_exercise_for_test(survey_id, period, context.unique_id,
                                                         context.scenario_name)

    survey_response = {
        'survey_name': response['survey_name'],
        'survey_short_name': response['survey_short_name'],
        'enrolment_code': enrolment_code
    }

    return survey_response


def create_period(from_date=datetime.utcnow()):
    return format_period(from_date.year, from_date.month)


def create_base_date_from_period(period):
    now = datetime.utcnow()
    period_year = int(period[:4])
    period_month = int(period[-2:])

    return datetime(period_year, period_month, now.day, now.hour, now.minute, now.second, now.microsecond)


def create_unique_ru_ref():
    return str(randint(50000000000, 59999999999))


def create_survey_for_test(survey_name, unique_id, survey_ref, survey_type='Business', survey_legal_basis='STA1947'):
    logger.info('Creating survey', test_name=survey_name)

    survey_short_name = unique_id

    response = create_survey(survey_type=survey_type, survey_ref=survey_ref, short_name=survey_short_name,
                             long_name=survey_name,
                             legal_basis=survey_legal_basis)

    survey_id = response['id']

    logger.info('Survey created - ', survey_id=survey_id,
                unique_id=unique_id,
                survey_long_name=survey_name,
                survey_short_name=survey_short_name)

    response = {}
    response['survey_id'] = survey_id
    response['unique_id'] = unique_id
    response['survey_name'] = survey_name
    response['survey_short_name'] = survey_short_name

    return response


def create_collection_exercise_for_test(survey_id, period, ru_ref, ce_name):
    ''' Creates a new Collection Exercise for the survey supplied '''

    logger.info('Creating Collection Exercise', survey_id=survey_id, period=period)

    user_description = make_user_description(ce_name)
    dates = generate_collection_exercise_dates_from_period(period)

    iac = create_and_execute_collection_exercise_with_unique_sample(survey_id, period, user_description, dates, ru_ref)

    logger.info('Collection Exercise created - ', survey_id=survey_id,
                ru_ref=ru_ref,
                user_description=user_description,
                period=period,
                dates=dates)

    return iac


def register_respondent_for_test(survey_id, period, username, ru_ref):
    register_respondent(survey_id, period, username, ru_ref)


def generate_collection_exercise_dates_from_period(period):
    """Generates a collection exercise events base date from the period supplied."""

    now = datetime.utcnow()
    period_year = int(period[:4])
    period_month = int(period[-2:])

    base_date = datetime(period_year, period_month, now.day, now.hour, now.minute, now.second, now.microsecond)

    return generate_collection_exercise_dates(base_date)


def generate_collection_exercise_dates(base_date):
    """Generates and returns collection exercise dates based on the base date supplied."""

    dates = {
        'mps': base_date + timedelta(seconds=5),
        'go_live': base_date + timedelta(minutes=1),
        'return_by': base_date + timedelta(days=10),
        'exercise_end': base_date + timedelta(days=11)
    }

    return dates


def create_respondent(user_name, enrolment_code):
    logger.info('Creating/retrieving respondent', username=user_name, enrolment_code=enrolment_code)

    respondent = party_controller.register_respondent(email_address=user_name,
                                                      first_name='first_name',
                                                      last_name='last_name',
                                                      password=Config.RESPONDENT_PASSWORD,
                                                      phone_number='0987654321',
                                                      enrolment_code=enrolment_code)
    respondent_id = respondent['id']

    party_controller.change_respondent_status(respondent_id)

    logger.info('Respondent exists', respondent_id=respondent_id, username=user_name, enrolment_code=enrolment_code)

    return respondent


def create_user_login(user_name):
    django_oauth_controller.verify_user(user_name)


def enrol_respondent(respondent_id, wait_for_case=False):
    logger.info('Enroling respondent', respondent_id=respondent_id, wait_for_case=wait_for_case)

    case_id = database_controller.enrol_party(respondent_id)

    case_controller.post_case_event(case_id, respondent_id, "RESPONDENT_ENROLED", "Respondent enrolled")
    if wait_for_case:
        wait_for_case_to_update(respondent_id)

    logger.info('Respondent Enrolled', respondent_id=respondent_id, case_id=case_id, wait_for_case=wait_for_case)

    return respondent_id


def create_utc_timestamp():
    return datetime.utcnow().strftime('%Y-%m-%d-%H-%M-%S-%f')


def format_period(period_year, period_month):
    return concatenate_strings(str(period_year), str(period_month).zfill(2))


def format_survey_name(description):
    unique_id = create_utc_timestamp()
    return concatenate_strings(concatenate_strings('TEST', description, "-"), unique_id, '-')


def make_user_description(description):
    return concatenate_strings('TEST', description, "-")


def make_respondent_user_name(left_part, right_part):
    return concatenate_strings(concatenate_strings(left_part, '@'), concatenate_strings(right_part, '.com'))


def concatenate_strings(left_part, right_part, separator=''):
    return left_part + separator + right_part
