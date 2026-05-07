import pytest
from api.api_client import APIClient

@pytest.fixture(scope="session")
def api_client():
    """Provides a logged-in API client instance."""
    api = APIClient()
    api.login()
    return api
