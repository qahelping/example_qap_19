import allure
from selenium.webdriver.firefox.webdriver import WebDriver

from core.base import Base


class Assertions(Base):

    def __init__(self, driver):
        super().__init__(driver)


    def assert_element_is_visible(self, selector):
        element = self.get_element(selector)
        assert element.is_displayed(), f"Element {selector} is not visible"
