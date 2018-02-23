RM_TOOLS_REPO_URL = https://github.com/ONSdigital/rm-tools.git
RAS_RM_REPO_URL = https://github.com/ONSdigital/ras-rm-docker-dev.git

.PHONY: test system_tests acceptance_tests

install:
	pipenv install --dev

start_services:
	if [ -d tmp_ras_rm_docker_dev ]; then \
		echo "tmp_ras_rm_docker_dev exists - pulling"; \
		cd tmp_rm_tools; git pull; cd -; \
	else \
		git clone --depth 1 ${RAS_RM_REPO_URL} tmp_ras_rm_docker_dev; \
	fi; \
	cd tmp_ras_rm_docker_dev\
	&& make pull && make up
	pipenv run python wait_until_services_up.py

stop_services:
	if [ -d tmp_ras_rm_docker_dev ]; then \
		echo "tmp_ras_rm_docker_dev exists"; \
	else \
		git clone --depth 1 ${RAS_RM_REPO_URL} tmp_ras_rm_docker_dev; \
	fi; \
	cd tmp_ras_rm_docker_dev\
	&& make down
	rm -rf tmp_ras_rm_docker_dev

setup:
	# Setting up initial data required for acceptance tests
	if [ -d tmp_rm_tools ]; then \
		echo "tmp_rm_tools exists - pulling"; \
	 	cd tmp_rm_tools; git pull; cd -; \
	else \
		git clone --depth 1 ${RM_TOOLS_REPO_URL} tmp_rm_tools; \
	fi; \
	cd tmp_rm_tools/collex-loader\
	&& pipenv run python load.py config/collex-config.json\
	&& pipenv run python load_events.py config/event-config.json\
	&& cd ../..\
	&& rm -rf tmp_rm_tools
	pipenv run python set_up_ce_execution.py
	# Acceptance tests can now be run

system_tests:
	pipenv run behave system_tests/features # This will only run the system tests

acceptance_tests: system_tests
	pipenv run behave acceptance_tests/features # This will only run the acceptance tests

test: start_services setup acceptance_tests stop_services
