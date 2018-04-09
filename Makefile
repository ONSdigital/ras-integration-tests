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

setup:
	./setup_data.sh ${RM_TOOLS_REPO_URL}

system_tests:
	pipenv run behave --format progress2 system_tests/features # This will only run the system tests

acceptance_tests:
	pipenv run behave --format progress2 acceptance_tests/features # This will only run the acceptance tests
