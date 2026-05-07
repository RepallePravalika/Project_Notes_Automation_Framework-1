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