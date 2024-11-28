import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver

from core.assertions import Assertions
from core.base import Base
from data.urls import DOMAIN
from elements.header_element import HeaderElement


class YandexPage(Base):
    SEARCH = (By.CLASS_NAME, 'search3__inner')
    HEADLINE = (By.CLASS_NAME, 'headline')
    WEATHER_ICON = (By.CLASS_NAME, 'weather__icon')
    ALICA_ICON = (By.CLASS_NAME, 'alice__icon')
    PERSONAL_ICON = (By.CSS_SELECTOR, '[class*="headline__personal-item_services"]')
    ENTER_ICON = (By.CSS_SELECTOR, '[class*="headline__personal-enter"]')
    MENU_ICON = (By.CSS_SELECTOR, '[class*="headline__personal-menu"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver: WebDriver = driver

        self.page = f'{DOMAIN}hotels/'
        self.path = 'https://ya.ru/'

        self.assertions = Assertions(self.driver)

    @allure.step('Open "YANDEX" page')
    def open(self):
        self.driver.get(self.page)
        self.assert_page_is_opened()

    @allure.step('Assert that page is opened')
    def assert_page_is_opened(self):
        assert self.driver.current_url == self.path, f"Url should be {self.path}, but is {self.driver.current_url}"
        assert self.driver.title == 'Яндекс — быстрый поиск в интернете'

        self.assertions.assert_element_is_visible(self.SEARCH)
        self.assertions.assert_element_is_visible(self.HEADLINE)
        self.assertions.assert_element_is_visible(self.WEATHER_ICON)
        self.assertions.assert_element_is_visible(self.ALICA_ICON)
        self.assertions.assert_element_is_visible(self.PERSONAL_ICON)
        self.assertions.assert_element_is_visible(self.ENTER_ICON)
        self.assertions.assert_element_is_visible(self.MENU_ICON)
