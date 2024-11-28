import allure
from selenium.webdriver.common.by import By

from core.base import Base

class HeaderElement(Base):
    LOGO = (By.XPATH, '//*[@class="W3Prq tOEJx"]')

    def __init__(self, driver):
        super(HeaderElement, self).__init__(driver)
        self.driver = driver

    @allure.step('Assert that logo is visible')
    def assert_logo_is_visible(self):
        element = self.get_element(self.LOGO)
        assert element.is_displayed(), f"Element {self.LOGO} is not visible"


