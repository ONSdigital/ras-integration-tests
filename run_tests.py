from behave import __main__ as behave_executable


if __name__ == '__main__':
    behave_executable.main()

    def before_scenario(context, scenario):
        if "ignore" in scenario.effective_tags:
            scenario.skip("Unimplemented Functionality")
            return
