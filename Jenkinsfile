#!/usr/bin/env groovy
pipeline {

    agent { docker { image 'python:latest' } }
    stages {
        stage('Clone') {
            agent { docker { image 'python:latest' } }
            steps {
                git url: "https://github.com/ONSdigital/ras-integration-tests.git", branch: "testing-info-endpoints"
            }
        }
        stage('Test') {
          agent { docker { image 'python:latest' } }
            steps {
                sh 'docker ps'
                // sh 'pip install -r requirements.txt'
                // git sh 'behave'
            }
        }
    }
}
