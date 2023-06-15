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
        sh 'python3 chrome.py'
      }
      post {
            success {
            publishHTML ([
              allowMissing: false,
              alwaysLinkToLastBuild: false,
              keepAll: true,
              reportDir: 'coverage',
              reportFiles: 'index.html',
              reportName: "RCov Report"
            ])
          }
      }
    }
  }
}
