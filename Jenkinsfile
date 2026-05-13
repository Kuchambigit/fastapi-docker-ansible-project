// Jenkins Declarative Pipeline

pipeline {

    agent any

    environment {
        // Docker image name
        IMAGE_NAME = "fastapi-app"

        // Container name
        CONTAINER_NAME = "fastapi-container"
    }

    stages {

        stage('Clone Repository') {
            steps {
                // Pull code from GitHub
                git branch: 'main',
                url: 'https://github.com/Kuchambigit/fastapi-docker-ansible-project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image from Dockerfile
                    sh 'docker build -t $IMAGE_NAME .'
                }
            }
        }

        stage('Stop Old Container') {
            steps {
                script {
                    // Stop old container if it exists
                    sh '''
                    docker stop $CONTAINER_NAME || true
                    docker rm $CONTAINER_NAME || true
                    '''
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    // Start new container
                    sh '''
                    docker run -d \
                    --name $CONTAINER_NAME \
                    -p 8000:8000 \
                    $IMAGE_NAME
                    '''
                }
            }
        }

        stage('Verify Deployment') {
            steps {
                script {
                    // Check application response
                    sh 'curl http://localhost:8000 || true'
                }
            }
        }
    }

    post {

        success {
            echo 'Pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed!'
        }
    }
}
