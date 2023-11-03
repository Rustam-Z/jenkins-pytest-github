
/* Requires the Docker Pipeline plugin */
pipeline {
    agent { docker { image 'python:3.12.0-alpine3.18' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
                sh '''
                        python3 -m venv env
                        source env/bin/activate
                        pip install -r requirements.txt
                        export PYTHONPATH="${PYTHONPATH}:./src"
                '''
            }
        }
        stage('test'){
            steps{
                sh '''
                pytest
                '''
            }
        }
    }
}
