import json

import pytest
import requests


def test_image():
    url = 'https://petstore.swagger.io/v2/pet/100/uploadImage'

    with open('../images/img.png', 'rb') as f:
        file = {'file': ('img2.png', f, 'image/png')}
        response = requests.post(url=url, files=file)

    print(response.json())
    assert response.status_code == requests.codes.ok
    assert 'File uploaded to' in response.text


def test_csv():
    url = 'https://httpbin.org/pos'
    text = 'some text'

    files = {'file': ('../images/petstore.csv', text)}
    response = requests.post(url=url, files=files)

    response_json = response.json()
    assert response.status_code == requests.codes.ok
    assert response_json['files']['file'] == text


def test_images_get():
    url = 'https://httpbin.org/image/png'
    response = requests.get(url)

    content = response.content

    assert response.status_code == requests.codes.ok

    with open('../images/expect.png', 'rb') as f:
        expected_content = f.read()

    assert content == expected_content


def test_images_save():
    url = 'https://httpbin.org/image/png'
    response = requests.get(url)

    content = response.content

    with open('../images/save_image.png', 'wb') as f:
        f.write(content)

    assert response.status_code == requests.codes.ok


class TestAddPet:
    BASE_URL = "https://petstore.swagger.io/v2/pet"

    def test_add_pet(self):
        new_pet = {
            "id": 123456,
            "name": "Buddy",
            "status": "available"
        }

        response = requests.post(
            self.BASE_URL,
            headers={"Content-Type": "application/json"},
            data=json.dumps(new_pet)
        )
        response_body = response.json()
        assert response.status_code == 200
        assert response_body['name'] == new_pet.get('name')