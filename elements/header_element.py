import allure
from selenium.webdriver.common.by import By

from core.assertions import Assertions
from core.base import Base

class HeaderElement(Base, Assertions):
    LOGO = (By.XPATH, '//*[@class="W3Prq tOEJx"]')

    def __init__(self, driver):
        super(HeaderElement, self).__init__(driver)

    @allure.step('Assert that logo is visible')
    def assert_logo_is_visible(self):
        self.assert_element_is_visible(self.LOGO)


