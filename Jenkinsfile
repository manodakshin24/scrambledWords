pipeline {
    agent any

    parameters {
        choice(name: 'DIFFICULTY', choices: ['Beginner', 'Intermediate', 'Advanced', 'Expert'], description: 'Select difficulty level')
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout code from the repository
                checkout scm
            }
        }
        stage('Select Difficulty') {
            steps {
                // Prompt the user to select the difficulty level
                script {
                    params.DIFFICULTY = input(message: 'Select the difficulty level:', parameters: [choice(name: 'DIFFICULTY', choices: ['Beginner', 'Intermediate', 'Advanced', 'Expert'], description: 'Select difficulty level')])
                }
            }
        }
        stage('Run Script') {
            steps {
                // Run the Python script with the selected difficulty level
                sh 'echo "Running the Python script..."'
                sh "python3 scrambledWordScript.py ${params.DIFFICULTY}"
            }
        }
    }
}
