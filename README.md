[![Build Status](https://travis-ci.org/ONSdigital/ras-integration-tests.svg?branch=master)](https://travis-ci.org/ONSdigital/ras-integration-tests)

** **NOTE** ** This repo is to be renamed ras-rm-acceptance-tests

# ras-integration-tests
System / API tests for RAS & RM services

## Prerequisites
1. Install [pyenv](https://github.com/pyenv/pyenv)
1. Install [pipenv](https://github.com/pypa/pipenv)


## Running the tests

To override any environmental variables you should export any variables before running the tests with behave e.g. `export HEADLESS=False`.
The environmental variables are defined in [config.py](config.py)


### Headless
```bash
npm install -g phantomjs-prebuilt 
pipenv install --dev
```

```bash
make tmp_rm_tools # Will load data for tests
```

Use Response-Operations-UI to load collection instruments manually.
Then:
```bash
make set_up
make acceptance_tests # Will load any data needed for the tests and run the system tests and acceptance tests
```

### Chrome
```bash
export HEADLESS=False
pipenv install --dev
make acceptance_tests # Will load any data needed for the tests and run system tests and acceptance tests
```

### Commands
```bash
make system_tests # Will run the system tests
make clean # Will delete tmp_rm_tools
make tmp_rm_tools # Will load data for tests
```



### Debugging tests in Pycharm
1. Set the environmental variable in pycharm HEADLESS=FALSE. Some instructions to do that https://www.jetbrains.com/help/pycharm/python-console.html
1. Stick a breakpoint at the point you want to debug
1. Debug the `run.py` and wait to hit the breakpoint

### Troubleshooting
#### Failing tests
The tests may be failing because you have teared down postgres recently
1. Run `make clean` to delete tmp_rm_tools
1. Run `make acceptance_tests` which will reload any data required for the tests