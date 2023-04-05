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
                // Start the app in the background
                sh 'npm start &'
            }

            // Wait for the app to start up
            // You may need to adjust the delay based on your app's startup time
            post {
                always {
                    sleep time: 10, unit: 'SECONDS'
                }
            }

            // Stop the app after 60 seconds
            post {
                always {
                    timeout(time: 60, unit: 'SECONDS') {
                        sh 'npm stop'
                    }
                }
            }
        }
    }
}
