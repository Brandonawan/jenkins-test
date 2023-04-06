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
                sh 'npm start'
            }
        }
        
        stage('Post Actions') {
            steps {
                sh 'git checkout main'
                sh 'git reset --hard HEAD~1'
                sh 'git push --force'
            }
        }
    }
}
