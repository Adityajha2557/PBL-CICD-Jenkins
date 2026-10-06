pipeline {
    agent any

    environment {
        IMAGE_NAME = "pbl-cicd-app"
        IMAGE_TAG = "latest"
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                bat 'docker build -t %IMAGE_NAME%:%IMAGE_TAG% .'
            }
        }

        stage('Deploy to Kubernetes') {
    steps {
        echo 'Deploying application to Kubernetes...'
        bat 'set KUBECONFIG=C:\\Users\\shrek\\.kube\\config && kubectl apply -f k8s/deployment.yaml'
        bat 'set KUBECONFIG=C:\\Users\\shrek\\.kube\\config && kubectl apply -f k8s/service.yaml'
    }
}

        sstage('Verify Deployment') {
    steps {
        echo 'Checking Kubernetes deployment...'
        bat 'set KUBECONFIG=C:\\Users\\shrek\\.kube\\config && kubectl get pods'
        bat 'set KUBECONFIG=C:\\Users\\shrek\\.kube\\config && kubectl get services'
    }
}

    post {
        success {
            echo 'CI/CD Pipeline completed successfully!'
        }

        failure {
            echo 'CI/CD Pipeline failed!'
        }
    }
}