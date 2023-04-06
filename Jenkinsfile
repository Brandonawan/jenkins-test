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
                // Install the dependencies
                sh 'npm install'
            }
        }

        stage('Run') {
            steps {
                // Start the app with a 2-minute timeout
                timeout(time: 2, unit: 'MINUTES') {
                    sh 'npm start'
                }
            }
        }
    }

    post {
        always {
            // Stop the app
            sh 'npm stop'
        }
    }
}
