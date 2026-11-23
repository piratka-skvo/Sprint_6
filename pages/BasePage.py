from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def scroll_to(self, locator):
        element = self.wait.until(expected_conditions.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        return element

    def click(self, locator):
        element = self.wait.until(expected_conditions.element_to_be_clickable(locator))
        element.click()
        return element

    def send_keys(self, locator, text):
        element = self.wait.until(expected_conditions.element_to_be_clickable(locator))
        element.send_keys(text)
        return element

    def get_text(self, locator):
        element = self.wait.until(expected_conditions.visibility_of_element_located(locator))
        return element.text