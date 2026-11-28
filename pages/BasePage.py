from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step('Скролл к элементу')
    def scroll_to(self, locator):
        element = self.wait.until(expected_conditions.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        return element
    
    @allure.step('Клик по элементу')
    def click(self, locator):
        element = self.wait.until(expected_conditions.element_to_be_clickable(locator))
        element.click()
        return element
    
    @allure.step('Ввод текста в поле')
    def send_keys(self, locator, text):
        element = self.wait.until(expected_conditions.element_to_be_clickable(locator))
        element.send_keys(text)
        return element

    @allure.step('Получение текста элемента')
    def get_text(self, locator):
        element = self.wait.until(expected_conditions.visibility_of_element_located(locator))
        return element.text

    @allure.step('Ожидание кликабельности элемента')
    def wait_clickable(self, locator):
        return self.wait.until(expected_conditions.element_to_be_clickable(locator))

    @allure.step('Ожидание видимости элемента')
    def wait_visible(self, locator):
        return self.wait.until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Клик по перекрытому элементу через JavaScript')
    def click_by_script(self, locator):
        element = self.wait.until(expected_conditions.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].click();", element)
        return element

    @allure.step('Ожидание количества открытых окон: {count}')
    def wait_windows(self, count):
        self.wait.until(expected_conditions.number_of_windows_to_be(count))

    @allure.step('Переключение на последнее открытое окно')
    def switch_to_new_window(self):
        self.wait_windows(2)
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step('Ожидание, что адрес страницы содержит {url_part}')
    def wait_url_contains(self, url_part):
        self.wait.until(expected_conditions.url_contains(url_part))

    @allure.step('Получение текущего адреса страницы')
    def get_current_url(self):
        return self.driver.current_url