pipeline {

    agent {
        node {
            label 'master'
        }
    }

    options {
        buildDiscarder logRotator( 
                    daysToKeepStr: '15', 
                    numToKeepStr: '10'
            )
    }

    stages {
        
        stage('Cleanup Workspace') {
            steps {
                cleanWs()
                sh """
                echo "Cleaned Up Workspace For Project"
                """
            }
        }

        stage('Code Checkout') {
            steps {
                checkout([
                    $class: 'GitSCM', 
                    branches: [[name: '*/main']], 
                    userRemoteConfigs: [[url: 'https://github.com/spring-projects/spring-petclinic.git']]
                ])
            }
        }

        stage('Unit Testing') {
            steps {
                sh """
                echo "Running Unit Tests"
                """
            }
        }

        stage('Code Analysis') {
            steps {
                sh """
                echo "Running Code Analysis"
                """
            }
        }

        stage('Build Deploy Code') {
            when {
                branch 'develop'
            }
            steps {
                sh """
                echo "Building Artifact"
                """

                sh """
                echo "Deploying Code"
                """
            }
        }

        stage('Check for Merge to Master') {
            when {
                branch 'main'
            }
            steps {
                // Check if the last commit was a merge to main
                script {
                    def lastCommit = sh(script: 'git log -1 --pretty=format:"%s"', returnStdout: true).trim()
                    if (lastCommit.contains('Merge pull request')) {
                        sh 'git checkout main'
                        sh 'git pull'
                        sh 'git merge --no-ff $GIT_BRANCH'
                        sh 'sh script_to_test_entire_codebase.sh'
                        // If the tests fail, revert the last commit
                        if (sh(script: 'sh script_to_test_entire_codebase.sh', returnStatus: true) != 0) {
                            sh 'git revert HEAD'
                            sh 'git push'
                        }
                    }
                }
            }
        }

    }   
}
