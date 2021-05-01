
def gitRepoName
pipeline {
  agent { label "master" }
  stages {
    stage("init"){
      steps {
        script{
          gitRepoName = scm.getUserRemoteConfigs()[0].getUrl().tokenize('/').last().split("\\.")[0]
        }
      }
    }
    stage("build") {
      steps {
        sh "echo 2845 | sudo -S docker build -t python_script . "
      }
    }
    stage("run") {
      steps {
        sh "echo 2845 | sudo -S docker build -t python_script . "
      }
    }
  }
  post{
    success{
      emailext (
          subject: "Fallo en la pipeline del proyecto: ${gitRepoName}",
            body: "La build de ${env.BUILD_URL} se ha completado",
            to: "jmunozmar@minsait.com"
       )
    }
    failure{
        emailext (
          subject: "Fallo en la pipeline del proyecto: ${gitRepoName}",
            body: "La build de ${env.BUILD_URL} ha fallado",
            to: "jmunozmar@minsait.com"
       )
    }
  }
}
