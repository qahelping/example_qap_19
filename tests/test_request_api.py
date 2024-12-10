import json

import requests


def test_get():
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    response_dict = response.json()
    assert response.status_code == 200
    assert response_dict.get("message") is not None
    assert response_dict.get("status") is not None


def test_get_404():
    response = requests.get('https://dog.ceo/api/breeds/image/random1')
    response_dict = response.json()
    assert response.status_code == 404
    assert response_dict.get("message")
    assert response_dict.get("status") == "error"
    assert response_dict.get("code") == 404


def test_put():
    body = {
        "id": 1020,
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
    response = requests.put(url='https://petstore.swagger.io/v2/pet', data=json.dumps(body))
    print(response.json())
    assert response.status_code == 415


def test_post():
    response = requests.post('https://httpbin.org/post', data={'key': 'value'})
    assert response.status_code == 200

def test_delete():
    response = requests.delete('https://httpbin.org/delete')
    assert response.status_code == 200


def test_head():
    response = requests.head('https://httpbin.org/head')
    assert response.status_code == 404


def test_options():
    response = requests.options('https://httpbin.org/options')
    assert response.status_code == 404
