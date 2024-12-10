import json

from core.service import BaseService
from models.jwt_model import JWT


class JWTService(BaseService):

    def __init__(self):
        super().__init__()
        self.BASE_URL = 'https://jwt.qa.studio/api/v1/jwt'
        self.token = None

    def get_jwt_token(self, login, password):
        data = {"login": login, "password": password}
        headers = {"Content-Type": "application/json", 'accept': 'application/json'}
        response = self.post(self.BASE_URL + '/token', body=data, headers=headers)
        model = JWT(**response)

        self.token = model.access_token
        return self.token



