pipeline {
  agent any
  stages {
    stage('Install Dependencies') {
      steps {
        sh 'pip install webdriver-manager'
      }
    }
    stage('Run Selenium Script') {
      steps {
        sh 'python3 selenium_script.py'
      }
    }
  }
}
