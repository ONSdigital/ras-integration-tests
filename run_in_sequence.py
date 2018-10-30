import argparse
import logging
import os
import sys
from distutils.util import strtobool

from behave import __main__ as behave_executable

from common.common_utilities import create_behave_tags

logger = logging.getLogger(__name__)

DEFAULT_COMMAND_LINE_ARGS = '--stop'
DEFAULT_BEHAVE_FORMAT = 'progress2'
DEFAULT_ACCEPTANCE_FEATURES_DIRECTORY = 'acceptance_tests/features'
DEFAULT_TAGS = '~@standalone'


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
    parser.add_argument('--command_line_args', '-a', help='Command line arguments', default=DEFAULT_COMMAND_LINE_ARGS)
    parser.add_argument('--format', '-f', help='Behave format', default=DEFAULT_BEHAVE_FORMAT)
    parser.add_argument('--test_tags', '-t', help='specify behave tags to run', default=DEFAULT_TAGS)
    parser.add_argument('--acceptance_features_directory', '-ad',
                        help='specify directory containing acceptance features',
                        default=DEFAULT_ACCEPTANCE_FEATURES_DIRECTORY)

    args = parser.parse_args()

    # Handle Tag ANDing properly
    args.tags = create_behave_tags(args.test_tags)

    return args


def main():
    """
    Runner
    """
    if not is_valid_sequential_environment():
        logger.error("Error: Environment Variable(s) must be set as 'IGNORE_SEQUENTIAL_DATA_SETUP=False'")

    args = parse_arguments()

    behave_args = f'{args.command_line_args} --format {args.format} {args.tags} {args.acceptance_features_directory}'
    exit_code = behave_executable.main(behave_args)

    sys.exit(exit_code)


if __name__ == '__main__':
    main()
