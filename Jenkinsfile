pipeline{
    agent any 

    stages{
        stage('Clone Repository'){
            steps{
                echo '===== Pulling source code ====='
                checkout scm

            }
        }

        stage('Build Docker Image'){
            steps{
                echo '===== Building Docker image ====='
                sh 'docker build -t ci-cd-project .'

            }
        }

        stage('Run Tests'){
            steps{
                echo '===== unning pytest inside container ====='
                sh 'docker run -rm ci-cd-project python -m pytest test/ -v'

            }
        }

        stage('Deploy container'){
            steps{
                echo '===== removing old container if exists =====' 
                sh 'docker stop flask-web-app || true'
                sh 'docker rm flask-web-app || true' 
                
                echo '===== Deploying new container =====' 
                sh 'docker run -d \
                    -p 5000:5000 \
                    --name flask-web-app \
                    ci-cd-project '

            }
        }


    }

    post{

        success{
            echo 'Pipeline succeeded. App is live on port 5000'
        }

        failure{
            echo 'Pipeline failed. Review the logs'
        }


    }



}
