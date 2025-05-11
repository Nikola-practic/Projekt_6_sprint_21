import allure
import curl

from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage


class HomePageScooter(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Открываем главную страницу Scooter")
    def open_home_page(self):
        self.navigate(curl.SCOOTER_HOME_PAGE)

    @allure.step("Ждём загрузки главной страницы Scooter")
    def wait_for_load_home_page(self):
        self.wait_for_element(HomePageLocators.PANEL_HOME_FIRST_PART)

    @allure.step('Скроллим до раздела "Вопросы о важном"')
    def scroll_to_important_questions(self):
        element = self.find_element(HomePageLocators.PANEL_IMPORTANT_QUESTIONS)
        self.scroll_into_view(element)

    @allure.step('Скроллим до кнопки "Заказать" внизу страницы')
    def scroll_down_to_button_order(self):
        element = self.find_element(HomePageLocators.BUTTON_ORDER_ON_BOTTOM)
        self.scroll_into_view(element)

    @allure.step('Ждём загрузки кнопки "Заказать" внизу страницы')
    def wait_for_load_down_button_order(self):
        self.wait_for_element(HomePageLocators.BUTTON_ORDER_ON_BOTTOM)

    @allure.step('Нажимаем на кнопку "Заказать" внизу страницы')
    def click_button_order_bottom(self):
        self.click_element(HomePageLocators.BUTTON_ORDER_ON_BOTTOM)

    @allure.step('Нажимаем на кнопку "Заказать" вверху страницы')
    def click_button_order_on_header(self):
        self.click_element(HomePageLocators.BUTTON_ORDER_ON_HEADER)

    @allure.step("Нажимаем на нужный вопрос")
    def click_question(self, locator):
        self.click_element(locator)

    @allure.step("Ждём загрузки вопроса на странице")
    def wait_for_load_question(self, locator):
        self.wait_for_element(locator)

    @allure.step("Ждём загрузки ответа на вопрос")
    def wait_for_load_info(self, locator):
        self.wait_for_element(locator)

    @allure.step("Ждём загрузки элемента")
    def wait_for_load_element(self, locator):
        self.wait_for_element(locator)

    @allure.step("Получаем текст ответа на вопрос")
    def get_info_text(self, locator):
         return self.get_text_on_element(locator)

    @allure.step("Получаем текущий адрес страницы")
    def get_my_current_url(self):
        self.get_current_url()