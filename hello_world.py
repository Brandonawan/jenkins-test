pipeline {
    agent any

    stages {
        stage('Build and test') {
            steps {
                sh 'python hello_world.py' || error("Build failed")
            }
        }
    }

    post {
        failure {
            script {
                def lastCommit = sh (
                    script: "git log --pretty=format:'%H' -n 1",
                    returnStdout: true
                ).trim()
                sh "git revert --no-edit ${lastCommit}"
            }
        }
    }
}
