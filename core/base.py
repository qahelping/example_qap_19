import allure
from selenium.webdriver.firefox.webdriver import WebDriver


class Base:
    def __init__(self, driver):
        self.driver: WebDriver = driver

    @allure.step('get_element')
    def get_element(self, selector):
        return self.driver.find_element(*selector)

    @allure.step('click_on ${selector}')
    def click_on(self, selector, force=False):
        element = self.get_element(selector)
        if force:
            self.driver.execute_script("arguments[0].click();", element)
        else:
            element.click()

    @allure.step('force_click_on "{selector}"')
    def force_click_on(self, selector):
        element = self.get_element(selector)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('click {selector}')
    def click(self, selector):
        element = self.get_element(selector)
        element.click()
