[![Build Status](https://travis-ci.org/ONSdigital/ras-integration-tests.svg?branch=master)](https://travis-ci.org/ONSdigital/ras-integration-tests)
# ras-integration-tests
System / API tests for RAS & RM services


# Running the tests

To override any environmental variables you should export any variables before running the tests with behave e.g. `export HEADLESS=False`.
The environmental variables are defined in [config.py](config.py)

### Headless
```bash
npm install -g phantomjs-prebuilt 
pipenv install --dev
pipenv run behave system_tests/features # This will only run the system tests
pipenv run behave acceptance_tests/features # This will only run the acceptance tests
```

### Chrome
```bash
export HEADLESS=False
pipenv install --dev
pipenv run behave system_tests/features # This will only run the system tests
pipenv run behave acceptance_tests/features # This will only run the acceptance tests
```