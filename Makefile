
.PHONY: system_tests acceptance_tests

system_tests:
	pipenv run behave system_tests/features # This will only run the system tests

acceptance_tests:
	pipenv run behave acceptance_tests/features # This will only run the acceptance tests

install:
	pipenv install --dev
