pipeline {
    agent any

    stages {
        stage('Build and test') {
            steps {
                sh 'python hello_world.py'
            }
        }
    }

    post {
        success {
            script {
                def lastCommit = sh (
                    script: "git log --pretty=format:'%H' -n 1",
                    returnStdout: true
                ).trim()
                def status = sh (
                    script: "git status",
                    returnStatus: true
                )
                if (status != 0) {
                    sh "git revert --no-edit ${lastCommit}"
                }
            }
        }
    }
}
