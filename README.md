# Notes Automation Framework

A production-grade, modular Hybrid UI and API Automation Framework using Python, Selenium, and Pytest. Features include parallel execution, AI-powered failure analysis, and dynamic test data generation.

## 🚀 Getting Started

### 1. Prerequisites
- **Python 3.10+**
- **Google Chrome** (latest version)
- **Allure Commandline** (for advanced reporting)

### 2. Environment Setup
Activate the virtual environment and install dependencies:

```powershell
# Activate venv (Windows)
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configuration
- **AI/LLM Support**: Open the `.env` file and add your `OPENAI_API_KEY`.
- **Base URLs & Credentials**: Check `config/config.yaml` to ensure the application URLs and test accounts are correct.

---

## 🧪 Running Tests

The framework uses `pytest` with predefined markers and options in `pytest.ini`.

### Run All Tests
```powershell
pytest
```

### Run Specific Categories
```powershell
# Run only UI tests
pytest -m ui

# Run only API tests
pytest -m api

# Run in parallel (e.g., using 3 workers)
pytest -n 3
```

### Headless Execution
To run UI tests without opening a browser window (CI/CD mode), ensure headless mode is toggled in your browser fixture (if applicable).

---

## 📊 Reports & Logs

### Allure Report (Recommended)
Generates a rich, interactive report with AI-powered failure analysis and screenshots.
```powershell
allure serve ./reports/allure-results
```

### Static HTML Report
A standalone report is automatically generated at:
`./reports/report.html`

### Logs
System logs are saved to:
`./reports/logs/pytest.log`

---

## 🤖 AI Features (MCP Layer)

- **Failure Analysis**: If a test fails, the framework sends the error to an LLM to provide insights and suggested actions in the Allure report.
- **Dynamic Data**: Uses AI to generate varied and realistic note content.
- **Locator Optimizer**: A utility in `utils/locator_optimizer.py` can be used to suggest better locators for unstable elements.
