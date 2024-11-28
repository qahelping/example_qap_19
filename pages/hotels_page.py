import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver

from core.assertions import Assertions
from core.base import Base
from core.get_locators import get_css_selector_by_class_name
from data.urls import DOMAIN
from elements.header_element import HeaderElement


class HotelsPage(Base):
    HOTELS_PAGE = (By.CSS_SELECTOR, '[class="JGFbQ zNQ2x"]')


    IN_DATA_PICKER = (By.CSS_SELECTOR, '[aria-label="Дата заезда"]')
    OUT_DATA_PICKER = (By.CSS_SELECTOR, '[aria-label="Дата выезда"]')
    SUBMIT = (By.CSS_SELECTOR, '[type="submit"]')

    WHERE_INPUT = get_css_selector_by_class_name('w_eHd input_center')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver: WebDriver = driver

        self.page = f'{DOMAIN}hotels/'
        self.header = HeaderElement(driver)
        self.assertions = Assertions(self.driver)

    @allure.step('Open "Hotels" page')
    def select_data(self, checkin_data='2024-12-10', checkin_out_data='2024-12-20'):
        checkin = f'[data-qa="calendar-day-{checkin_data}"]'
        checkout = f'[data-qa="calendar-day-{checkin_out_data}"]'

        self.click_on(self.IN_DATA_PICKER)
        self.click_on((By.CSS_SELECTOR, checkin))

        self.click_on(self.OUT_DATA_PICKER)
        self.click_on((By.CSS_SELECTOR, checkout))
        self.click_on(self.SUBMIT)

    @allure.step('Fill location')
    def fill_where(self):
        pass

    @allure.step('Open "Hotels" page')
    def open(self):
        self.driver.get(self.page)
        self.assert_page_is_opened()

    @allure.step('Assert that page is opened')
    def assert_page_is_opened(self):
       self.assertions.assert_element_is_visible(self.HOTELS_PAGE)

