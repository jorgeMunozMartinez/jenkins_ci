
pipeline {
  docker { image 'node:14-alpine' }
  stages {
    stage("build") {
      steps {
        sh """
          docker build -t script .
        """
      }
    }
    stage("run") {
      steps {
        sh """
          docker run --rm script
        """
      }
    }
  }
}
