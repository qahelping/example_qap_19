import json

import requests


def test_post():
    url = 'https://httpbin.org/status/301'
    data = {'key': 'value'}

    response = requests.post(url, data=data)
    assert response.status_code == 200


def test_post_json():
    url = 'https://httpbin.org/status/301'
    headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
    body = {
        "id": 0,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }
    response = requests.post(url, data=json.dumps(body), headers=headers)
    assert response.status_code == 200
