import pytest
import requests


def test_text():
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    assert response.status_code == 200
    assert 'message' in response.text


def test_json():
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    response_json = response.json()

    assert response.status_code == 200, f"status_code should be 200, but get {response.status_code}"
    assert 'message' in response_json.keys(), "key 'message' not in body"
    assert 'status' in response_json.keys(), "key 'status' not in body"
    assert 'code' not in response_json.keys(), "key 'code' in body"

    assert response_json['status'] == 'success'
    assert 'images.dog.ceo/breeds' in response_json['message']


@pytest.mark.parametrize("code, result", [(200, True), (300, True), (400, False), (500, False), (201, False)],
                         ids=['200_success', '300_success', '400_failed', '500_failed', '201_failed'])
def test_raise_for_status(code, result):
    url = f'https://httpbin.org/status/{code}'

    response = requests.get(url)

    try:
        response.raise_for_status()
        assert result == True
    except requests.HTTPError as err:
        print(err)
        assert result == False


def test_codes():
    url = f'https://httpbin.org/status/{404}'

    response = requests.get(url)
    assert response.status_code == requests.codes.not_found, f"status_code should be 404, but get {response.status_code}"

STATUS_CODE = [
    (200, requests.codes.ok),  # OK
    (300, requests.codes.multiple_choices),  # Multiple Choices
    (400, requests.codes.bad_request),  # Bad Request
    (404, requests.codes.not_found),  # Not Found
    (500, requests.codes.internal_server_error),  # Internal Server Error
    (511, requests.codes.network_authentication),  # Network Authentication Required
]

@pytest.mark.parametrize("code, result", STATUS_CODE)
def test_raise_for_status(code, result):
    url = f'https://httpbin.org/status/{code}'
    response = requests.get(url)
    assert response.status_code == result, f"status_code should be {response.status_code}, but get {result}"

