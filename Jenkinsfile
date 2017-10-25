#!/usr/bin/env groovy

pipeline {

    agent {
        docker {
            image 'python:latest'
            args '-u root'
        }
    }

    stages {
        stage('clone') {
            steps {
                git url: "https://github.com/ONSdigital/ras-integration-tests.git", branch: "testing-info-endpoints"
            }
        }
        stage('pip install') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('test') {
            steps {
                sh 'behave'
            }
        }
    }
}
