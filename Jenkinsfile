
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
    stage("test"){
      steps {
        script{
          sh "echo 2845 | sudo -S sudo apt install python3-pip"
          sh "echo 2845 | sudo -S sudo pip3 install flake8 pytest pytest-cov"
          sh "pytest pruebas.py"
        }
      }
    }
   /* stage("build") {
      steps {
        sh "echo 2845 | sudo -S docker build -t python_script . "
      }
    }
    stage("run") {
      steps {
        sh "echo 2845 | sudo -S docker build -t python_script . "
      }
    }*/
  }
  /*post{
    success{
      emailext (
          subject: "Fallo en la pipeline del proyecto: ${gitRepoName}",
            body: "La build de ${env.BUILD_URL} se ha completado",
            to: "Jorge.Munoz9@alu.uclm.es"
       )
    }
    failure{
        emailext (
          subject: "Fallo en la pipeline del proyecto: ${gitRepoName}",
            body: "La build de ${env.BUILD_URL} ha fallado",
            to: "Jorge.Munoz9@alu.uclm.es"
       )
    }
  }*/
}
