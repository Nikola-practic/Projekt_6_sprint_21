import allure
import pytest

from selenium import webdriver
from pages.home_page import HomePageScooter
from pages.order_page import OrderPageScooter


@allure.step('Открываем браузер Firefox')
@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.set_window_size(1448, 1024)
    yield driver
    driver.quit()

@allure.step('Открываем главную страницу Scooter')
@pytest.fixture
def open_home_page(driver):
    home_page = HomePageScooter(driver)
    home_page.open_home_page()
    home_page.wait_for_load_home_page()

@allure.step('Открываем страницу заказа самоката')
@pytest.fixture
def open_order_page(driver):
    order_page = OrderPageScooter(driver)
    order_page.open_order_page()
    order_page.wait_for_load_order_page()