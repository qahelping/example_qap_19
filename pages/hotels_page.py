import allure
from selenium.webdriver.common.by import By

from core.base import Base
from data.urls import DOMAIN


class HotelsPage(Base):
    HOTELS_PAGE = (By.CSS_SELECTOR, '[class="JGFbQ zNQ2x"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        self.page = f'{DOMAIN}hotels/'

    @allure.step('Open "Hotels" page')
    def open(self):
        self.driver.get(self.page)

    @allure.step('Assert that page is opened')
    def assert_page_is_opened(self):
       element = self.get_element(self.HOTELS_PAGE)
       assert element.is_displayed(), f"Element {self.HOTELS_PAGE} is not visible"

