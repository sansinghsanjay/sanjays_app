pipeline {
  agent any
  environment {
    APP_NAME = 'app'
    APP_PORT = '8501'            // change to your app port
    IMAGE = "app:${env.GIT_COMMIT.take(7)}"
  }
  triggers { pollSCM('') } // optional; GitHub hook is primary trigger
  stages {
    stage('Checkout') {
      steps { checkout scm }
    }
    stage('Build image') {
      steps {
        sh '''
          docker build -t $IMAGE .
        '''
      }
    }
    stage('Stop old container') {
      steps {
        sh '''
          if [ "$(docker ps -q -f name=$APP_NAME)" ]; then docker stop $APP_NAME; fi
          if [ "$(docker ps -aq -f name=$APP_NAME)" ]; then docker rm $APP_NAME; fi
        '''
      }
    }
    stage('Run new container') {
      steps {
        sh '''
          docker run -d --name $APP_NAME -p ${APP_PORT}:${APP_PORT} --restart=always $IMAGE
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
    failure { echo 'Build failed. Check console output.' }
  }
}