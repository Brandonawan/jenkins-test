pipeline {
    agent any
    
    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }
        
        stage('Revert') {
            steps {
                sh 'git revert HEAD'
            }
        }
        
        stage('Post Actions') {
            steps {
                sh 'git push --force'
            }
        }
    }
}
