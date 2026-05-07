from pages.login_page import LoginPage

from config.environment import load_config

from utils.logger import logger


def test_login(driver):

    logger.info(
        "Starting login test"
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

    # Perform login
    logger.info(
        "Performing login"
    )

    login.login(
        config["email"],
        config["password"]
    )

    logger.info(
        "Login successful"
    )

    # Validate dashboard
    assert login.is_dashboard_loaded()

    logger.info(
        "Dashboard loaded successfully"
    )