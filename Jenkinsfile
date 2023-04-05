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
                          userRemoteConfigs: [[url: 'https://github.com/username/my-node-app.git']]])
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
                // Start the app
                sh 'npm start'
            }

            // Wait for the app to start up
            // You may need to adjust the delay based on your app's startup time
            post {
                always {
                    sleep time: 10, unit: 'SECONDS'
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
