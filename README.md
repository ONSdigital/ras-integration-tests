[![Build Status](https://travis-ci.org/ONSdigital/rasrm-acceptance-tests.svg?branch=master)](https://travis-ci.org/ONSdigital/ras-integration-tests)

** **NOTE** ** This repo was renamed from ONSdigital/ras-integration-tests

# ras-integration-tests
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
```


### Config
Config is set by environment variables in [config.py](config.py)

If any config is updated it also has to be updated in the Jenkinsfile


### Debugging tests in Pycharm
1. Set the environmental variable in pycharm HEADLESS=FALSE. Some instructions to do that https://www.jetbrains.com/help/pycharm/python-console.html
1. Stick a breakpoint at the point you want to debug
1. Debug the `run.py` and wait to hit the breakpoint


### Troubleshooting
#### Failing tests
The tests may be failing because you have teared down postgres recently
1. Run `make acceptance_tests` which will reload any data required for the tests
