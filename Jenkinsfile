// Jenkins Declarative Pipeline

pipeline {

    agent any

    environment {

        // Docker image name
        IMAGE_NAME = "fastapi-app"

        // DockerHub image name
        DOCKERHUB_IMAGE = "kuchambiatud/fastapi-app:latest"

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

        stage('Push Docker Image') {
            steps {

                // Use Jenkins stored DockerHub credentials
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {

                    script {

                        // Login to DockerHub securely
                        sh '''
                        echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                        '''

                        // Tag Docker image
                        sh '''
                        docker tag $IMAGE_NAME $DOCKERHUB_IMAGE
                        '''

                        // Push Docker image to DockerHub
                        sh '''
                        docker push $DOCKERHUB_IMAGE
                        '''
                    }
                }
            }
        }

        stage('Deploy with Ansible') {
    steps {
        script {

            // Run Ansible deployment playbook
            sh 'ansible-playbook ansible/deploy.yml'

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
