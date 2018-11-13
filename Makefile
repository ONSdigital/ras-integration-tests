RM_TOOLS_REPO_URL = https://github.com/ONSdigital/rm-tools.git
RAS_RM_REPO_URL = https://github.com/ONSdigital/ras-rm-docker-dev.git

.PHONY: test system_tests acceptance_tests

install:
	pipenv install --dev

test: style_tests start_services wait_for_services system_tests setup acceptance_tests stop_services

style_tests:
	pipenv check --style . --max-line-length 120

start_services:
	./start_services.sh ${RAS_RM_REPO_URL}

stop_services:
	./stop_services.sh ${RAS_RM_REPO_URL}

wait_for_services:
	pipenv run python wait_until_services_up.py

clean:
	pipenv run python reset_database.py
	pipenv run python reset_sftp_server.py

setup: clean
	./setup_data.sh ${RM_TOOLS_REPO_URL}

# If you want to run a single feature file WITHOUT setup first use:
# make TEST_TARGET=acceptance_tests/features/your.feature run_tests
#
# If you want to run a single feature file WITH setup first use:
# make TEST_TARGET=acceptance_tests/features/your.feature acceptance_tests
BEHAVE_FORMAT = progress2
TEST_ARGS = --stop

system_tests: TEST_TARGET = system_tests/features  # This will only run the system tests
system_tests: run_tests

acceptance_tests: acceptance_sequential_tests acceptance_parallel_tests

acceptance_sequential_tests: setup
	export IGNORE_SEQUENTIAL_DATA_SETUP=False; \
	pipenv run python run_in_sequence.py --command_line_args="${TEST_ARGS}"

acceptance_parallel_tests:
	export IGNORE_SEQUENTIAL_DATA_SETUP=True; \
	pipenv run python run_in_parallel.py --command_line_args="${TEST_ARGS}"

acceptance_sequential_tests_all: setup
	export IGNORE_SEQUENTIAL_DATA_SETUP=False; \
	pipenv run python run_in_sequence.py --command_line_args="${TEST_ARGS}" --test_tags="~donotskipany"

rasrm_acceptance_tests: rasrm_acceptance_sequential_tests rasrm_acceptance_parallel_tests

rasrm_acceptance_sequential_tests: TEST_TAGS = ~@secure_messaging ~@standalone
rasrm_acceptance_sequential_tests:
	export IGNORE_SEQUENTIAL_DATA_SETUP=False; \
	pipenv run python run_in_sequence.py --command_line_args="${TEST_ARGS}" --test_tags "${TEST_TAGS}"

rasrm_acceptance_parallel_tests: TEST_TAGS = ~@secure_messaging @standalone
rasrm_acceptance_parallel_tests:
	export IGNORE_SEQUENTIAL_DATA_SETUP=True; \
	pipenv run python run_in_parallel.py --command_line_args="${TEST_ARGS}" --test_tags "${TEST_TAGS}"

rasrm_business_acceptance_tests: TEST_TARGET = acceptance_tests/features
rasrm_business_acceptance_tests: TEST_TAGS = ~@secure_messaging ~@social
rasrm_business_acceptance_tests:
	pipenv run behave --stop --format ${BEHAVE_FORMAT} --tags ${TEST_TAGS} ${TEST_TARGET}

social_acceptance_tests: TEST_TARGET = acceptance_tests/features
social_acceptance_tests: TEST_TAGS = @social
social_acceptance_tests: setup
social_acceptance_tests:
	pipenv run behave --stop --format ${BEHAVE_FORMAT} --tags ${TEST_TAGS} ${TEST_TARGET}

secure_messaging_acceptance_tests: TEST_TARGET = acceptance_tests/features
secure_messaging_acceptance_tests: TEST_TAGS = @secure_messaging
secure_messaging_acceptance_tests:
	pipenv run behave --stop --format ${BEHAVE_FORMAT} --tags ${TEST_TAGS} ${TEST_TARGET}

run_tests:
	pipenv run behave --stop --format ${BEHAVE_FORMAT} ${TEST_TARGET}
