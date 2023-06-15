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
        sh 'python3 chrome2.py'
      }
    }
    stage('Publish HTML Report') {
      steps {
        publishHTML(target: [
          allowMissing: false,
          alwaysLinkToLastBuild: true,
          keepAll: true,
          reportDir: 'target/surefire-reports',
          reportFiles: 'index.html',
          reportName: 'Test Report',
          reportTitles: 'Test Results'
        ])
      }
    }
  }
}
