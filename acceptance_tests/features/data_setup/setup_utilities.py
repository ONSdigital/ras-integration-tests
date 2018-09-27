from logging import getLogger

from structlog import wrap_logger

logger = wrap_logger(getLogger(__name__))


def scenario_setup_not_defined(_):
    logger.info('No scenario specific data setup defined')
