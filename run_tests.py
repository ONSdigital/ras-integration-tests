import logging
import os

from cloud.cloud_foundry import ONSCloudFoundry  #NOQA  # pylint: disable=wrong-import-position
from structlog import wrap_logger  #NOQA  # pylint: disable=wrong-import-position
from behave import __main__ as behave_executable


logger = wrap_logger(logging.getLogger(__name__))


if __name__ == '__main__':
    cf = ONSCloudFoundry()
    # First check if front-stage is deployed in a Cloud Foundry environment
    if cf.detected:
        port = cf.port
        protocol = cf.protocol
        logger.info('* Cloud Foundry environment detected.')
        logger.info('* Cloud Foundry port "{}"'.format(port))
        logger.info('* Cloud Foundry protocol "{}"'.format(protocol))

    behave_executable.main()

    def before_scenario(context, scenario):
        if "ignore" in scenario.effective_tags:
            scenario.skip("Unimplemented Functionality")
            return
