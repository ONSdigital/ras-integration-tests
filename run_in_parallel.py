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
from multiprocessing import Process, Queue
from subprocess import Popen, PIPE, check_output, CalledProcessError, TimeoutExpired

from reset_database import reset_database

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DEFAULT_COMMAND_LINE_ARGS = '--stop --no-summary'
DEFAULT_BEHAVE_FORMAT = 'progress2'
DEFAULT_FEATURES_DIRECTORY = 'acceptance_tests/features'
DEFAULT_PROCESSES = 6  # Higher than 6 causes collex (and possibly other services) to fail intermittently

DEFAULT_TAGS = 'standalone'
DELIMITER = '_BEHAVE_PARALLEL_BDD_'


def is_valid_parallel_environment():
    if os.getenv('RESET_DATABASE') == None or os.getenv('IGNORE_SEQUENTIAL_DATA_SETUP') == None:
        return False

    is_reset_database = strtobool(os.getenv('RESET_DATABASE'))
    is_ignore_sequential_data_setup = strtobool(os.getenv('IGNORE_SEQUENTIAL_DATA_SETUP'))

    return not is_reset_database and is_ignore_sequential_data_setup


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
    parser.add_argument('--tags', '-t', help='specify behave tags to run', default=DEFAULT_TAGS)
    parser.add_argument('--timeout', '-tout', type=int,
                        help='Maximum seconds to execute each scenario. Default = 300', default=300)

    # TODO BUG: "AND" tags not handled properly
    args = parser.parse_args()

    return args


def is_process_running(process):
    return process != None and process.is_alive()


def _run_scenario(q, feature_scenario, timeout, command_line_args):
    """
    Runs features/scenarios
    :param feature_scenario: Feature/scenario that should be run
    :type feature_scenario: str
    :return: Feature/scenario and status
    """

    execution_code = {0: 'OK', 1: 'FAILED', 2: 'TIMEOUT'}
    feature, scenario = feature_scenario.split(DELIMITER)

    cmd = f'behave {command_line_args} --format progress2 {feature} --name \"{scenario}\"'

    try:
        check_output(cmd, shell=True, timeout=timeout)
        code = 0
    except CalledProcessError as e:
        out_bytes = e.output
        code = e.returncode
    except TimeoutExpired:
        code = 2

    status = execution_code[code]
    logger.info(f"{feature:50}: {scenario} --> {status}")

    if status == 'FAILED':
        q.put(f'FAILED - Feature: [{feature}], Scenario [{scenario}]"')
        logger.error(out_bytes.decode())

    return feature, scenario, status


def run_all_scenarios(scenarios_to_run, thread_count, timeout, command_line_args):
    total_scenarios_to_run = len(scenarios_to_run)

    # Set number of threads needed
    if total_scenarios_to_run < thread_count:
        process_pool_size = total_scenarios_to_run
    else:
        process_pool_size = thread_count

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
                    f"Processing Feature [{scenario_index}] : [{feature}], Scenario [{scenario}] in process no [{process_index}]")
                process_pool[process_index] = Process(target=_run_scenario, args=(
                    failure_queue, scenarios_to_run[scenario_index], timeout, command_line_args))
                process_pool[process_index].start()

                scenario_index += 1

                if scenario_index == total_scenarios_to_run:
                    break

        # If last Scenario has started, wait for it to finish
        if scenario_index == total_scenarios_to_run:

            while processes_running:

                # Assume all finished
                processes_running = False

                for process_index in range(process_pool_size):
                    if is_process_running(process_pool[process_index]):
                        processes_running = True
                        time.sleep(3)
                        break
        else:
            time.sleep(3)

    return total_scenarios_to_run, failure_queue


def find_matching_features_and_scenarios(tags, acceptance_features_directory):
    cmd = f'behave -d --no-junit --f json --no-summary -t {tags} {acceptance_features_directory}'

    p = Popen(cmd, stdout=PIPE, shell=True)
    out, err = p.communicate()
    try:
        json_all_features = json.loads(out.decode())
    except ValueError:
        json_all_features = []

    return json_all_features


def extract_scenarios_to_run(tags, acceptance_features_directory):
    """
    Performs a Behave dry run to extract all Features/Scenarios with matching Tags before filtering out only Scenarios
    that need testing i.e. 'status' == 'untested'
    :return: Scenarios to run
    """
    matching_features_and_scenarios = find_matching_features_and_scenarios(tags, acceptance_features_directory)

    # Extract only the scenarios that need testing
    untested_scenarios = [[e['location'][:-2] + DELIMITER + i['name']
                           for i in e['elements']
                           if i['keyword'].upper() in ["scenario".upper(), "scenario outline".upper()] and i[
                               'status'] == 'untested']
                          for e in matching_features_and_scenarios]

    scenarios_to_run = []

    # Convert to single List
    for scenario in untested_scenarios:
        scenarios_to_run = scenarios_to_run + scenario

    return scenarios_to_run


def print_summary(start_time, end_time, total_scenarios_run, failure_queue):

    struct_time = time.strptime(str(end_time - start_time), "%H:%M:%S.%f")

    duration = f'{struct_time.tm_hour:02}:{struct_time.tm_min:02}:{struct_time.tm_sec:02}'

    logger.info(f'A total of [{total_scenarios_run}] Scenario(s) took {duration} to run')

    failed = 0
    exit_code = 0

    if not failure_queue.empty():
        while not failure_queue.empty():
            logger.info('  ' + failure_queue.get())
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
            "Error: Environment Variables must be set as 'RESET_DATABASE=False' & 'IGNORE_NON_STANDALONE_DATA_SETUP=True'")
        exit(1)

    args = parse_arguments()

    scenarios_to_run = extract_scenarios_to_run(args.tags, args.acceptance_features_directory)

    logger.info(f"Running [{len(scenarios_to_run)}] Scenarios in [{args.processes}] Processes")

    reset_database()

    start_time = datetime.now()
    total_scenarios_run, failure_queue = run_all_scenarios(scenarios_to_run, args.processes, args.timeout,
                                                           args.command_line_args)

    exit_code = print_summary(start_time, datetime.now(), total_scenarios_run, failure_queue)

    sys.exit(exit_code)


if __name__ == '__main__':
    main()
