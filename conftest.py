import os

import pytest

import allure

from fixtures.browser_fixture import driver
from fixtures.api_fixture import api_client


# Create screenshots folder
os.makedirs(
    "screenshots",
    exist_ok=True
)


@pytest.hookimpl(hookwrapper=True)

def pytest_runtest_makereport(item, call):

    outcome = yield

    report = outcome.get_result()

    # Capture screenshot only on failure
    if report.when == "call" and report.failed:

        driver_instance = item.funcargs.get(
            "driver"
        )

        if driver_instance:

            screenshot_path = (

                f"screenshots/"
                f"{item.name}.png"
            )

            driver_instance.save_screenshot(
                screenshot_path
            )

            # Attach screenshot to Allure
            allure.attach.file(

                screenshot_path,

                name="Failure Screenshot",

                attachment_type=
                allure.attachment_type.PNG
            )

            # AI-Assisted Failure Analysis
            from utils.failure_analyzer import FailureAnalyzer
            from utils.logger import logger

            # Extract exception info
            error_msg = f"{call.excinfo.typename}: {str(call.excinfo.value)}"
            analysis = FailureAnalyzer.analyze(error_msg)

            # Log analysis
            logger.error("-" * 50)
            logger.error("AI-POWERED FAILURE ANALYSIS")
            logger.error(f"Detected Issue: {analysis['detected_issue']}")
            logger.error(f"Insight: {analysis['insight']}")
            logger.error(f"Suggested Action: {analysis['suggested_action']}")
            logger.error("-" * 50)

            # Attach analysis to Allure
            analysis_text = (
                f"DETECTED ISSUE: {analysis['detected_issue']}\n"
                f"INSIGHT: {analysis['insight']}\n"
                f"SUGGESTED ACTION: {analysis['suggested_action']}"
            )
            allure.attach(
                analysis_text,
                name="AI Failure Analysis",
                attachment_type=allure.attachment_type.TEXT
            )