import allure
import pytest

from elements.header_element import HeaderElement
from pages.hotels_page import HotelsPage


@allure.feature("Hotels")
class TestHotels:

    def test_open_page(self, driver):
        hotels_page = HotelsPage(driver)
        hotels_page.open()
        hotels_page.assert_page_is_opened()

    @pytest.mark.only
    def test_logo_is_visible(self, driver):
        hotels_page = HotelsPage(driver)
        hotels_page.open()

        header_element = HeaderElement(driver)
        header_element.assert_logo_is_visible()
