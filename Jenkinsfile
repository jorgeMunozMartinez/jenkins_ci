
pipeline {
  agent { label "master" }
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
