
pipeline {
  agent { label "master" }
  stages {
    stage("build") {
      steps {
        sh "echo 2845 | sudo -S docker build -t hello_there . "
      }
    }
    stage("run") {
      steps {
        sh "echo 2845 | sudo -S docker build -t hello_there . "
      }
    }
  }
}
