#!/usr/bin/env groovy

pipeline {

    agent {
        docker {
            image 'sdcplatform/python-pipenv-chrome'
            args '-u root --privileged=true'
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
            }
        }
        stage('system tests') {
            environment {
                DOMAIN_SUFFIX = credentials('CF_DOMAIN_SUFFIX')
                RESPONSE_OPERATIONS_UI_HOST = "response-operations-ui-python-ci${DOMAIN_SUFFIX}"
                RESPONSE_OPERATIONS_UI_PORT = "80"
                SECURE_MESSAGE_SERVICE_HOST = "ras-secure-messaging-ci${DOMAIN_SUFFIX}"
                SECURE_MESSAGE_SERVICE_PORT = "80"
                FRONTSTAGE_SERVICE_HOST = "ras-frontstage-ci${DOMAIN_SUFFIX}"
                FRONTSTAGE_SERVICE_PORT = "80"
                BACKSTAGE_SERVICE_HOST = "ras-backstage-service-ci${DOMAIN_SUFFIX}"
                BACKSTAGE_SERVICE_PORT = "80"
                PARTY_SERVICE_HOST = "ras-party-service-ci${DOMAIN_SUFFIX}"
                PARTY_SERVICE_PORT = "80"
                COLLECTION_INSTRUMENT_SERVICE_HOST = "ras-collection-instrument-ci${DOMAIN_SUFFIX}"
                COLLECTION_INSTRUMENT_SERVICE_PORT = "80"
                DJANGO_SERVICE_HOST = "ras-django-ci${DOMAIN_SUFFIX}"
                DJANGO_SERVICE_PORT = "80"
                ACTION_SERVICE_HOST = "actionsvc-ci${DOMAIN_SUFFIX}"
                ACTION_SERVICE_PORT = "80"
                ACTION_EXPORTER_HOST = "actionexportersvc-ci${DOMAIN_SUFFIX}"
                ACTION_EXPORTER_PORT = "80"
                BACKSTAGE_UI_HOST = "ras-backstage-ci${DOMAIN_SUFFIX}"
                BACKSTAGE_UI_PORT = "80"
                CASE_SERVICE_HOST = "casesvc-ci${DOMAIN_SUFFIX}"
                CASE_SERVICE_PORT = "80"
                COLLECTION_EXERCISE_SERVICE_HOST = "collectionexercisesvc-ci${DOMAIN_SUFFIX}"
                COLLECTION_EXERCISE_SERVICE_PORT = "80"
                FRONTSTAGE_API_SERVICE_HOST = "ras-frontstage-api-ci${DOMAIN_SUFFIX}"
                FRONTSTAGE_API_SERVICE_PORT = "80"
                IAC_SERVICE_HOST = "iacsvc-ci${DOMAIN_SUFFIX}"
                IAC_SERVICE_PORT = "80"
                NOTIFY_GATEWAY_SERVICE_HOST = "notifygatewaysvc-ci${DOMAIN_SUFFIX}"
                NOTIFY_GATEWAY_SERVICE_PORT = "80"
                SAMPLE_SERVICE_HOST = "samplesvc-ci${DOMAIN_SUFFIX}"
                SAMPLE_SERVICE_PORT = "80"
                SURVEY_SERVICE_HOST = "surveysvc-ci${DOMAIN_SUFFIX}"
                SURVEY_SERVICE_PORT = "80"
            }
            steps {
                sh 'pipenv run behave --no-skipped system_tests/features'
            }
        }
        stage('acceptance tests') {
            environment {
                DOMAIN_SUFFIX = credentials('CF_DOMAIN_SUFFIX')
                DATABASE_URI = credentials('RM_CF_DATABASE')
                DJANGO_OAUTH_DATABASE_URI = credentials('DJANGO_CF_DATABASE')
                PARTY_DATABASE_URI = credentials('PARTY_CF_DATABASE')
                SECURE_MESSAGE_DATABASE_URI = credentials('SECURE_MESSAGE_CF_DATABASE')
                COLLECTION_INSTRUMENT_DATABASE_URI = credentials('COLLECTION_INSTRUMENT_CF_DATABASE')
                RESPONSE_OPERATIONS_UI_HOST = "response-operations-ui-python-ci${DOMAIN_SUFFIX}"
                RESPONSE_OPERATIONS_UI_PORT = "80"
                CASE_SERVICE_HOST = "casesvc-ci${DOMAIN_SUFFIX}"
                CASE_SERVICE_PORT = "80"
                COLLECTION_EXERCISE_SERVICE_HOST = "collectionexercisesvc-ci${DOMAIN_SUFFIX}"
                COLLECTION_EXERCISE_SERVICE_PORT = "80"
                DJANGO_SERVICE_HOST = "ras-django-ci${DOMAIN_SUFFIX}"
                DJANGO_SERVICE_PORT = "80"
                SECURE_MESSAGE_SERVICE_HOST = "ras-secure-messaging-ci${DOMAIN_SUFFIX}"
                SECURE_MESSAGE_SERVICE_PORT = "80"
                PARTY_SERVICE_HOST = "ras-party-service-ci${DOMAIN_SUFFIX}"
                PARTY_SERVICE_PORT = "80"
                SAMPLE_SERVICE_HOST = "samplesvc-ci${DOMAIN_SUFFIX}"
                SAMPLE_SERVICE_PORT = "80"
                FRONTSTAGE_SERVICE_HOST = "ras-frontstage-ci${DOMAIN_SUFFIX}"
                FRONTSTAGE_SERVICE_PORT = "80"
                COLLECTION_INSTRUMENT_SERVICE_HOST = "ras-collection-instrument-ci${DOMAIN_SUFFIX}"
                COLLECTION_INSTRUMENT_SERVICE_PORT = "80"
                SECURITY_USER_NAME = credentials('SECURITY_USER_NAME')
                SECURITY_USER_PASSWORD = credentials('SECURITY_USER_PASSWORD')
            }
            steps {
                sh 'env'
                sh 'make setup'
                sh 'pipenv run behave --no-skipped acceptance_tests/features'
            }
        }
    }
}
