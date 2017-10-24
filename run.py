import logging

from structlog import wrap_logger  #NOQA  # pylint: disable=wrong-import-position
from behave import __main__ as behave_executable


logger = wrap_logger(logging.getLogger(__name__))


if __name__ == '__main__':

    behave_executable.main()

    def before_scenario(context, scenario):
        if "ignore" in scenario.effective_tags:
            scenario.skip("Unimplemented Functionality")
            return
