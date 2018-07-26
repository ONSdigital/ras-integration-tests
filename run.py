import os
from behave import __main__ as behave_executable


if __name__ == '__main__':
    format = os.getenv('BEHAVE_FORMAT', 'progress2')

    behave_executable.main(args=f'--format {format} system_tests/features')
    behave_executable.main(args=f'--format {format} acceptance_tests/features/notification_letter.feature')
