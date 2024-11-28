import allure
from selenium.webdriver.common.by import By

from core.assertions import Assertions
from core.base import Base


class HeaderElement(Base):
    LOGO = (By.XPATH, '//*[@class="W3Prq tOEJx"]')
    LOGO_YANDEX = (By.CSS_SELECTOR, '[class="Kw61r vOWh4 opWbc"]')

    def __init__(self, driver):
        super(HeaderElement, self).__init__(driver)

        self.assertions = Assertions(self.driver)

    @allure.step('Click on yandex logo')
    def click_on_logo_yandex(self):
        self.click_on(self.LOGO_YANDEX, force=True)


    @allure.step('Assert that logo is visible')
    def assert_logo_is_visible(self):
        self.assertions.assert_element_is_visible(self.LOGO)
