
RM_TOOLS_REPO_URL = git@github.com:ONSdigital/rm-tools.git

.PHONY: system_tests acceptance_tests

install:
	pipenv install --dev

setup:
	# Setting up initial data required for acceptance tests
	git clone ${RM_TOOLS_REPO_URL} tmp_rm_tools
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
