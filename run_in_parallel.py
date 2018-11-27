# -*- coding: UTF-8 -*-

"""
based on from github "https://gist.github.com/s1ider/f13c2f163282dbec7a61"
Customized for parallel scenarios
Authors: i4s-pserrano
"""

import argparse
import json
import logging
import os
import sys
import time
from datetime import datetime
from distutils.util import strtobool
from logging import getLogger
from multiprocessing import Process, Queue
from subprocess import Popen, PIPE, check_output, CalledProcessError, TimeoutExpired

from structlog import wrap_logger

from common.common_utilities import create_behave_tags_argument, create_behave_stop_argument, \
    create_behave_show_skipped_tests_argument, create_behave_log_level_argument, create_behave_format_argument, \
    create_behave_acceptance_feature_directory_argument
from common.common_utilities import kill_all_processes, get_child_processes

DEFAULT_STOP_ON_FAILURE = 'True'
DEFAULT_SHOW_SKIPPED_TESTS = 'False'
DEFAULT_LOG_LEVEL = 'INFO'
DEFAULT_BEHAVE_FORMAT = 'progress2'
DEFAULT_TAGS = '@standalone'
DEFAULT_FEATURE_DIRECTORY = 'acceptance_tests/features'
DEFAULT_PROCESSES = 6  # Higher than 6 causes collex (and possibly other services) to fail intermittently

logger = wrap_logger(getLogger(__name__))

DELIMITER = '_BEHAVE_PARALLEL_BDD_'


def is_valid_parallel_environment():
    if os.getenv('IGNORE_SEQUENTIAL_DATA_SETUP') is None:
        return False

    is_ignore_sequential_data_setup = strtobool(os.getenv('IGNORE_SEQUENTIAL_DATA_SETUP'))

    return is_ignore_sequential_data_setup


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
    parser.add_argument('--processes', '-p', type=int, help=f'Maximum number of processes. '
                                                            f'Default [{DEFAULT_PROCESSES}] ',
                        default=DEFAULT_PROCESSES)
    parser.add_argument('--timeout', '-tout', type=int,
                        help='Maximum seconds to execute each scenario. Default = 300', default=300)

    args = parser.parse_args()

    # Create behave command line arguments
    args.behave_args = {
        'stop_on_failure': create_behave_stop_argument(args.stop_on_failure),
        'show_skipped_tests': create_behave_show_skipped_tests_argument(args.show_skipped_tests),
        'log_level': create_behave_log_level_argument(args.log_level),
        'format': create_behave_format_argument(args.format),
        'tags': create_behave_tags_argument(args.test_tags),
        'feature_directory': create_behave_acceptance_feature_directory_argument(args.feature_directory)
    }

    return args


def is_process_running(process):
    return process is not None and process.is_alive()


def _run_scenario(q, feature_scenario, timeout, stop_on_failure, show_skipped_tests, log_level, format):
    """
    Runs features/scenarios
    :param feature_scenario: Feature/scenario that should be run
    :type feature_scenario: str
    :return: Feature/scenario and status
    """

    execution_code = {0: 'OK', 1: 'FAILED', 2: 'TIMEOUT', 3: 'UNEXPECTED_ERROR'}
    feature, scenario = feature_scenario.split(DELIMITER)

    cmd_line_args = f'{stop_on_failure} ' \
                    f'{show_skipped_tests} ' \
                    f'{log_level} ' \
                    f'{format} ' \
                    f'{feature} ' \
                    f'--name \"{scenario}\"'

    out_bytes = None

    try:
        check_output(f'behave {cmd_line_args}', shell=True, timeout=timeout)
        code = 0
    except CalledProcessError as e:
        out_bytes = e.output
        code = 1
    except TimeoutExpired:
        code = 2
    except Exception:
        code = 3

    status = execution_code[code]
    logger.info(f"{feature:50}: {scenario} --> {status}")

    if status == 'FAILED':
        q.put(f'FAILED - Feature: [{feature}], Scenario [{scenario}]"')
        logger.error(out_bytes.decode())

    # To give time for postgres connections to close before starting the next Scenario
    time.sleep(10)

    return feature, scenario, status


def run_all_scenarios(scenarios_to_run, process_count, timeout, stop_on_failure, show_skipped_tests, log_level, format):
    total_scenarios_to_run = len(scenarios_to_run)

    # Set number of threads needed
    if total_scenarios_to_run < process_count:
        process_pool_size = total_scenarios_to_run
    else:
        process_pool_size = process_count

    process_pool = [None] * process_pool_size
    scenario_index = 0
    processes_running = True
    failure_queue = Queue(maxsize=0)

    # Run every scenario
    while processes_running:

        # Find a 'Free' Thread slot
        for process_index in range(process_pool_size):

            # Found one
            if not is_process_running(process_pool[process_index]):
                feature, scenario = scenarios_to_run[scenario_index].split(DELIMITER)

                logger.info(
                    f"Processing Feature [{scenario_index}] : [{feature}], Scenario [{scenario}] in [{process_index}]")
                process_pool[process_index] = Process(target=_run_scenario, args=(failure_queue,
                                                                                  scenarios_to_run[scenario_index],
                                                                                  timeout, stop_on_failure,
                                                                                  show_skipped_tests, log_level,
                                                                                  format))
                process_pool[process_index].start()

                scenario_index += 1

                if scenario_index == total_scenarios_to_run:
                    break

        # If last Scenario has started, wait for it to finish
        if scenario_index == total_scenarios_to_run:

            while processes_running:

                # Assume all finished
                processes_running = False

                for process in process_pool:
                    if is_process_running(process):
                        processes_running = True
                        time.sleep(3)
                        break
        else:
            time.sleep(3)

    return total_scenarios_to_run, failure_queue


def find_matching_features_and_scenarios(tags, acceptance_features_directory):
    cmd = f'behave -d --no-junit --f json --no-summary {tags} {acceptance_features_directory}'

    p = Popen(cmd, stdout=PIPE, shell=True)
    time.sleep(3)
    child_processes = get_child_processes(p.pid)

    out, err = p.communicate()
    try:
        json_all_features = json.loads(out.decode())
    except ValueError:
        json_all_features = []

    kill_all_processes(child_processes)

    return json_all_features


def extract_scenarios_to_run(tags, acceptance_features_directory):
    """
    Performs a Behave dry run to extract all Features/Scenarios with matching Tags before filtering out only Scenarios
    that need testing i.e. 'status' == 'untested'
    :return: Scenarios to run
    """
    matching_features_and_scenarios = find_matching_features_and_scenarios(tags, acceptance_features_directory)

    scenarios_to_run = []

    # Extract only the scenarios that need testing
    for feature in matching_features_and_scenarios:

        # Feature has at least 1 untested Scenario
        if feature['status'] == 'untested':

            # Find them
            for scenario in feature['elements']:

                # Test this Scenario
                if scenario['keyword'] in ["Scenario", "Scenario Outline"] and scenario['status'] == 'untested':
                    scenarios_to_run.append(feature['location'][:-2] + DELIMITER + scenario['name'])

    return scenarios_to_run


def print_summary(start_time, end_time, total_scenarios_run, failure_queue):
    struct_time = time.strptime(str(end_time - start_time), "%H:%M:%S.%f")

    duration = f'{struct_time.tm_hour:02}:{struct_time.tm_min:02}:{struct_time.tm_sec:02}'

    logger.info(f'A total of [{total_scenarios_run}] Scenario(s) took {duration} to run')

    failed = 0
    exit_code = 0

    if not failure_queue.empty():
        while not failure_queue.empty():
            logger.info(f'\t{failure_queue.get()}')
            failed += 1

        exit_code = 1

    successes = total_scenarios_run - failed

    logger.info(f'[{successes}] passed, [{failed}] failed')

    return exit_code


def main():
    """
    Runner
    """
    if not is_valid_parallel_environment():
        logger.error("Error: Environment Variable(s) must be set as 'IGNORE_SEQUENTIAL_DATA_SETUP=True'")
        exit(1)

    args = parse_arguments()

    logging.basicConfig(level=args.log_level)

    behave_args = args.behave_args

    scenarios_to_run = extract_scenarios_to_run(behave_args['tags'], behave_args['feature_directory'])

    logger.info(f"Running [{len(scenarios_to_run)}] Scenarios in [{args.processes}] Processes")

    if len(scenarios_to_run) == 0:
        sys.exit(0)

    start_time = datetime.now()

    total_scenarios_run, failure_queue = run_all_scenarios(scenarios_to_run,
                                                           args.processes,
                                                           args.timeout,
                                                           behave_args['stop_on_failure'],
                                                           behave_args['show_skipped_tests'],
                                                           behave_args['log_level'],
                                                           behave_args['format'])

    exit_code = print_summary(start_time, datetime.now(), total_scenarios_run, failure_queue)

    sys.exit(exit_code)


if __name__ == '__main__':
    main()
