pipeline {
    agent any
    stages {
        stage('Clone') {
            steps {
                git branch: 'development',
                    url: ' https://github.com/MaryamCodeHub/TaskFlow.git
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'python -m pytest tests/'
            }
        }
    }
    post {
        success { echo 'Build Passed!' }
        failure { echo 'Build Failed!' }
    }
}
