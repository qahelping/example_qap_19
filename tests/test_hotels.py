import allure

from pages.hotels_page import HotelsPage


@allure.feature("Hotels")
class TestHotels:

    def test_open_page(self, driver):
        hotels_page = HotelsPage(driver)
        hotels_page.open()
        hotels_page.assert_page_is_opened()
