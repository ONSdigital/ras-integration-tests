from datetime import datetime
from logging import getLogger

from behave import use_fixture
from structlog import wrap_logger

from acceptance_tests import browser
from acceptance_tests.features import fixtures
from acceptance_tests.features.fixtures import \
    setup_enrolled_respondent, \
    setup_unenrolled_respondent, setup_default_data, \
    setup_unenrolled_respondent_generate_new_iac_collection_exercise_to_live_status, \
    setup_unenrolled_respondent_generate_new_iac, \
    setup_enrolled_respondent_generate_new_iac_collection_exercise_to_live_status, setup_data_2_enrolled_respondents
from common import survey_utilities
from config import Config
from exceptions import MissingFixtureError

FIELD_SEPARATOR = '-'
FIXTURE_TAG_PREFIX = 'fixture.'

USER_DESCRIPTION_SOCIAL_PREFIX = 'SOCIAL'
USER_DESCRIPTION_BUSINESS_PREFIX = 'BUSINESS'

logger = wrap_logger(getLogger(__name__))

timings = {}

fixture_scenario_registry = {
    'fixture.setup.data.default': setup_default_data,

    'fixture.setup.data.enrolled.respondent': setup_enrolled_respondent,
    'fixture.setup.data.unenrolled.respondent': setup_unenrolled_respondent,
    'fixture.setup.data.unenrolled.respondent.generate.new.iac': setup_unenrolled_respondent_generate_new_iac,
    'fixture.setup.data.collection.exercise.created': fixtures.setup_collection_exercise_to_created_status,
    'fixture.setup.data.collection.exercise.closed.social': fixtures.setup_collection_exercise_to_closed_status,
    'fixture.setup.data.unenrolled.respondent.generate.new.iac.collection.exercise.live':
        setup_unenrolled_respondent_generate_new_iac_collection_exercise_to_live_status,
    'fixture.setup.data.enrolled.respondent.generate.new.iac.collection.exercise.live':
        setup_enrolled_respondent_generate_new_iac_collection_exercise_to_live_status,
    'fixture.setup.data.2.enrolled.respondents': setup_data_2_enrolled_respondents
}


def before_all(_):

    # Run all tests using original method - standalone tests run in sequence
    if not is_ignore_sequential_data_setup():
        survey_utilities.setup_sequential_data_for_test()


def before_feature(context, feature):
    context.feature_name = feature.name


def process_scenario_fixtures(context):
    for tag in context.tags:
        if tag.startswith(FIXTURE_TAG_PREFIX):
            try:
                use_fixture(fixture_scenario_registry[tag], context)
            except KeyError:
                raise MissingFixtureError


def before_scenario(context, scenario):
    if "skip" in scenario.effective_tags:
        scenario.skip("Marked with @skip")
        return
    timings[scenario.name] = {'start_time': datetime.now()}
    context.scenario_name = scenario.name
    context.survey_type = get_survey_type(context.tags)

    logger.info(f'Running Feature [{context.feature_name}], Scenario [{context.scenario_name}]')

    # Default to non-standalone fixed user name, standalone mode changes it
    context.user_name = Config.RESPONDENT_USERNAME

    # Run any custom scenario setup from fixture tags
    process_scenario_fixtures(context)


def after_feature(_, feature):
    logger.info('Finished Feature [' + feature.name + ']')


def after_scenario(_, scenario):
    if "skip" not in scenario.effective_tags:
        timings[scenario.name]['end_time'] = datetime.now()


def after_step(context, step):
    if step.status == "failed":
        logger.exception('Failed step', scenario=context.scenario.name, step=step.name)


def after_all(_):
    browser.quit()
    logger.info('Outputting execution time per test')

    def sort_by_execution_time(t):
        return (t[1]['end_time'] - t[1]['start_time']).total_seconds()

    for name, timing in sorted(timings.items(), key=sort_by_execution_time, reverse=True):
        diff = timing['end_time'] - timing['start_time']
        logger.info(f'{name} took {diff.total_seconds()}s')


def is_ignore_sequential_data_setup():
    return Config.IGNORE_SEQUENTIAL_DATA_SETUP


def get_survey_type(tags):
    if 'social' in tags:
        return "Social"

    return 'Business'
