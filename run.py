import argparse
import logging
import os
from distutils.util import strtobool

from behave import __main__ as behave_executable

logger = logging.getLogger(__name__)

DEFAULT_COMMAND_LINE_ARGS = '--stop'
DEFAULT_BEHAVE_FORMAT = 'progress2'
DEFAULT_ACCEPTANCE_FEATURES_DIRECTORY = 'acceptance_tests/features'
DEFAULT_SYSTEM_DIRECTORY = 'system_tests/features'
DEFAULT_TAGS = '~@standalone'


def is_valid_sequential_environment():
    if os.getenv('IGNORE_SEQUENTIAL_DATA_SETUP') is None:
        return True

    is_ignore_sequential_data_setup = strtobool(os.getenv('IGNORE_SEQUENTIAL_DATA_SETUP'))

    return not not is_ignore_sequential_data_setup


def parse_arguments():
    """
    Parses commandline arguments
    :return: Parsed arguments
    """
    parser = argparse.ArgumentParser('Run behave in sequential mode for scenarios')
    parser.add_argument('--command_line_args', '-a', help='Command line arguments', default=DEFAULT_COMMAND_LINE_ARGS)
    parser.add_argument('--format', '-f', help='Behave format', default=DEFAULT_BEHAVE_FORMAT)
    parser.add_argument('--tags', '-t', help='specify behave tags to run', default=DEFAULT_TAGS)
    parser.add_argument('--system_features_directory', '-sd', help='specify directory containing system features',
                        default=DEFAULT_SYSTEM_DIRECTORY)
    parser.add_argument('--acceptance_features_directory', '-ad',
                        help='specify directory containing acceptance features',
                        default=DEFAULT_ACCEPTANCE_FEATURES_DIRECTORY)

    args = parser.parse_args()

    return args


def main():
    """
    Runner
    """

    if not is_valid_sequential_environment():
        logger.error(
            "Error: Environment Variable(s) must be set as 'IGNORE_NON_STANDALONE_DATA_SETUP=False'")

    args = parse_arguments()

    logger.error('command_line_args=' + args.command_line_args)
    logger.error('args.format=' + args.format)
    logger.error('args.tags=' + args.tags)
    logger.error('args.system_features_directory' + args.system_features_directory)
    logger.error('args.acceptance_features_directory' + args.acceptance_features_directory)

    behave_executable.main(
        args=f'--stop {args.command_line_args} --format {args.format} --tags={args.tags} {args.system_features_directory}')
    behave_executable.main(
        args=f'--stop {args.command_line_args} --format {args.format} --tags={args.tags} {args.acceptance_features_directory}')


if __name__ == '__main__':
    main()
