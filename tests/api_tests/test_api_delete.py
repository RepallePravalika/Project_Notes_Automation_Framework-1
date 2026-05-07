from api.api_client import APIClient

from utils.logger import logger


def test_delete_note(api_client):

    logger.info(
        "Starting delete note API test"
    )

    # Get notes list
    logger.info(
        "Fetching notes list"
    )

    response = api_client.get_notes()

    response_json = response.json()

    notes = response_json["data"]

    # If no notes exist, create one first
    if len(notes) == 0:

        logger.info(
            "No notes found. Creating temporary note"
        )

        create_response = api_client.create_note(

            title="API Delete Test",

            description="Temporary note",

            category="Work"
        )

        assert create_response.status_code == 200

        response = api_client.get_notes()

        notes = response.json()["data"]

    logger.info(
        "Notes list fetched successfully"
    )

    # Pick first note
    note = notes[0]

    note_id = note["id"]

    note_title = note["title"]

    logger.info(
        f"Deleting note : {note_title}"
    )

    logger.info(
        f"Note ID : {note_id}"
    )

    # Delete note
    delete_response = api_client.delete_note(
        note_id
    )

    # Validate delete status
    assert delete_response.status_code == 200

    logger.info(
        "Note deleted successfully"
    )

    # Call GET /notes again
    updated_response = api_client.get_notes()

    updated_notes = updated_response.json()["data"]

    # Validate deleted note removed
    deleted_note_exists = any(
        note["id"] == note_id
        for note in updated_notes
    )

    assert deleted_note_exists is False

    logger.info(
        "Deleted note no longer exists"
    )