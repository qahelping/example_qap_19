import json
import logging

import allure
import requests

def create_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # Создаем обработчик для вывода логов в консоль
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # Создаем обработчик для записи логов в файл
    file_handler = logging.FileHandler('../log.log')
    file_handler.setLevel(logging.INFO)

    # Форматирование логов
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # Добавляем обработчики к логгеру
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger


class BaseService:
    def __init__(self):
        self.logger = create_logger()

    # @allure.step('GET: {url}')
    # def request(self, url, headers, code=200):
    #     response = requests.request(method, url, headers)
    #
    #     try:
    #         assert response.status_code == code
    #         self.logger.info("OK. URL: %s, Code: %d", url, response.status_code)
    #     except requests.HTTPError as err:
    #         self.logger.error("Error. %s", str(err))
    #         assert response.status_code == code
    #
    #     return response.json()

    @allure.step('GET: {url}')
    def get(self, url, headers, code=200):
        response = requests.get(url, headers)

        try:
            assert response.status_code == code
            self.logger.info("OK. URL: %s, Code: %d", url, response.status_code)
        except requests.HTTPError as err:
            self.logger.error("Error. %s", str(err))
            assert response.status_code == code

        return response.json()

    @allure.step('POST: {url}')
    def post(self, url, body, headers, code=200):
        response = requests.post(url, data=json.dumps(body), headers=headers)

        try:
            assert response.status_code == code
            self.logger.info("OK. URL: %s, Code: %d", url, response.status_code)
        except requests.HTTPError as err:
            self.logger.error("Error. %s", str(err))

            assert response.status_code == code

        return response.json()

