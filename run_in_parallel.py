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
from datetime import datetime
from distutils.util import strtobool
from functools import partial
from multiprocessing import Pool
from subprocess import Popen, PIPE
from subprocess import check_output, CalledProcessError, TimeoutExpired

from reset_database import reset_database

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DEFAULT_FEATURES_DIRECTORY = 'acceptance_tests/features'
DEFAULT_TAGS = 'standalone'
DELIMITER = '_BEHAVE_PARALLEL_BDD_'

start_time = datetime.now()


def is_valid_parallel_environment():
    if os.getenv('RESET_DATABASE') == None or os.getenv('IGNORE_NON_STANDALONE_DATA_SETUP') == None:
        return False

    is_reset_database = strtobool(os.getenv('RESET_DATABASE'))
    is_ignore_non_standalone_data_setup = strtobool(os.getenv('IGNORE_NON_STANDALONE_DATA_SETUP'))

    return not is_reset_database and is_ignore_non_standalone_data_setup


def parse_arguments():
    """
    Parses commandline arguments
    :return: Parsed arguments
    """
    parser = argparse.ArgumentParser('Run behave in parallel mode for scenarios')
    parser.add_argument('--directory', '-d', help='specify directory containing features',
                        default=DEFAULT_FEATURES_DIRECTORY)
    parser.add_argument('--processes', '-p', type=int, help='Maximum number of processes. Default = 8', default=8)
    parser.add_argument('--tags', '-t', help='specify behave tags to run', default=DEFAULT_TAGS)
    parser.add_argument('--timeout', '-tout', type=int,
                        help='Maximum seconds to execute each scenario. Default = 300', default=300)

    # TODO BUG: "AND" tags not handled properly
    args = parser.parse_args()

    return args


def _run_feature(feature_scenario, timeout, directory):
    """
    Runs features/scenarios
    :param feature_scenario: Feature/scenario that should be run
    :type feature_scenario: str
    :return: Feature/scenario and status
    """
    execution_code = {0: 'OK', 1: 'FAILED', 2: 'TIMEOUT'}
    feature, scenario = feature_scenario.split(DELIMITER)
    logger.info(f"Processing feature: {feature} and scenario {scenario}")
    params = "--no-capture"
    cmd = f'behave --stop --format progress2 {feature} -i {feature.split("/")[-1]} --name \'{scenario}\''
    try:
        r = check_output(cmd, shell=True, timeout=timeout)
        code = 0
    except CalledProcessError as e:
        out_bytes = e.output
        logger.info(out_bytes)
        code = e.returncode
    except TimeoutExpired:
        code = 2
    status = execution_code[code]
    logger.info(f"{feature:50}: {scenario} --> {status}")
    return feature, scenario, status


def main():
    """
    Runner
    """

    if not is_valid_parallel_environment():
        logger.error(
            "Environment Variables must be set as 'RESET_DATABASE=False' & 'IGNORE_NON_STANDALONE_DATA_SETUP=True'")
        exit(1)

    reset_database()

    args = parse_arguments()
    pool = Pool(args.processes)

    features_to_run = extract_scenarios_to_run(args)

    run_feature = partial(_run_feature, timeout=args.timeout, directory=args.directory)
    logger.info("--------------------------------------------------------------------------")
    output = 0
    for feature, scenario, status in pool.map(run_feature, features_to_run):
        if status != 'OK':
            if output == 0:
                if status == "FAILED":
                    output = 1
                else:
                    output = 2
    logger.info("--------------------------------------------------------------------------")
    end_time = datetime.now()

    logger.info(f"Duration: {format(end_time - start_time)}")

    sys.exit(output)


def extract_scenarios_to_run(args):
    """
    Performs a Behave dry run to extract all Features/Scenarios with matching Tags before filtering out only Scenarios
    that need testing i.e. 'status' == 'untested'
    :return: Scenarios to run
    """

    if args.tags:
        cmd = f'behave -d --no-junit --f json --no-summary -t {args.tags} {args.directory}'
    else:
        cmd = f'behave -d --no-junit --f json --no-summary {args.directory}'

    p = Popen(cmd, stdout=PIPE, shell=True)
    out, err = p.communicate()
    try:
        json_all_features = json.loads(out.decode())
    except ValueError:
        json_all_features = []

    # Extract only the scenarios that need testing
    matching_features_scenarios = [[e['location'][:-2] + DELIMITER + i['name']
                            for i in e['elements']
                            if i['keyword'].upper() in ["scenario".upper(), "scenario outline".upper()] and i[
                                'status'] == 'untested']
                           for e in json_all_features]

    scenarios_to_run = []

    # Convert to single List
    for elto in matching_features_scenarios:
        scenarios_to_run = scenarios_to_run + elto

    logger.info(f"Found {len(scenarios_to_run)} scenarios")
    logger.info(f"Timeout for each scenario {args.timeout} seconds")
    if args.processes > len(scenarios_to_run):
        logger.info(f"You have defined {args.processes} and Will execute only necessary {len(scenarios_to_run)} parallel process ")
    else:
        logger.info(f"Will execute {args.processes} parallel process")

    return scenarios_to_run


if __name__ == '__main__':
    main()

