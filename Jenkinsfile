pipeline {
  agent any
  stages {
    stage('Install Dependencies') {
      steps {
        sh "python3 --version"
        // sh "python3 -m pip install --upgrade pip"
        sh 'pip3 install webdriver-manager'
        sh 'pip3 install selenium'
      }
    }
    stage('Run Selenium Script') {
      steps {
        sh 'python3 chrome4.py'
      }
      post {
            success {
              script {
            // Define the HTML report directory and file
            def reportDir = 'target'
            def reportFile = 'surefire-report.html'

            publishHTML([
              allowMissing: false,
              alwaysLinkToLastBuild: false,
              keepAll: false,
              reportDir: reportDir,
              reportFiles: reportFile,
              reportName: 'Surefire Report',
              reportTitles: '',
            ])
          }
      }
    }
  }
}
