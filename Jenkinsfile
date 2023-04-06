pipeline {
    agent any
    environment {
        GIT_COMMITTER_NAME = 'Jenkins'
        GIT_COMMITTER_EMAIL = 'jenkins@example.com'
        GIT_AUTHOR_NAME = 'Jenkins'
        GIT_AUTHOR_EMAIL = 'jenkins@example.com'
    }
    stages {
        stage('Checkout SCM') {
            steps {
                checkout([$class: 'GitSCM',
                          branches: [[name: 'main']],
                          doGenerateSubmoduleConfigurations: false,
                          extensions: [],
                          submoduleCfg: [],
                          userRemoteConfigs: [[url: 'https://github.com/Brandonawan/jenkins-test.git']]])
            }
        }
        stage('Revert') {
            steps {
                sh 'git checkout -b revert-branch HEAD' // create new branch
                sh 'git revert HEAD' // revert the changes
                sh 'git push origin revert-branch' // push the changes to the new branch
            }
        }
        stage('Post Actions') {
            steps {
                echo 'Done!'
            }
        }
    }
}
