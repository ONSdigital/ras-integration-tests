
RM_TOOLS_REPO_URL = git@github.com:ONSdigital/rm-tools.git

.PHONY: system_tests acceptance_tests

system_tests: tmp_rm_tools 
	pipenv run behave system_tests/features # This will only run the system tests

acceptance_tests: system_tests
	pipenv run behave acceptance_tests/features # This will only run the acceptance tests

install:
	pipenv install --dev

tmp_rm_tools: 
	git clone ${RM_TOOLS_REPO_URL} tmp_rm_tools
	cd tmp_rm_tools/collex-loader;python load.py config/app-config.json

clean:
	rm -rf tmp_rm_tools
