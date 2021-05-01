
pipeline {
  agent { label "master" }
  stages {
    stage("build") {
      steps {
        sh "echo admin | sudo -S ls admin docker build -t hello_there ."
      }
    }
    stage("run") {
      steps {
        sh "sudo admin docker run --rm hello_there"
      }
    }
  }
}
