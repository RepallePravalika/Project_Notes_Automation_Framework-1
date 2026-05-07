import pytest

from pages.login_page import LoginPage

from config.environment import load_config

from utils.logger import logger


@pytest.mark.parametrize(

    "email,password",

    [

        ("wronguser@gmail.com", "wrongpassword"),

        ("invalid@gmail.com", "123456"),

        ("", "wrongpassword"),

        ("wronguser@gmail.com", ""),

        ("", "")
    ]
)

def test_invalid_login(

    driver,

    email,

    password
):

    logger.info(
        "Starting invalid login test"
    )

    config = load_config()

    login = LoginPage(driver)

    # Open application
    logger.info(
        "Opening Notes application"
    )

    login.load(
        config["ui_base_url"]
    )

    # Open login page
    logger.info(
        "Opening login page"
    )

    login.open_login_page()

    # Perform invalid login
    logger.info(
        f"Performing invalid login with email : {email}"
    )

    login.login(
        email,
        password,
        wait_for_dashboard=False
    )

    logger.info(
        "Validating login failure"
    )

    # Validate user still remains on login page
    assert "login" in driver.current_url.lower()

    logger.info(
        "Invalid login validation successful"
    )