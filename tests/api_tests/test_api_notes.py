from api.api_client import APIClient

from utils.logger import logger


def test_get_notes(api_client):

    logger.info(
        "Starting GET notes API test"
    )

    # Call GET /notes
    logger.info(
        "Calling GET /notes API"
    )

    response = api_client.get_notes()

    # Validate status code
    assert response.status_code == 200

    logger.info(
        "Status code validation successful"
    )

    # Validate response time
    assert response.elapsed.total_seconds() < 2

    logger.info(
        "Response time validation successful"
    )

    # Convert response to JSON
    response_json = response.json()

    # Validate notes list exists
    assert "data" in response_json

    logger.info(
        "Notes list exists in response"
    )

    # Validate data type
    assert isinstance(
        response_json["data"],
        list
    )

    logger.info(
        "Notes response is of list type"
    )

    # Extract notes list
    notes = response_json["data"]

    logger.info(
        f"Total Notes Retrieved : {len(notes)}"
    )

    # Log each note details
    for note in notes:

        logger.info(
            f"Title : {note['title']}"
        )

        logger.info(
            f"Description : {note['description']}"
        )

        logger.info(
            f"Category : {note['category']}"
        )

        logger.info(
            "-----------------------------------"
        )
