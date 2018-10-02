from logging import getLogger

from structlog import wrap_logger

logger = wrap_logger(getLogger(__name__))


def scenario_data_setup_not_required(_):
    logger.info('Scenario specific data is not required')
