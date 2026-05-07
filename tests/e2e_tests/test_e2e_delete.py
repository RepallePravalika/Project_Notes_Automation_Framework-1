from pages.login_page import LoginPage
from pages.notes_page import NotesPage
from config.environment import load_config
from api.api_client import APIClient
from utils.logger import logger

def test_api_delete_reflects_in_ui(driver, api_client):
    logger.info("Starting API to UI delete validation test")
    config = load_config()
    login = LoginPage(driver)
    notes = NotesPage(driver)

    # Fetch notes list
    logger.info("Fetching notes list")
    response = api_client.get_notes()
    notes_list = response.json()["data"]

    # If no notes exist create one
    if len(notes_list) == 0:
        logger.info("No notes found, creating note")
        create_response = api_client.create_note(
            title="E2E Delete Test",
            description="Delete validation note",
            category="Work"
        )
        assert create_response.status_code == 200
        logger.info("Note created successfully")
        
        # Refresh list after creation
        response = api_client.get_notes()
        notes_list = response.json()["data"]

    # Open application
    logger.info("Opening Notes application")
    login.load(config["ui_base_url"])

    # Open login page
    logger.info("Opening login page")
    login.open_login_page()

    # Login to UI
    logger.info("Logging into UI")
    login.login(config["email"], config["password"])
    logger.info("Login successful")

    # Refresh UI to ensure notes are loaded
    notes.refresh_page()

    # Capture first note title
    note_title = notes.get_first_note_title()
    logger.info(f"Captured note title : {note_title}")

    # Find matching note ID in API list
    matching_note = next(
        (note for note in notes_list if note["title"] == note_title),
        None
    )
    
    # If not found in initial list, try fetching latest list one more time
    if not matching_note:
        response = api_client.get_notes()
        notes_list = response.json()["data"]
        matching_note = next(
            (note for note in notes_list if note["title"] == note_title),
            None
        )

    assert matching_note is not None, f"Note with title '{note_title}' not found in API"
    logger.info("Matching note found")

    # Extract note ID
    note_id = matching_note["id"]
    logger.info(f"Deleting note ID : {note_id}")

    # Delete note via API
    delete_response = api_client.delete_note(note_id)
    assert delete_response.status_code == 200
    logger.info("Note deleted successfully using API")

    # Refresh UI
    notes.refresh_page()

    # Validate note removed from UI
    # Note: is_note_present now returns False if the note is NOT there
    assert not notes.is_note_present(note_title), f"Note '{note_title}' is still visible in UI after deletion"
    logger.info("Deleted note no longer visible in UI")