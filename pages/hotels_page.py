import allure
from selenium.webdriver.common.by import By

from core.assertions import Assertions
from core.base import Base
from data.urls import DOMAIN
from elements.header_element import HeaderElement


class HotelsPage(Base, Assertions):
    HOTELS_PAGE = (By.CSS_SELECTOR, '[class="JGFbQ zNQ2x"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        self.page = f'{DOMAIN}hotels/'
        self.header = HeaderElement(driver)

    @allure.step('Open "Hotels" page')
    def open(self):
        self.driver.get(self.page)
        self.assert_page_is_opened()

    @allure.step('Assert that page is opened')
    def assert_page_is_opened(self):
       self.assert_element_is_visible(self.HOTELS_PAGE)

