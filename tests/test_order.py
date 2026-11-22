import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.MainPageScooter import MainPageScooter
from pages.OrderScooterPage_1 import OrderScooterPage_1
from pages.OrderScooterPage_2 import OrderScooterPage_2


class TestOrder:
    def test_order_up_button(self, driver):
        main_page = MainPageScooter(driver)
        main_page.click_order_up()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(OrderScooterPage_1.name_field))
        page_1 = OrderScooterPage_1(driver)
        page_1.order_start("Эля", "Маг", "улица Ленина, 10", "Митино", "89997775522")
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(OrderScooterPage_2.date_field))
        page_2 = OrderScooterPage_2(driver)
        page_2.order_finish()
        success = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(OrderScooterPage_2.success_message))
        assert success.is_displayed()

    def test_order_down_button(self, driver):
        main_page = MainPageScooter(driver)
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(MainPageScooter.cookie_button))
        main_page.click_cookie_button()
        main_page.click_order_down()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(OrderScooterPage_1.name_field))
        page_1 = OrderScooterPage_1(driver)
        page_1.order_start("Эльвира", "Магсум", "улица Калинина, 10", "Строгино", "89997775533")
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(OrderScooterPage_2.date_field))
        page_2 = OrderScooterPage_2(driver)
        page_2.order_finish()
        success = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(OrderScooterPage_2.success_message))
        assert success.is_displayed()

