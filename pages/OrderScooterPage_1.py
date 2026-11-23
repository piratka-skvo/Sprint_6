from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from pages.BasePage import BasePage

class OrderScooterPage_1(BasePage):
    name_field = (By.XPATH, ".//input[@placeholder='* Имя']") #поле Имя
    surname_field = (By.XPATH, ".//input[@placeholder='* Фамилия']") #поле Фамилия
    address_field = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']") #поле Адрес
    metro_field = (By.XPATH, ".//input[@class='select-search__input' and @placeholder='* Станция метро']") #выбор метро
    phone_field = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']") #поле Телефон
    next_button = (By.XPATH, ".//button[text()='Далее']") #кнопка Далее
    metro_dropdown_item = ".//li[contains(., '{}')]" #список метро
    metro_option = ".//button[contains(@class, 'Order_SelectOption') and contains(text(), '{}')]" #точная станция метро
    scooter_button = (By.XPATH, '//a[img[@alt="Scooter"]]') #кнопка Самокат
    yandex_button = (By.XPATH, '//a[img[@alt="Yandex"]]') #кнопка Яндекс

    def set_name(self, name):
        self.send_keys(self.name_field, name)

    def set_surname(self, surname):
        self.send_keys(self.surname_field, surname)

    def set_address(self, address):
        self.send_keys(self.address_field, address)

    def set_metro(self, metro):
        field = self.wait.until(expected_conditions.element_to_be_clickable(self.metro_field))
        field.click()
        field.send_keys(metro)
        option = self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, f"//ul[contains(@class,'select-search__options')]//*[contains(text(),'{metro}')]")))
        option.click()

    def set_phone(self, phone):
        self.send_keys(self.phone_field, phone)

    def click_next_button(self):
        self.click(self.next_button)

    def click_scooter_button(self):
        self.click(self.scooter_button)

    def click_yandex_button(self):
        self.click(self.yandex_button)


    def order_start(self, name, surname, address, metro, phone):
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.set_metro(metro)
        self.set_phone(phone)
        self.click_next_button()
