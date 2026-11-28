import pytest
from pages.MainPageScooter import MainPageScooter
from pages.OrderScooterPage_1 import OrderScooterPage_1
from pages.OrderScooterPage_2 import OrderScooterPage_2
import allure

class TestOrder:
    @allure.title('Оформление заказа через кнопку Заказать в верхней части страницы')
    def test_order_up_button(self, driver):
        main_page = MainPageScooter(driver)
        main_page.click_cookie_button()
        main_page.click_order_up()
        page_1 = OrderScooterPage_1(driver)
        page_1.wait_visible(OrderScooterPage_1.name_field)
        page_1.order_start('Эля', 'Маг', 'улица Ленина, 10', 'Митино', '89997775522')
        page_2 = OrderScooterPage_2(driver)
        page_2.wait_visible(OrderScooterPage_2.date_field)
        page_2.order_finish()
        success=page_2.wait_visible(OrderScooterPage_2.success_message)
        assert success.is_displayed()

    @allure.title('Оформление заказа через кнопку Заказать в нижней части страницы')
    def test_order_down_button(self, driver):
        main_page = MainPageScooter(driver)
        main_page.click_cookie_button()
        main_page.click_order_down()
        page_1 = OrderScooterPage_1(driver)
        page_1.wait_visible(OrderScooterPage_1.name_field)
        page_1.order_start('Эльвира', 'Магсум', 'улица Калинина, 10', 'Строгино', '89997775533')
        page_2 = OrderScooterPage_2(driver)
        page_2.wait_visible(OrderScooterPage_2.date_field)
        page_2.order_finish()
        success=page_2.wait_visible(OrderScooterPage_2.success_message)
        assert success.is_displayed()

