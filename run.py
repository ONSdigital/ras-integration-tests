import logging

from structlog import wrap_logger  # NOQA  # pylint: disable=wrong-import-position
from behave import __main__ as behave_executable


logger = wrap_logger(logging.getLogger(__name__))


if __name__ == '__main__':

    behave_executable.main('system_tests/features')
    behave_executable.main('acceptance_tests/features')
