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
                        try {
                            sh "git revert --no-edit -m 1 ${lastCommit}"
                        } catch (Exception ex) {
                            echo "Failed to revert commit: ${lastCommit}. ${ex.getMessage()}"
                        }
                    }
                }
            }
        }
        stage('Build and test') {
            steps {
                try {
                    sh 'python hello_world.py'
                } catch (Exception ex) {
                    error("Build failed. ${ex.getMessage()}")
                }
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
                try {
                    sh "git revert --no-edit -m 1 ${lastCommit}"
                } catch (Exception ex) {
                    echo "Failed to revert commit: ${lastCommit}. ${ex.getMessage()}"
                }
            }
        }
    }
}
