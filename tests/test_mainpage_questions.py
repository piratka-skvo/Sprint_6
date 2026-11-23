import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.MainPageScooter import MainPageScooter

elements=[
(MainPageScooter.question_1button, MainPageScooter.question_1answer, 'наличными или картой'),
(MainPageScooter.question_2button, MainPageScooter.question_2answer, 'один заказ — один самокат'), 
(MainPageScooter.question_3button, MainPageScooter.question_3answer, 'Отсчёт времени аренды'),
(MainPageScooter.question_4button, MainPageScooter.question_4answer, 'станем расторопнее'),
(MainPageScooter.question_5button, MainPageScooter.question_5answer, 'что-то срочное'),
(MainPageScooter.question_6button, MainPageScooter.question_6answer, 'полной зарядкой'),
(MainPageScooter.question_7button, MainPageScooter.question_7answer, 'Штрафа не будет'),
(MainPageScooter.question_8button, MainPageScooter.question_8answer, 'Всем самокатов')]

class TestMainPageQuestions:
    @pytest.mark.parametrize('button, answer, expected_text', elements)
    def test_mainpage_questions_and_answers(self, driver, button, answer, expected_text):
        page = MainPageScooter(driver)
        page.click_cookie_button()
        page.scroll_to(button)
        page.click_question_button(button)
        answer_text = page.get_text(answer)
        assert expected_text in answer_text
