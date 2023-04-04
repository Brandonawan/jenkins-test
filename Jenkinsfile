pipeline {
    agent any

    stages {
        stage('Check Python script') {
            steps {
                script {
                    def scriptExists = sh (
                        script: "test -e hello_world.py && echo 'exists' || echo 'does not exist'",
                        returnStdout: true
                    ).trim()
                    if (scriptExists == 'does not exist') {
                        def lastCommit = sh (
                            script: "git log --pretty=format:'%H' -n 1",
                            returnStdout: true
                        ).trim()
                        sh "git revert --no-edit ${lastCommit}"
                    }
                }
            }
        }
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
