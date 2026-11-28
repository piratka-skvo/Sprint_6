from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
import allure


class OrderScooterPage_2(BasePage):
    date_field = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']") #поле Когда привезти
    calendar_form = (By.CLASS_NAME, "react-datepicker") #форма календаря
    next_month_button = (By.XPATH, "//button[contains(@class, 'react-datepicker__navigation--next')]") #стрелка следующего месяца
    calendar_day = (By.XPATH, ".//div[contains(@class, 'react-datepicker__day--015') and not(contains(@class, 'react-datepicker__day--disabled'))]") #точный день в календаре
    order_time = (By.CLASS_NAME, 'Dropdown-root') #период аренды
    order_time_for_test = (By.XPATH, "//div[@class='Dropdown-option' and text()='сутки']") #период аренды для тестов - сутки
    color_black = (By.XPATH, "//input[@type='checkbox' and @id='black']") #выбор черного самоката
    color_grey = (By.XPATH, "//input[@type='checkbox' and @id='grey']") #выбор серого самоката
    comments = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']") #поле Комментарий
    order_button = (By.XPATH, "//button[contains(@class,'Button_Middle') and text()='Заказать']") #кнопка Заказать
    yes_button = (By.XPATH, ".//button[text()='Да']") #кнопка Да
    success_message = (By.XPATH, "//div[contains(text(), 'Заказ оформлен')]") #сообщение об успешном оформлении заказа

    @allure.step('Выбор даты доставки')
    def set_date(self):
        self.click(self.date_field)
        self.click(self.next_month_button)
        self.wait_clickable(self.calendar_day)
        self.click(self.calendar_day)

    @allure.step('Выбор времени аренды')
    def set_order_time(self):
        self.scroll_to(self.order_time)
        self.click(self.order_time)
        self.wait_visible(self.order_time_for_test)
        self.click(self.order_time_for_test)

    @allure.step('Выбор черного самоката')
    def set_color(self):
        self.click(self.color_black)

    @allure.step('Ввод комментария')
    def set_comment(self, text):
        self.send_keys(self.comments, text)

    @allure.step('Клик по кнопке Заказать')
    def click_order_button(self):
        self.click(self.order_button)

    @allure.step('Клик по кнопке Да')
    def click_yes_button(self):
        self.click(self.yes_button)

    @allure.step('Оформление заказа')
    def order_finish(self, comment=''):
        self.set_date()
        self.set_order_time()
        self.set_color()
        self.set_comment(comment)
        self.click_order_button()
        self.wait_clickable(self.yes_button)
        self.click_yes_button()
