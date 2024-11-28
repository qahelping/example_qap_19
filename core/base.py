from selenium.webdriver.firefox.webdriver import WebDriver


class Base:
    def __init__(self, driver):
        self.driver: WebDriver = driver


    def get_element(self, selector):
        return self.driver.find_element(*selector)