#!/usr/bin/python
import argparse
from functools import partial
import json
import requests
from file_processing import process_files


def parse_args():
    parser = argparse.ArgumentParser(description='Load collection exercise CSV.')
    parser.add_argument("config", help="Configuration file")
    parser.add_argument("--posturl", help="URL to load collection exercises", nargs='?')
    parser.add_argument("--user", help="User to load collection exercises", nargs='?')
    parser.add_argument("--password", help="Password to load collection exercises", nargs='?')
    return parser.parse_args()


def post_collex(data, url, user, password):
    response = requests.post(url, json=data, auth=(user, password), verify=False)

    status_code = response.status_code
    detail_text = response.text if status_code != 201 else ''

    print("%s <= %s (%s)" % (status_code, data, detail_text))


def dump_collex(data):
    survey_id = data['surveyRef']
    period = data['exerciseRef']
    if survey_id and period:
        filename = "%s-%s.json" % (survey_id, period)
        with open(filename, 'w') as fo:
            json.dump(data, fo)

if __name__ == '__main__':
    args = parse_args()
    print("Config filename: %s" % args.config)
    config = json.load(open(args.config))
    config['api']['post-url'] = args.posturl or config['api']['post-url']
    config['api']['user'] = args.user or config['api']['user']
    config['api']['password'] = args.password or config['api']['password']
    input_files = config['inputFiles']
    print("Input filenames: %s" % input_files)
    column_mappings = config['columnMappings']
    api_url = config['api']['post-url']
    print("API URL: %s" % api_url)
    row_handler = dump_collex if config['dryRun'] else partial(post_collex,
                                                            url=api_url,
                                                            user=config['api']['user'],
                                                            password=config['api']['password'])

    process_files(input_files, row_handler, column_mappings)
