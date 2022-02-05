pipeline {
    agent any
    environment {
        REGISTRY = "localhost:5000"
        PROD = "<Prod-IP>:<Docker-Port>"
    }
    stages {
        stage('Verify') {
            steps {
                sh 'chmod +x ./CICD/scripts/00-verify.sh'
                sh './CICD/scripts/00-verify.sh'
            }
        }
        stage('Build') {
            steps {
                sh 'chmod +x ./CICD/scripts/01-build.sh'
                sh './CICD/scripts/01-build.sh'
            }
        }
        stage('Test') {
            steps {
                sh 'chmod +x ./CICD/scripts/02-test.sh'
                sh './CICD/scripts/02-test.sh'
            }
        }
        stage('Push') {
            steps {
                sh 'chmod +x ./CICD/scripts/03-push.sh'
                sh './CICD/scripts/03-push.sh'
            }
        }
        stage('Await approval') {
            steps {
                input message: 'Deploy to prod?', ok: 'Do it!'
            }
        }
        stage('Deploy') {
            steps {
                withCredentials([
                    file(credentialsId: 'docker-ca.pem', variable: 'ca'),
                    file(credentialsId: 'docker-cert.pem', variable: 'cert'),
                    file(credentialsId: 'docker-key.pem', variable: 'key')
                ]) {
                    sh 'chmod +x ./CICD/scripts/04-deploy.sh'
                    sh './CICD/scripts/04-deploy.sh'
                }
            }
        }
    }
}
