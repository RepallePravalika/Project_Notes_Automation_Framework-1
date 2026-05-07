from pages.login_page import LoginPage

from pages.notes_page import NotesPage

from config.environment import load_config

from api.api_client import APIClient

from utils.logger import logger


def test_ui_to_api_validation(driver, api_client):

    logger.info(
        "Starting UI to API hybrid validation test"
    )

    config = load_config()

    login = LoginPage(driver)

    notes = NotesPage(driver)

    # Test data
    note_title = "Hybrid UI API Test"

    note_description = (
        "Validate UI note in API response"
    )

    note_category = "Work"

    logger.info(
        "Test data prepared"
    )

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
        "Logging into UI"
    )

    login.login(
        config["email"],
        config["password"]
    )

    logger.info(
        "Login successful"
    )

    # Create note in UI
    logger.info(
        "Creating note in UI"
    )

    notes.click_add_note()

    notes.select_category(
        note_category
    )

    notes.enter_title(
        note_title
    )

    notes.enter_description(
        note_description
    )

    notes.click_create()

    logger.info(
        "Note created successfully in UI"
    )

    # Validate note visible in UI
    assert notes.is_note_created(
        note_title
    )

    logger.info(
        "Note visible in UI"
    )

    # Call GET /notes
    logger.info(
        "Calling GET /notes API"
    )

    response = api_client.get_notes()

    # Validate status code
    assert response.status_code == 200

    logger.info(
        "GET /notes API successful"
    )

    response_json = response.json()

    notes_list = response_json["data"]

    # Validate note exists in API
    matching_note = next(

        (
            note for note in notes_list

            if note["title"] == note_title

            and note["description"] == note_description
        ),

        None
    )

    assert matching_note is not None

    logger.info(
        "Created note found in API response"
    )

    # Validate category consistency
    assert (
        matching_note["category"]
        == note_category
    )

    logger.info(
        "UI and API data validation successful"
    )