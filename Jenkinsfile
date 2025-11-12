pipeline {
  agent any
  environment {
    COMPOSE_PROJECT_NAME = 'sanjays_app'   // optional: custom prefix for container names
  }
  triggers { pollSCM('') } // optional
  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Build and Run with Docker Compose') {
      steps {
        sh '''
          docker compose down || true
          docker compose build --no-cache
          docker compose up -d
        '''
      }
    }

    stage('Cleanup old images') {
      steps {
        sh 'docker image prune -f || true'
      }
    }
  }

  post {
    success {
      echo '✅ App is up via Docker Compose!'
    }
    failure {
      echo '❌ Build failed. Check logs.'
    }
  }
}
