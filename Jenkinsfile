
pipeline {
  agent { label "master" }
  stages {
    stage("build") {
      steps {
        sh "sudo -S admin docker build -t hello_there ."
      }
    }
    stage("run") {
      steps {
        sh "sudo -S admin docker run --rm hello_there"
      }
    }
  }
}
