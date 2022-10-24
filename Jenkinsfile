pipeline {
    agent any 
    stages {
        stage('Stage 1') {
            steps {
                echo 'Hello world!' 
                echo 'Pulling... ' + env.GIT_BRANCH
                BRANCH_NAME = "${GIT_BRANCH.split("/")[1]}"
                echo 'Pulling... ' + BRANCH_NAME
                
            }
        }
    }
}
