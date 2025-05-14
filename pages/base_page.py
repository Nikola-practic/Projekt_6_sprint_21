import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Перейти на страницу')
    def navigate(self, url):
        self.driver.get(url)

    @allure.step('Перейти на текущий адрес')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Подождать появление элемента')
    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step('Подождать видимости элемента')
    def wait_for_element(self, locator, timeout=25):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step('Скролл до элемента')
    def scroll_into_view(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView()", locator)

    @allure.step('Кликнуть по элементу')
    def click_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        element.click()

    @allure.step("Получить текст элемента")
    def get_text_on_element(self, locator, timeout=30):
        element = self.wait_for_element(locator, timeout)
        return element.text

    @allure.step('Подождать перехода на панель заказа')
    def panel_confirm_order_is_displayed(self, locator):
        panel_confirm_order = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))
        return panel_confirm_order.is_displayed()

    @allure.step('Переключиться на новое окно')
    def switch_to_new_window(self):
        window_handles = self.driver.window_handles
        if len(window_handles) > 1:
            self.driver.switch_to.window(window_handles[1])
        else:
            raise Exception("Нет дополнительного окна для переключения")

