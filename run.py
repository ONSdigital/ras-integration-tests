from behave import __main__ as behave_executable


if __name__ == '__main__':

    behave_executable.main('system_tests/features')
    behave_executable.main('acceptance_tests/features')
