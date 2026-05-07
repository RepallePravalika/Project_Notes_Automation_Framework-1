pipeline {
    agent any

    stages {
        stage('Checkout Source Code') {
            steps {
                git branch: 'main', 
                    url: 'https://github.com/RepallePravalika/Notes_Automation_Framework_.git'
            }
        }

        stage('Install Python Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Parallel Test Execution') {
            steps {
                // We use catchError to ensure that even if tests fail, 
                // the subsequent stages for report collection and artifact uploading will run.
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    bat 'pytest -n 2 -v --html=reports/report.html --self-contained-html'
                }
            }
        }
    }

    post {
        always {
            script {
                echo 'CI/CD Pipeline: Capturing Reports and Artifacts...'
                
                // Archiving everything as per requirement 4 and 5
                // This includes the HTML report, screenshots of any failures, and execution logs.
                archiveArtifacts artifacts: 'reports/report.html, screenshots/*.png, logs/*.log', 
                                 fingerprint: true, 
                                 allowEmptyArchive: true
                
                echo 'Artifacts uploaded successfully. You can download them from the build dashboard.'
            }
        }
    }
}
