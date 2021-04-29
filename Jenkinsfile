pipeline{
 agent any
 stages {
  stage("build") {
    steps {
      sh "Creando imagen Docker ..."
      sh "docker build -t dockerImage ."
      sh "Imagen Docker creada"
    }
  }
  stage("run") {
    steps {
      sh "Ejecutando imagen de Docker"
      sh "docker run --rm dockerImage"
    }
  }
}
}
