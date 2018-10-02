from datetime import datetime
from logging import getLogger

from structlog import wrap_logger

from acceptance_tests import browser
from common import survey_utilities
from config import Config
from reset_database import reset_database

logger = wrap_logger(getLogger(__name__))

timings = {}


def before_all(_):

    # Delete all standalone test data
    if is_delete_standalone_data():
        reset_database()

    # Defaults to setting up data for non-standalone tests as before
    if not is_ignore_non_standalone_data_setup():
        survey_utilities.setup_non_standalone_data_for_test()


def before_feature(context, feature):
    context.feature_name = feature.name


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

    # A standalone Scenario creates a new Survey and Collection Exercise
    if is_standalone_scenario(context.tags):
        survey_utilities.setup_standalone_data_for_test(context)


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


def is_ignore_non_standalone_data_setup():
    try:
        if Config.IGNORE_NON_STANDALONE_DATA_SETUP and Config.IGNORE_NON_STANDALONE_DATA_SETUP == 'True':
            return True
        else:
            return False
    except AttributeError:
        return False


def is_delete_standalone_data():
    try:
        if Config.DELETE_STANDALONE_DATA and Config.DELETE_STANDALONE_DATA == 'True':
            return True
        else:
            return False
    except AttributeError:
        return False


def is_standalone_scenario(tags):
    return 'standalone' in tags


def get_survey_type(tags):
    if 'social' in tags:
        return "Social"

    #todo others?

    # todo ok as default?
    return 'Business'
