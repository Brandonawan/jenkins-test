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
            publishHTML([
              allowMissing: false,
              alwaysLinkToLastBuild: false,
              keepAll: false,
              reportDir: target,
              reportFiles: 'surefire-report.html',
              reportName: 'Surefire Report',
              reportTitles: '',
            ])
          }
      }
    }
  }
}
