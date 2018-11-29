import argparse
import logging
import os
import sys
from distutils.util import strtobool
from logging import getLogger

from behave import __main__ as behave_executable
from structlog import wrap_logger

from common.common_utilities import create_behave_tags_argument, create_behave_stop_argument, \
    create_behave_show_skipped_tests_argument, create_behave_log_level_argument, create_behave_format_argument, \
    create_behave_acceptance_feature_directory_argument

DEFAULT_STOP_ON_FAILURE = 'True'
DEFAULT_SHOW_SKIPPED_TESTS = 'False'
DEFAULT_LOG_LEVEL = 'INFO'
DEFAULT_BEHAVE_FORMAT = 'progress2'
DEFAULT_TAGS = '~@standalone'
DEFAULT_FEATURE_DIRECTORY = 'acceptance_tests/features'

logger = wrap_logger(getLogger(__name__))


def is_valid_sequential_environment():
    if os.getenv('IGNORE_SEQUENTIAL_DATA_SETUP') is None:
        return True

    is_ignore_sequential_data_setup = strtobool(os.getenv('IGNORE_SEQUENTIAL_DATA_SETUP'))

    return not is_ignore_sequential_data_setup


def parse_arguments():
    """
    Parses commandline arguments
    :return: Parsed arguments
    """
    parser = argparse.ArgumentParser('Run behave in sequential mode for scenarios')
    parser.add_argument('--stop_on_failure', '-s', help='Stop on test failure', default=DEFAULT_STOP_ON_FAILURE)
    parser.add_argument('--show_skipped_tests', '-k', help='Show skipped tests', default=DEFAULT_SHOW_SKIPPED_TESTS)
    parser.add_argument('--log_level', '-l', help='Logging level', default=DEFAULT_LOG_LEVEL)
    parser.add_argument('--format', '-f', help='Behave format', default=DEFAULT_BEHAVE_FORMAT)
    parser.add_argument('--test_tags', '-t', help='Behave tags to run', default=DEFAULT_TAGS)
    parser.add_argument('--feature_directory', '-fd', help='Feature directory', default=DEFAULT_FEATURE_DIRECTORY)

    args = parser.parse_args()

    # Create behave test commmand line arguments
    args.behave_test_args = {
        'stop_on_failure': create_behave_stop_argument(args.stop_on_failure),
        'show_skipped_tests': create_behave_show_skipped_tests_argument(args.show_skipped_tests),
        'log_level': create_behave_log_level_argument(args.log_level),
        'format': create_behave_format_argument(args.format),
        'tags': create_behave_tags_argument(args.test_tags),
        'feature_directory': create_behave_acceptance_feature_directory_argument(args.feature_directory)
    }

    return args


def main():
    """
    Runner
    """
    if not is_valid_sequential_environment():
        logger.error("Error: Environment Variable(s) must be set as 'IGNORE_SEQUENTIAL_DATA_SETUP=False'")
        sys.exit(1)

    args = parse_arguments()

    logging.basicConfig(level=args.log_level)

    behave_args = args.behave_test_args

    cmd_line_args = f'{behave_args["stop_on_failure"]} ' \
                    f'{behave_args["show_skipped_tests"]} ' \
                    f'{behave_args["log_level"]} ' \
                    f'{behave_args["format"]} ' \
                    f'{behave_args["tags"]} ' \
                    f'{behave_args["feature_directory"]}'

    exit_code = behave_executable.main(cmd_line_args)

    sys.exit(exit_code)


if __name__ == '__main__':
    main()
