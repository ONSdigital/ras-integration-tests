import datetime
from datetime import datetime
from logging import getLogger

from structlog import wrap_logger

from acceptance_tests import browser
from common import survey_utilities
from config import Config
from reset_database import reset_database

logger = wrap_logger(getLogger(__name__))

timings = {}


def set_test_execution_mode(context):
    try:
        context.standalone_mode = Config.STANDALONE and Config.STANDALONE == 'True'
    except AttributeError:
        context.standalone_mode = 'False'


def before_all(context):
    set_test_execution_mode(context)

    mode = ' ' if context.standalone_mode else ' NOT '
    logger.info(f'Acceptance Tests are{mode}RUNNING IN STANDALONE mode')

    if Config.RESET_DATABASE and Config.RESET_DATABASE == 'True':
        reset_database()

    if not context.standalone_mode:
        survey_utilities.setup_non_standalone_data_for_test()


def before_feature(context, feature):
    context.feature_name = feature.name


def before_scenario(context, scenario):
    if "skip" in scenario.effective_tags:
        scenario.skip("Marked with @skip")
        return
    timings[scenario.name] = {'start_time': datetime.now()}
    context.scenario_name = scenario.name

    logger.info(f'Running Feature [{context.feature_name}], Scenario [{context.scenario_name}]')

    # Default to non-standalone fixed user name standalone mode changes
    context.user_name = Config.RESPONDENT_USERNAME

    # Every standalone Scenario creates a new Survey and Collection Exercise
    if context.standalone_mode:
        survey_utilities.setup_standalone_data_for_test(context)


def after_scenario(context, scenario):
    if "skip" not in scenario.effective_tags:
        timings[scenario.name]['end_time'] = datetime.now()


def after_step(context, step):
    if step.status == "failed":
        logger.exception('Failed step', scenario=context.scenario.name, step=step.name)


def after_all(context):
    browser.quit()
    logger.info('Outputting execution time per test')

    def sort_by_execution_time(t):
        return (t[1]['end_time'] - t[1]['start_time']).total_seconds()

    for name, timing in sorted(timings.items(), key=sort_by_execution_time, reverse=True):
        diff = timing['end_time'] - timing['start_time']
        logger.info(f'{name} took {diff.total_seconds()}s')
