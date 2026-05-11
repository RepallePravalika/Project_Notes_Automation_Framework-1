1. Create Virtual Environment
python -m venv venv
2. Activate Virtual Environment
venv\Scripts\activate
3. Start Selenium Grid using Docker
Open Docker Desktop First

Then run:

docker compose up -d
4. If Selenium Hub is Already in Use
docker rm -f selenium-hub

Then again run:

docker compose up -d
5. Run Tests in Parallel
pytest -n 4
6. Generate HTML Report
pytest --html=reports/report.html --self-contained-html
7. Generate Allure Raw Results
pytest --alluredir=reports/allure-results
8. Serve Allure Report
allure serve reports/allure-results
9. Run Last Failed Tests
pytest --lf
10.Stop Selenium Grid
docker compose down
