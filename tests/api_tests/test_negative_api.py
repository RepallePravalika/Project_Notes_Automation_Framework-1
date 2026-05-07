import requests

from config.environment import load_config

from utils.logger import logger


def test_get_notes_without_token():

    logger.info(
        "Starting negative API test"
    )

    config = load_config()

    logger.info(
        "Calling GET /notes without token"
    )

    response = requests.get(

        f"{config['api_base_url']}/notes"
    )

    logger.info(
        "Validating unauthorized response"
    )

    # Validate unauthorized access
    assert response.status_code == 401

    logger.info(
        "Unauthorized API validation successful"
    )