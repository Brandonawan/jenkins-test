// pipeline {
//   agent any
//   stages {
//     stage('Install Dependencies') {
//       steps {
//         sh "python3 --version"
//         // sh "python3 -m pip install --upgrade pip"
//         sh 'pip3 install webdriver-manager'
//         sh 'pip3 install selenium'
//       }
//     }
//     stage('Run Selenium Script') {
//       steps {
//         sh 'python3 chrome4.py'
//       }
//     }
//   }
// }

pipeline {
  agent any
  environment {
    VIRTUAL_ENV = "${WORKSPACE}/venv"
    PATH = "${VIRTUAL_ENV}/bin:${PATH}"
  }
  stages {
    stage('Create Virtual Environment') {
      steps {
        script {
          // Check if the virtual environment already exists
          def venvExists = sh (
            returnStdout: true,
            script: "test -d ${VIRTUAL_ENV} && echo 'true' || echo 'false'"
          ).trim()
          if (venvExists == 'true') {
            // Delete the existing virtual environment
            sh "rm -rf ${VIRTUAL_ENV}"
          }
          
          // Create a new virtual environment
          sh "python3 -m venv ${VIRTUAL_ENV}"
          
          // Activate the virtual environment
          sh ". ${VIRTUAL_ENV}/bin/activate"
        }
      }
    }
    stage('Install Dependencies') {
      steps {
        sh "python3 --version"
        sh "pip3 install --upgrade pip"
        sh "pip3 install -r requirements.txt"
      }
    }
    stage('Run Selenium Script') {
      steps {
        sh 'python3 hello.py'
      }
    }
  }
}
