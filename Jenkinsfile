pipeline {
  agent any
  stages {
    stage('Install Dependencies') {
      steps {
        sh "python3 --version"
        sh "python3 -m pip install --upgrade pip"
        sh 'pip install webdriver-manager'
      }
    }
    stage('Run Selenium Script') {
      steps {
        sh 'python3 chrome.py'
      }
    }
  }
}
