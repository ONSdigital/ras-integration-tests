#!/usr/bin/env groovy
pipeline {

    agent {
        docker { image 'python:latest' }
    }

    stages {
        stage('Clone') {
            steps {
                git url: "https://github.com/ONSdigital/ras-integration-tests.git", branch: "testing-info-endpoints"
            }
        }
        stage('Test') {
            steps {
                sh 'whoami'
                sh 'pip install -r requirements.txt'
                sh 'behave'
            }
        }
    }
}
