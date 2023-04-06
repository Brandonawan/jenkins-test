pipeline {
    agent any
    
    stages {
        stage('Checkout SCM') {
            steps {
                checkout([$class: 'GitSCM',
                    branches: [[name: '*/main']],
                    doGenerateSubmoduleConfigurations: false,
                    extensions: [],
                    submoduleCfg: [],
                    userRemoteConfigs: [[url: 'https://github.com/Brandonawan/jenkins-test.git']]]

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
