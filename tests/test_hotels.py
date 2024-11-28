import allure
import pytest

from elements.header_element import HeaderElement
from pages.hotels_page import HotelsPage
from pages.ya_page import YandexPage


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
        hotels_page.header.assert_logo_is_visible()

    @pytest.mark.only
    def test_click_on_logo(self, driver):
        hotels_page = HotelsPage(driver)
        hotels_page.open()
        hotels_page.header.assert_logo_is_visible()
        hotels_page.header.click_on_logo_yandex()

        yandex_page = YandexPage(driver)
        yandex_page.assert_page_is_opened()


    @pytest.mark.only
    def test_search_hotels(self, driver):
        hotels_page = HotelsPage(driver)
        hotels_page.open()

        hotels_page.select_data()