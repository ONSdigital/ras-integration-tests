# -*- coding: UTF-8 -*-

"""
based on from github "https://gist.github.com/s1ider/f13c2f163282dbec7a61"
Customized for parallel scenarios
Authors: i4s-pserrano
"""

import argparse
import json
import logging
import sys
from datetime import datetime
from functools import partial
from multiprocessing import Pool
from subprocess import Popen, PIPE
from subprocess import check_output, CalledProcessError, TimeoutExpired

logging.basicConfig(level=logging.INFO,
                    format="[%(levelname)-8s %(asctime)s] %(message)s")
logger = logging.getLogger(__name__)

delimiter = "_BEHAVE_PARALLEL_BDD_"

start_time = datetime.now()


def parse_arguments():
    """
    Parses commandline arguments
    :return: Parsed arguments
    """
    parser = argparse.ArgumentParser('Run behave in parallel mode for scenarios')
    parser.add_argument('--directory', '-d', help='specify directory containing features')
    parser.add_argument('--processes', '-p', type=int, help='Maximum number of processes. Default = 8', default=8)
    parser.add_argument('--tags', '-t', help='specify behave tags to run')
    parser.add_argument('--timeout', '-tout', type=int,
                        help='Maximum seconds to execute each scenario. Default = 300', default=300)

    #TODO BUG does not handle "AND" tags properly
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
    feature, scenario = feature_scenario.split(delimiter)
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
    args = parse_arguments()
    pool = Pool(args.processes)

    if not args.tags:
        logger.error('Only Standalone Acceptance Tests can currently run in parallel!')
        sys.exit(1)

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

    # Extract scenarios that need testing
    matching_features_scenarios = [[e['location'][:-2] + delimiter + i['name']
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

