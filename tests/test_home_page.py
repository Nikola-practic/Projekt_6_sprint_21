import allure
import pytest

from pages.home_page import HomePageScooter
from data import data_for_test_important_questions

class TestImportantQuestions:
    @allure.title('Проверка открытия соответствующего текста ответа на вопрос')
    @pytest.mark.parametrize("button_locator, text_locator, expected_text", data_for_test_important_questions)
    def test_open_and_check_text(self, driver, button_locator, text_locator, expected_text, open_home_page):
        # Создаём объект класса
        home_page = HomePageScooter(driver)

        # Ждём загрузки главной страницы Scooter
        home_page.wait_for_load_home_page()

        # Скроллим до раздела "Вопросы о важном"
        home_page.scroll_to_important_questions()

        # Ждём загрузки вопроса на странице
        home_page.wait_for_load_question(button_locator)

        # Нажимаем на нужный вопрос
        home_page.click_question(button_locator)

        # Ждём загрузки ответа на вопрос
        home_page.wait_for_load_info(text_locator)

        # Получаем текст ответа на вопрос
        actual_result = home_page.get_info_text(text_locator)

        # Проверяем, что текст ответа совпал с ожидаемым текстом
        assert actual_result == expected_text, f'Ожидаемый текст: "{expected_text}", но получили: "{actual_result}".'