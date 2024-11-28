import allure
from selenium.webdriver.firefox.webdriver import WebDriver

from core.base import Base


class Assertions:

    def __init__(self, driver):
        super().__init__(driver)
        self.driver: WebDriver = driver

        self.base = Base(driver)

    def assert_element_is_visible(self, selector):
        element = self.base.get_element(selector)
        assert element.is_displayed(), f"Element {selector} is not visible"
