from datetime import datetime
from logging import getLogger

from behave import use_fixture
from structlog import wrap_logger

from acceptance_tests import browser
from acceptance_tests.features.fixtures import \
    setup_data_with_enrolled_respondent_user_and_internal_user, \
    setup_data_with_unenrolled_respondent_user, \
    setup_data_with_unenrolled_respondent_user_and_new_iac_and_collection_exercise_to_live, \
    setup_data_with_unenrolled_respondent_user_and_new_iac, \
    setup_data_with_enrolled_respondent_user_and_internal_user_and_new_iac_and_collection_exercise_to_live, \
    setup_data_with_2_enrolled_respondent_users_and_internal_user, \
    setup_data_with_internal_user_and_social_collection_exercise_to_closed_status, \
    setup_data_with_internal_user_and_collection_exercise_to_created_status, setup_data_with_response_user, \
    setup_with_internal_user, \
    setup_data_with_unenrolled_respondent_user_and_internal_user
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
    'fixture.setup.with.internal.user':
        setup_with_internal_user,
    'fixture.setup.data.with.internal.user':
        setup_data_with_response_user,
    'fixture.setup.data.with.enrolled.respondent.user.and.internal.user':
        setup_data_with_enrolled_respondent_user_and_internal_user,
    'fixture.setup.data.with.unenrolled.respondent.user':
        setup_data_with_unenrolled_respondent_user,
    'fixture.setup.data.with.unenrolled.respondent.user.and.internal.user':
        setup_data_with_unenrolled_respondent_user_and_internal_user,
    'fixture.setup.data.with.unenrolled.respondent.user.and.new.iac':
        setup_data_with_unenrolled_respondent_user_and_new_iac,
    'fixture.setup.data.with.internal.user.and.collection.exercise.to.created.status':
        setup_data_with_internal_user_and_collection_exercise_to_created_status,
    'fixture.setup.data.with.internal.user.and.social.collection.exercise.to.closed.status':
        setup_data_with_internal_user_and_social_collection_exercise_to_closed_status,
    'fixture.setup.data.with.unenrolled.respondent.user.and.new.iac.and.collection.exercise.to.live':
        setup_data_with_unenrolled_respondent_user_and_new_iac_and_collection_exercise_to_live,
    'fixture.setup.data.with.enrolled.respondent.user.and.internal.user.and.new.iac.and.collection.exercise.to.live':
        setup_data_with_enrolled_respondent_user_and_internal_user_and_new_iac_and_collection_exercise_to_live,
    'fixture.setup.data.with.2.enrolled.respondent.users.and.internal.user':
        setup_data_with_2_enrolled_respondent_users_and_internal_user
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
    context.respondent_user_name = Config.RESPONDENT_USERNAME
    context.internal_user_name = Config.INTERNAL_USERNAME

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
