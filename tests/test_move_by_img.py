import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.MainPageScooter import MainPageScooter
from pages.OrderScooterPage_1 import OrderScooterPage_1

class TestMoveByImg:
    def test_open_mainpage_by_scooter_button(self, driver):
        main_page = MainPageScooter(driver)
        main_page.click_order_up()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(OrderScooterPage_1.name_field))
        page_1 = OrderScooterPage_1(driver)
        page_1.click_scooter_button()
        success=WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(main_page.scooter_img))
        assert success.is_displayed()

    def test_open_dzen_by_yandex_button(self, driver):
        main_page = MainPageScooter(driver)
        main_page.click_order_up()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(OrderScooterPage_1.name_field))
        page_1 = OrderScooterPage_1(driver)
        page_1.click_yandex_button()
        WebDriverWait(driver, 10).until(expected_conditions.number_of_windows_to_be(2))
        driver.switch_to.window(driver.window_handles[-1])
        WebDriverWait(driver, 10).until(expected_conditions.url_contains("dzen.ru"))
        assert "dzen.ru" in driver.current_url
