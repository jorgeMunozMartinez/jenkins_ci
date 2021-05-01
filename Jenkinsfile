
pipeline {
  agent { label "master" }
  stages {
    stage("build") {
      steps {
        sh "sudo -S 2845 docker build -t hello_there ."
      }
    }
    stage("run") {
      steps {
        sh "sudo -S 2845 docker run --rm hello_there"
      }
    }
  }
}
