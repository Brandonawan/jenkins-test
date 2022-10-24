pipeline {
    agent any 
    stages {
        stage('Stage 1') {
            steps {
                echo 'Pulling... ' + env.GIT_BRANCH
                def getGitBranchName() {
                return scm.branches[0].name
                }
            }
        }
    }
}
