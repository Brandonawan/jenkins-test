pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Test') {
            steps {
                sh 'python test.py > test-result.txt'
            }
        }

        stage('Check Results') {
            steps {
                script {
                    // Read the test results from a file or environment variable.
                    def testResult = readFile 'test-result.txt'

                    // Check if the test failed.
                    if (testResult.contains('FAILED')) {
                        // Rollback the changes if the test failed.
                        withCredentials([string(credentialsId: 'github-token', variable: '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')]) {
                            sh "curl -H 'Authorization: token ${GITHUB_TOKEN}' -X POST -d '{\"sha\":\"${env.GIT_COMMIT}\",\"force\":\"true\"}' https://api.github.com/repos/${env.GIT_URL#*/}/git/refs/heads/${env.BRANCH_NAME}"
                        }
                    } else {
                        // Commit the changes if the test passed.
                        sh 'git commit -m "Fix issue in sample.py"'
                        sh 'git push origin ${env.BRANCH_NAME}'
                    }
                }
            }
        }
    }
}
