import pytest

from config.environment import load_config

from pages.login_page import LoginPage

from pages.notes_page import NotesPage

from utils.logger import logger


@pytest.mark.parametrize(

    "title,description",

    [

        ("", ""),

        ("", "Only description"),

        ("Only title", ""),

        (" ", " "),

    ]
)

def test_create_invalid_note(

    driver,

    title,

    description
):

    logger.info(
        "Starting negative create note test"
    )

    config = load_config()

    login = LoginPage(driver)

    notes = NotesPage(driver)

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

    # Login
    logger.info(
        "Logging into application"
    )

    login.login(
        config["email"],
        config["password"]
    )

    logger.info(
        "Login successful"
    )

    # Open create note popup
    logger.info(
        "Opening create note popup"
    )

    notes.click_add_note()

    # Enter invalid data
    logger.info(
        "Entering invalid note data"
    )

    if title:
        notes.enter_title(title)

    if description:
        notes.enter_description(description)

    # Click create
    logger.info(
        "Trying to create invalid note"
    )

    notes.click_create()

    logger.info(
        "Validating note creation failure"
    )

    # Validate popup still visible
    assert driver.find_element(
        *notes.TITLE_FIELD
    ).is_displayed()

    logger.info(
        "Invalid note creation blocked successfully"
    )