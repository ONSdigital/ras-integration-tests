#!/usr/bin/env groovy

pipeline {

    agent {
        docker {
            image 'python:latest'
            args '-u root'
        }
    }


    tools {nodejs "Node 6.10.3"}

    stages {
        stage('clone') {
            steps {
                git url: "https://github.com/ONSdigital/ras-integration-tests.git", branch: "${env.BRANCH_NAME}"
            }
        }
        stage('pip install') {

            steps {
                sh 'pip install pipenv'
                sh 'pipenv install --dev'
                sh 'npm install -g phantomjs-prebuilt'
            }
        }
        stage('system tests') {
            environment {
                RESPONSE_OPERATIONS_UI_SUFFIX = credentials('CF_DOMAIN_SUFFIX')
                RESPONSE_OPERATIONS_UI_HOST = "response-operations-ui-python-int${RESPONSE_OPERATIONS_UI_SUFFIX}"
                RESPONSE_OPERATIONS_UI_PORT = "80"
                SECURE_MESSAGE_SERVICE_HOST = "ras-secure-messaging-int${RESPONSE_OPERATIONS_UI_SUFFIX}"
                SECURE_MESSAGE_SERVICE_PORT = "80"
                FRONTSTAGE_SERVICE_HOST = "ras-frontstage-int${RESPONSE_OPERATIONS_UI_SUFFIX}"
                FRONTSTAGE_SERVICE_PORT = "80"
                BACKSTAGE_SERVICE_HOST = "ras-backstage-service-int${RESPONSE_OPERATIONS_UI_SUFFIX}"
                BACKSTAGE_SERVICE_PORT = "80"
                PARTY_SERVICE_HOST = "ras-party-service-int${RESPONSE_OPERATIONS_UI_SUFFIX}"
                PARTY_SERVICE_PORT = "80"
                COLLECTION_INSTRUMENT_SERVICE_HOST = "ras-collection-instrument-int${RESPONSE_OPERATIONS_UI_SUFFIX}"
                COLLECTION_INSTRUMENT_SERVICE_PORT = "80"
                DJANGO_SERVICE_HOST = "ras-django-int${RESPONSE_OPERATIONS_UI_SUFFIX}"
                DJANGO_SERVICE_PORT = "80"
                ACTION_SERVICE_HOST = "actionsvc-int${RESPONSE_OPERATIONS_UI_SUFFIX}"
                ACTION_SERVICE_PORT = "80"
                ACTION_EXPORTER_HOST = "actionexportersvc-int${RESPONSE_OPERATIONS_UI_SUFFIX}"
                ACTION_EXPORTER_PORT = "80"
                BACKSTAGE_UI_HOST = "ras-backstage-int${RESPONSE_OPERATIONS_UI_SUFFIX}"
                BACKSTAGE_UI_PORT = "80"
                CASE_SERVICE_HOST = "casesvc-int${RESPONSE_OPERATIONS_UI_SUFFIX}"
                CASE_SERVICE_PORT = "80"
                COLLECTION_EXERCISE_SERVICE_HOST = "collectionexercisesvc-int${RESPONSE_OPERATIONS_UI_SUFFIX}"
                COLLECTION_EXERCISE_SERVICE_PORT = "80"
                FRONTSTAGE_API_SERVICE_HOST = "ras-frontstage-api-int${RESPONSE_OPERATIONS_UI_SUFFIX}"
                FRONTSTAGE_API_SERVICE_PORT = "80"
                IAC_SERVICE_HOST = "iacsvc-int${RESPONSE_OPERATIONS_UI_SUFFIX}"
                IAC_SERVICE_PORT = "80"
                NOTIFY_GATEWAY_SERVICE_HOST = "notifygatewaysvc-int${RESPONSE_OPERATIONS_UI_SUFFIX}"
                NOTIFY_GATEWAY_SERVICE_PORT = "80"
                SAMPLE_SERVICE_HOST = "samplesvc-int${RESPONSE_OPERATIONS_UI_SUFFIX}"
                SAMPLE_SERVICE_PORT = "80"
                SURVEY_SERVICE_HOST = "surveysvc-int${RESPONSE_OPERATIONS_UI_SUFFIX}"
                SURVEY_SERVICE_PORT = "80"
            }
            steps {
                sh 'pipenv run behave --no-skipped system_tests/features'
            }
        }
        stage('acceptance tests') {
            environment {
                RESPONSE_OPERATIONS_UI_SUFFIX = credentials('CF_DOMAIN_SUFFIX')
                RESPONSE_OPERATIONS_UI_HOST = "response-operations-ui-python-int${RESPONSE_OPERATIONS_UI_SUFFIX}"
                RESPONSE_OPERATIONS_UI_PORT = "80"
            }
            steps {
                sh 'env'
                sh 'pipenv run behave --no-skipped acceptance_tests/features'
            }
        }
    }
}
