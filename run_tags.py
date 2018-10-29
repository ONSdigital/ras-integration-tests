import os
import sys
from logging import getLogger
from behave import __main__ as behave_executable
from structlog import wrap_logger


logger = wrap_logger(getLogger(__name__))


if __name__ == '__main__':

    if len(sys.argv) < 2:
        print('You must supply at least one tag e.g acceptance_tests/features --tags=standalone')
        exit(1)

    format = os.getenv('BEHAVE_FORMAT', 'progress2')

    tags = sys.argv.copy()

    # Strip off program name
    del tags[0]

    all_tags = ''

    for t in tags:
        all_tags += f' --tags={t}'

    logger.warn('Running Acceptance Tests with ' + all_tags)

    behave_executable.main(args=f'--format {format} acceptance_tests/features ' + all_tags)
