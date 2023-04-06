pipeline {
    agent any
    
    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }
        
        stage('Build') {
            steps {
                sh 'npm install'
            }
        }
        
        stage('Run') {
            steps {
                sh 'timeout -k 5s 60s node app.js'
            }
        }
        
        stage('Post Actions') {
            steps {
                sh 'git checkout main'
                sh 'git reset --hard HEAD^'
                sh 'git push --force'
            }
        }
    }
}
