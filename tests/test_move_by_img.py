import pytest
from pages.MainPageScooter import MainPageScooter
from pages.OrderScooterPage_1 import OrderScooterPage_1
import allure

class TestMoveByImg:
    @allure.title('Переход на главную страницу по кнопке Самокат')
    def test_open_mainpage_by_scooter_button(self, driver):
        main_page = MainPageScooter(driver)
        main_page.click_order_up()
        page_1 = OrderScooterPage_1(driver)
        page_1.wait_visible(OrderScooterPage_1.name_field)
        page_1.click_scooter_button()
        success=main_page.wait_visible(main_page.scooter_img)
        assert success.is_displayed()

    @allure.title('Переход на Дзен по кнопке Яндекс')
    def test_open_dzen_by_yandex_button(self, driver):
        main_page = MainPageScooter(driver)
        main_page.click_order_up()
        page_1 = OrderScooterPage_1(driver)
        page_1.wait_visible(OrderScooterPage_1.name_field)
        page_1.click_yandex_button()
        page_1.switch_to_new_window()
        page_1.wait_url_contains('dzen.ru')
        assert "dzen.ru" in page_1.get_current_url()
