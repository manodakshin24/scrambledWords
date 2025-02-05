pipeline {
    agent any 

    stages {
        stage('Checkout') {
            steps {
                // Checkout code from the repository
                checkout scm
            }
        }
        stage('Run Script') {
            steps {
                // Run the Python script
                sh 'echo "Running the Python script..."'
                sh 'python3 scrambledWordScript.py' // Replace with the actual script name if different
            }
        }
    }
}
