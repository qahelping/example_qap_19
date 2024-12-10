import json
import requests

from services.jwt_service import JWTService


class TestAuth():
    BASE_URL = 'https://jwt.qa.studio/api/v1/jwt'
    TOKEN = None

    def test_get_token(self):
        data = {"login": "example@qa.studio", "password": "wfdswhHXIAUDTQ"}
        headers = {"Content-Type": "application/json", 'accept': 'application/json'}
        response = requests.post(self.BASE_URL + '/token', body=json.dumps(data), headers=headers)

        assert response.status_code == requests.codes.ok
        assert response.json()['access_token'] is not None
        assert response.json()['refresh_token'] is not None

        self.TOKEN = response.json()['access_token']

        print(self.TOKEN)

        headers = {"Content-Type": "application/json",
                   'accept': 'application/json',
                   'Authorization': 'Bearer {}'.format(self.TOKEN)}
        response = requests.get(self.BASE_URL + '/data', headers=headers)

        assert response.status_code == requests.codes.ok
        assert response.json()['success'] == "my secure data"

    def test_get_user_toke(self):
        service = JWTService()
        token = service.get_jwt_token("example@qa.studio", "wfdswhHXIAUDTQ")
        assert token
