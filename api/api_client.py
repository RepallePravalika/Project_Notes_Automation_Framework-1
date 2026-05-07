import requests

from config.environment import load_config


config = load_config()

BASE_URL = config["api_base_url"]


class APIClient:

    def __init__(self):

        self.token = None

    # Login API
    def login(self):

        response = requests.post(

            f"{BASE_URL}/users/login",

            data={
                "email": config["email"],
                "password": config["password"]
            }

        )

        assert response.status_code == 200

        self.token = response.json()["data"]["token"]

        return self.token

    # Common headers
    def get_headers(self):

        return {
            "x-auth-token": self.token
        }

    # GET /notes
    def get_notes(self):

        response = requests.get(

            f"{BASE_URL}/notes",

            headers=self.get_headers()

        )

        return response

    # DELETE /notes/{id}
    def delete_note(self, note_id):

        response = requests.delete(

            f"{BASE_URL}/notes/{note_id}",

            headers=self.get_headers()

        )

        return response
    
    def create_note(self, title, description, category):

        response = requests.post(

        f"{BASE_URL}/notes",

        headers=self.get_headers(),

        json={

            "title": title,

            "description": description,

            "category": category
        }
    )

        return response