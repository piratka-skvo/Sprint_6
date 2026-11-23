from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from pages.BasePage import BasePage

class MainPageScooter(BasePage):
    question_title = (By.CLASS_NAME, "Home_SubHeader__zwi_E") #раздел "Вопросы о важном"
    question_1button = (By.ID, "accordion__heading-0") #кнопка 1 вопроса: Сколько это стоит? И как оплатить?
    question_1answer = (By.ID, "accordion__panel-0") #ответ на 1 вопрос: Сутки — 400 рублей. Оплата курьеру — наличными или картой.
    question_2button = (By.ID, "accordion__heading-1") #кнопка 2 вопроса: Хочу сразу несколько самокатов! Так можно?
    question_2answer = (By.ID, "accordion__panel-1") #ответ на 2 вопрос: Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями...
    question_3button = (By.ID, "accordion__heading-2") #кнопка 3 вопроса: Как рассчитывается время аренды?
    question_3answer = (By.ID, "accordion__panel-2") #ответ на 3 вопрос: ... Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру...
    question_4button = (By.ID, "accordion__heading-3") #кнопка 4 вопроса: Можно ли заказать самокат прямо на сегодня?
    question_4answer = (By.ID, "accordion__panel-3") #ответ на 4 вопрос: Только начиная с завтрашнего дня. Но скоро станем расторопнее.
    question_5button = (By.ID, "accordion__heading-4") #кнопка 5 вопроса: Можно ли продлить заказ или вернуть самокат раньше?
    question_5answer = (By.ID, "accordion__panel-4") #ответ на 5 вопрос: Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку...
    question_6button = (By.ID, "accordion__heading-5") #кнопка 6 вопроса: Вы привозите зарядку вместе с самокатом?
    question_6answer = (By.ID, "accordion__panel-5") #ответ на 6 вопрос: Самокат приезжает к вам с полной зарядкой...
    question_7button = (By.ID, "accordion__heading-6") #кнопка 7 вопроса: Можно ли отменить заказ?
    question_7answer = (By.ID, "accordion__panel-6") #ответ на 7 вопрос: Да, пока самокат не привезли. Штрафа не будет...
    question_8button = (By.ID, "accordion__heading-7") #кнопка 8 вопроса: Я жизу за МКАДом, привезёте?
    question_8answer = (By.ID, "accordion__panel-7") #ответ на 8 вопрос: ...Всем самокатов! И Москве, и Московской области.
    order_button_up=(By.CLASS_NAME, "Button_Button__ra12g") #кнопка «Заказать» в верху страницы.
    order_button_down=(By.XPATH, "//div[contains(@class, 'Home_FinishButton')]//button[contains(text(), 'Заказать')]") #кнопка «Заказать» внизу страницы.
    scooter_img = (By.XPATH, '//img[@alt="Scooter blueprint"]')
    cookie_button = (By.ID, "rcc-confirm-button")

    def click_question_button(self, button):
        element = self.wait.until(expected_conditions.presence_of_element_located(button))
        self.driver.execute_script("arguments[0].click();", element)

    def check_answer(self, locator, expected_text):
        answer = self.get_text(locator)
        assert expected_text in answer
    
    def click_order_up(self):
        self.click(self.order_button_up)

    def click_order_down(self):
        self.click(self.order_button_down)

    def click_cookie_button(self):
        self.wait.until(expected_conditions.element_to_be_clickable(self.cookie_button))
        self.click(self.cookie_button)