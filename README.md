[![Build Status](https://travis-ci.org/ONSdigital/rasrm-acceptance-tests.svg?branch=master)](https://travis-ci.org/ONSdigital/rasrm-acceptance-tests)

# rasrm-acceptance-tests
System / API tests for RAS & RM services

## Prerequisites
1. Install [pyenv](https://github.com/pyenv/pyenv)
1. Install [pipenv](https://github.com/pypa/pipenv)


## Running the tests

To override any environmental variables you should export any variables before running the tests with behave e.g. `export HEADLESS=False` or by creating a local `.env` file. Most of the environmental variables are defined in [config.py](config.py)

### Headless
```bash
pipenv install --dev
```

First prepare the system for acceptance tests (this only needs to be run once)
```bash
make setup
```
Then run the acceptance tests
```bash
make acceptance_tests  # Will run the acceptance tests
```


### Phantom JS
```bash
npm install -g phantomjs-prebuilt
export HEADLESS=phantomjs
pipenv install --dev
make test
```


### Chrome
```bash
export HEADLESS=False  # or =True for Chrome in headless mode
pipenv install --dev
make test
```


### Commands
```bash
make start_services  # Brings all the services up using Docker
make setup  # Prepares data for acceptance tests
make style_tests  # Will check for Flake8 errors
make system_tests  # Will run the system tests
make acceptance_tests  # Will run the acceptance tests
make stop_services  # Bring down all the Docker services
make test  # Will bring all the services up and run all the tests
make TEST_TARGET=acceptance_tests/features/your.feature run_tests # Runs a single feature file WITHOUT 'make setup' first
make TEST_TARGET=acceptance_tests/features/your.feature acceptance_tests # Runs a single feature file WITH 'make setup' first
```


### Config
Config is set by environment variables in [config.py](config.py)

If any config is updated it also has to be updated in the Jenkinsfile


### Debugging tests in Pycharm
1. Set the environmental variable in pycharm HEADLESS=FALSE. Some instructions to do that https://www.jetbrains.com/help/pycharm/python-console.html
1. If running against another environment set any other host environmental variables in pycharm
1. Stick a breakpoint at the point you want to debug
1. Debug the `run.py` and wait to hit the breakpoint

### Debugging tests against services deployed in Cloudfoundry
1. Set Cloudfoundry database environmental variables
```bash
export CLOUDFOUNDRY_API=
export CLOUDFOUNDRY_EMAIL=
export CLOUDFOUNDRY_PASSWORD=
export CLOUDFOUNDRY_ORG=
export CLOUDFOUNDRY_SPACE=
```
2. Get database environmental variables `curl -fsSL  https://raw.githubusercontent.com/ONSdigital/ras-deploy/master/scripts/get_database_uris.sh |bash|sed -e 's/@.*:5432/@localhost:5432/g' > setenvs.sh`
1. Set database environmental variables `source setenvs.sh`
1. Get database URI `export DATABASE_NAME=$(cf apps | grep ras-collection-instrument-ci-migration | awk ‘{ print “cf env “$1 }‘| bash | grep “postgres://” | awk -F \” ‘{ print $4 }’ | sed ‘s!postgres://.*@\(.*\):.*!\1!’)`
1. Create an SSH tunnel to the database `cf ssh -L 5432:$DATABASE_NAME:5432 ras-collection-instrument-ci-migration`
cloudfoundry app name of a service that has a dependency on the database.
1. Set acceptance tests environmental variables in [config.py](config.py)
```bash
export ACTION_SERVICE_HOST=
export ACTION_SERVICE_PORT=
...
export SURVEY_SERVICE_HOST=
export SURVEY_SERVICE_PORT=
```
7. Reset data in cloudfoundry `make setup`
1. Run tests `pipenv run python run.py`

### Troubleshooting
#### Failing tests
The tests may be failing because you have teared down postgres recently
1. Run `make setup` which will reload any data required for the tests
