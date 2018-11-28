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
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from distutils.util import strtobool
from multiprocessing import Queue
from subprocess import CalledProcessError, PIPE, Popen, TimeoutExpired, check_output

from common.common_utilities import create_behave_tags, get_child_processes, kill_all_processes

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DEFAULT_COMMAND_LINE_ARGS = '--stop --no-summary'
DEFAULT_BEHAVE_FORMAT = 'progress2'
DEFAULT_FEATURES_DIRECTORY = 'acceptance_tests/features'
DEFAULT_PROCESSES = 6  # Higher than 6 causes collex (and possibly other services) to fail intermittently

DEFAULT_TAGS = 'standalone'
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
    parser = argparse.ArgumentParser('Run behave in parallel mode for scenarios')
    parser.add_argument('--command_line_args', '-a', help='Command line arguments', default=DEFAULT_COMMAND_LINE_ARGS)
    parser.add_argument('--format', '-f', help='Behave format', default=DEFAULT_BEHAVE_FORMAT)
    parser.add_argument('--acceptance_features_directory', '-d', help='specify directory containing features',
                        default=DEFAULT_FEATURES_DIRECTORY)
    parser.add_argument('--processes', '-p', type=int,
                        help=f'Maximum number of processes. Default [{DEFAULT_PROCESSES}] ', default=DEFAULT_PROCESSES)
    parser.add_argument('--test_tags', '-t', help='specify behave tags to run', default=DEFAULT_TAGS)
    parser.add_argument('--timeout', '-tout', type=int,
                        help='Maximum seconds to execute each scenario. Default = 300', default=300)
    parser.add_argument('--no-parallel-stop', '-ns', help='Do not stop parallel execution on failure',
                        action='store_true')

    args = parser.parse_args()

    # Handle Tag ANDing properly
    args.tags = create_behave_tags(args.test_tags)

    return args


def is_process_running(process):
    return process is not None and process.is_alive()


def _run_scenario(failure_queue: Queue, feature_scenario: str, scenario_index, timeout, command_line_args):
    feature, scenario = feature_scenario.split(DELIMITER)
    logger.info(f'Starting Scenario [{scenario_index}] : Feature [{feature}], Scenario [{scenario}]')

    execution_code = {0: 'OK', 1: 'FAILED', 2: 'TIMEOUT', 3: 'UNEXPECTED_ERROR'}

    cmd = f'behave {command_line_args} --format progress2 {feature} --name \"{scenario}\"'

    try:
        check_output(cmd, shell=True, timeout=timeout)
        code = 0
    except CalledProcessError as e:
        out_bytes = e.output
        code = 1
        failure_queue.put(f'FAILED - Feature: [{feature}], Scenario [{scenario}]"')
        logger.error(out_bytes.decode())
    except TimeoutExpired:
        code = 2
        failure_queue.put(f'TIMEOUT - Feature: [{feature}], Scenario [{scenario}]"')
    except Exception:
        code = 3
        failure_queue.put(f'ERROR - Feature: [{feature}], Scenario [{scenario}]"')
        logger.exception(f'Unexpected exception in Feature: [{feature}], Scenario [{scenario}]"')

    status = execution_code[code]
    logger.info(f"Finished Scenario [{scenario_index}] : Feature [{feature}], Scenario [{scenario}] --> {status}")

    # To give time for postgres connections to close before starting the next Scenario
    time.sleep(10)

    return feature, scenario, status


def run_all_scenarios(scenarios_to_run, max_threads, timeout, command_line_args, stop_on_failure):
    total_scenarios_run = 0

    thread_pool_size = get_thread_pool_size(max_threads, len(scenarios_to_run))

    failure_queue = Queue()

    with ThreadPoolExecutor(max_workers=thread_pool_size) as executor:
        scenario_futures = [executor.submit(_run_scenario, failure_queue, scenario, scenario_index, timeout,
                                            command_line_args)
                            for scenario_index, scenario in enumerate(scenarios_to_run)]

        aborting = False
        for future in as_completed(scenario_futures):
            if not future.cancelled():
                if stop_on_failure and not aborting and not failure_queue.empty():
                    aborting = True
                    logger.info('Test failure, aborting')
                    for future_to_cancel in scenario_futures:
                        future_to_cancel.cancel()
                try:
                    future.result()
                except Exception:
                    logger.exception('Parallel execution error')
                    failure_queue.put('Parallel execution error')
                total_scenarios_run += 1

    return total_scenarios_run, failure_queue


def get_thread_pool_size(max_threads: int, number_of_scenarios_to_run: int) -> int:
    return max_threads if number_of_scenarios_to_run > max_threads else number_of_scenarios_to_run


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
        logger.error(
            "Error: Environment Variable(s) must be set as 'IGNORE_SEQUENTIAL_DATA_SETUP=True'")
        exit(1)

    args = parse_arguments()

    scenarios_to_run = extract_scenarios_to_run(args.tags, args.acceptance_features_directory)

    logger.info(f"Running [{len(scenarios_to_run)}] Scenarios in [{args.processes}] Processes")

    if len(scenarios_to_run) == 0:
        sys.exit(0)

    start_time = datetime.now()
    total_scenarios_run, failure_queue = run_all_scenarios(scenarios_to_run, args.processes, args.timeout,
                                                           args.command_line_args, not args.no_parallel_stop)

    exit_code = print_summary(start_time, datetime.now(), total_scenarios_run, failure_queue)

    sys.exit(exit_code)


if __name__ == '__main__':
    main()
