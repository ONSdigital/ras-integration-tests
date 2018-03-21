from behave import __main__ as behave_executable


if __name__ == '__main__':

    behave_executable.main(args='--format progress2 system_tests/features')
    behave_executable.main(args='--format progress2 acceptance_tests/features')
