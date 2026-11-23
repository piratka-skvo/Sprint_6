from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from pages.BasePage import BasePage


class OrderScooterPage_2(BasePage):
    date_field = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']") #поле Когда привезти
    calendar_form = (By.CLASS_NAME, "react-datepicker") #форма календаря
    calendar_day = (By.XPATH, ".//div[contains(@class, 'react-datepicker__day--028') and not(contains(@class, 'react-datepicker__day--disabled'))]") #точный день в календаре
    order_time = (By.CLASS_NAME, 'Dropdown-root') #период аренды
    order_time_for_test = (By.XPATH, "//div[@class='Dropdown-option' and text()='сутки']") #период аренды для тестов - сутки
    color_black = (By.XPATH, "//input[@type='checkbox' and @id='black']") #выбор черного самоката
    color_grey = (By.XPATH, "//input[@type='checkbox' and @id='grey']") #выбор серого самоката
    comments = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']") #поле Комментарий
    order_button = (By.XPATH, "//button[contains(@class,'Button_Middle') and text()='Заказать']") #кнопка Заказать
    yes_button = (By.XPATH, ".//button[text()='Да']") #кнопка Да
    success_message = (By.XPATH, "//div[contains(text(), 'Заказ оформлен')]") #сообщение об успешном оформлении заказа

    def set_date(self):
        self.click(self.date_field)
        self.wait.until(expected_conditions.element_to_be_clickable(self.calendar_day))
        self.click(self.calendar_day)

    def set_order_time(self):
        element = self.driver.find_element(*self.order_time)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.wait.until(expected_conditions.element_to_be_clickable(self.order_time)).click()
        self.wait.until(expected_conditions.visibility_of_element_located(self.order_time_for_test))
        self.driver.find_element(*self.order_time_for_test).click()

    def set_color(self):
        self.click(self.color_black)
    
    def set_comment(self, text):
        self.send_keys(self.comments, text)

    def click_order_button(self):
        self.click(self.order_button)

    def click_yes_button(self):
        self.click(self.yes_button)

    def order_finish(self, comment=''):
        self.set_date()
        self.set_order_time()
        self.set_color()
        self.set_comment(comment)
        self.click_order_button()
        self.wait.until(expected_conditions.element_to_be_clickable(
        self.yes_button))
        self.click_yes_button()
