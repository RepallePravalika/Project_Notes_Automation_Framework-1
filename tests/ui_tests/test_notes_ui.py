from config.environment import load_config

from pages.login_page import LoginPage

from pages.notes_page import NotesPage

from utils.logger import logger

from utils.ai_test_data import AITestDataGenerator


def test_create_note(driver):

    logger.info(
        "Starting create note UI test"
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

    # Create note
    logger.info(
        "Creating new note"
    )

    # Generate AI Test Data
    note_data = AITestDataGenerator.generate_note_data()

    notes.click_add_note()

    notes.select_category(
        "Work"
    )

    notes.enter_title(
        note_data["title"]
    )

    notes.enter_description(
        note_data["description"]
    )

    notes.click_create()

    logger.info(
        "Note created successfully"
    )

    # Validate note created
    assert notes.is_note_created(
        note_data["title"]
    )

    logger.info(
        "Created note visible in UI"
    )