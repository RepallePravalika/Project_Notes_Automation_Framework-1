pipeline {

    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/RepallePravalika/Project_Notes_Automation_Framework.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Delete old venv if exists
                bat 'if exist venv rmdir /s /q venv'

                // Create fresh virtual environment
                bat 'python -m venv venv'

                // Upgrade pip
                bat 'venv\\Scripts\\python -m pip install --upgrade pip'

                // Install requirements
                bat 'venv\\Scripts\\python -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests (Parallel)') {
            steps {
                // Create reports directory if it doesn't exist
                bat 'if not exist reports mkdir reports'

                // Continue pipeline even if tests fail
                catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE') {
                    bat '''
                    venv\\Scripts\\python -m pytest ^
                    -n 2 ^
                    --alluredir=allure-results ^
                    --html=reports/report.html ^
                    --self-contained-html
                    '''
                }
            }
        }
    }

    post {
        always {
            script {
                echo 'CI/CD Pipeline: Capturing Reports and Artifacts...'

                // Generate Allure Report gracefully
                try {
                    allure([
                        includeProperties: false,
                        jdk: '',
                        results: [[path: 'allure-results']]
                    ])
                } catch (Exception e) {
                    echo "WARNING: Allure report generation failed. Error: ${e.message}"
                    echo "Please configure 'Allure Commandline' in Jenkins Global Tool Configuration if you want Allure reports."
                }

                // Publish HTML Report
                publishHTML(target: [
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: 'reports',
                    reportFiles: 'report.html',
                    reportName: 'Pytest HTML Report'
                ])

                // Archive Artifacts
                archiveArtifacts(
                    artifacts: 'reports/report.html, allure-results/**, screenshots/**, logs/**',
                    fingerprint: true,
                    allowEmptyArchive: true
                )
            }
        }
    }
}
