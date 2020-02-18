
"""
Run individual scenarios/features from python.
This can be useful for debugging.
"""


import sys
import os

from behave import __main__ as behave_executable


FEATURE = 'create_collection_exercise.feature'

# Use "" to run all scenarios within the given feature
SCENARIO = 'Each collection exercise must be associated to a specific survey'

HEADLESS = 'False'

FEATURE_DIR = 'acceptance_tests/features/'


def setup():
    os.system('make setup')


def run():

    os.environ["HEADLESS"] = HEADLESS

    cmd_line_args = f'--stop ' \
                    + '--format progress2 ' \
                    + (f'--name "{SCENARIO}" ' if SCENARIO else '') \
                    + (FEATURE_DIR + FEATURE)

    print(cmd_line_args)

    exit_code = behave_executable.main(cmd_line_args)

    sys.exit(exit_code)


if __name__ == '__main__':
    setup()
    run()
