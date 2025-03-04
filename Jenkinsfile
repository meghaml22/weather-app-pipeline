pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/your-repo/weather-api.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("weather-api:latest")
                }
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest tests/test_app.py'
            }
        }

        stage('Deploy Container') {
            steps {
                sh 'docker run -d -p 5000:5000 weather-api:latest'
            }
        }
    }
}
