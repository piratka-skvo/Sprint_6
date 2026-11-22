from selenium.webdriver.common.by import By

class MainPageScooter:
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

    def __init__(self, driver):
        self.driver = driver 

    def scroll_to_questions(self):
        element= self.driver.find_element(*self.question_8button)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def click_question1(self):
        self.driver.find_element(*self.question_1button).click()
    def click_question2(self):
        self.driver.find_element(*self.question_2button).click()
    def click_question3(self):
        self.driver.find_element(*self.question_3button).click()
    def click_question4(self):
        self.driver.find_element(*self.question_4button).click()
    def click_question5(self):
        self.driver.find_element(*self.question_5button).click()
    def click_question6(self):
        self.driver.find_element(*self.question_6button).click()
    def click_question7(self):
        self.driver.find_element(*self.question_7button).click()
    def click_question8(self):
        self.driver.find_element(*self.question_8button).click()

    def check_1answer(self):
        answer = self.driver.find_element(*self.question_1answer).text
        assert 'наличными или картой' in answer
    def check_2answer(self):
        answer = self.driver.find_element(*self.question_2answer).text
        assert 'один заказ — один самокат' in answer
    def check_3answer(self):
        answer = self.driver.find_element(*self.question_3answer).text
        assert 'Отсчёт времени аренды' in answer
    def check_4answer(self):
        answer = self.driver.find_element(*self.question_4answer).text
        assert 'станем расторопнее' in answer
    def check_5answer(self):
        answer = self.driver.find_element(*self.question_5answer).text
        assert 'что-то срочное' in answer
    def check_6answer(self):
        answer = self.driver.find_element(*self.question_6answer).text
        assert 'полной зарядкой' in answer
    def check_7answer(self):
        answer = self.driver.find_element(*self.question_7answer).text
        assert 'Штрафа не будет' in answer
    def check_8answer(self):
        answer = self.driver.find_element(*self.question_8answer).text
        assert 'Всем самокатов' in answer

    def click_order_up(self):
        self.driver.find_element(*self.order_button_up).click()

    def click_order_down(self):
        self.driver.find_element(*self.order_button_down).click()

    def click_cookie_button(self):
        self.driver.find_element(*self.cookie_button).click()
