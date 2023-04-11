pipeline {
    agent any
    stages {
         stage('Checkout') {
            steps {
                // Checkout the code from Git
                checkout([$class: 'GitSCM', 
                          branches: [[name: '*/main']], 
                          doGenerateSubmoduleConfigurations: false, 
                          extensions: [], 
                          submoduleCfg: [], 
                          userRemoteConfigs: [[url: 'https://github.com/Brandonawan/jenkins-test.git']]])
            }
        }
        stage('Build') {
            steps {
                sh 'npm install'
            }
        }
    }
    post {
        failure {
            // Revert the commit if the build fails
            sh 'git reset --hard HEAD^'
            sh 'git push --force'
        }
    }
}
