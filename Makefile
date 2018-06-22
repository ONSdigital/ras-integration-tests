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

setup: clean
	./setup_data.sh ${RM_TOOLS_REPO_URL}

# If you want to run a single feature file WITHOUT setup first use:
# make TEST_TARGET=acceptance_tests/features/your.feature run_tests
#
# If you want to run a single feature file WITH setup first use:
# make TEST_TARGET=acceptance_tests/features/your.feature acceptance_tests
BEHAVE_FORMAT = progress2

system_tests: TEST_TARGET = system_tests/features  # This will only run the system tests
system_tests: run_tests

acceptance_tests: TEST_TARGET = acceptance_tests/features  # This will only run the acceptance tests
acceptance_tests: setup
	pipenv run behave --format ${BEHAVE_FORMAT} ${TEST_TARGET}

rasrm_acceptance_tests: TEST_TARGET = acceptance_tests/features
rasrm_acceptance_tests: TEST_TAGS = ~@secure_messaging
rasrm_acceptance_tests:
	pipenv run behave --format ${BEHAVE_FORMAT} --tags ${TEST_TAGS} ${TEST_TARGET}

secure_messaging_acceptance_tests: TEST_TARGET = acceptance_tests/features
secure_messaging_acceptance_tests: TEST_TAGS = @secure_messaging
secure_messaging_acceptance_tests:
	pipenv run behave --format ${BEHAVE_FORMAT} --tags ${TEST_TAGS} ${TEST_TARGET}

run_tests:
	pipenv run behave --format ${BEHAVE_FORMAT} ${TEST_TARGET}
