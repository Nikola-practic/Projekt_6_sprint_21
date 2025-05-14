import allure
import curl


from pages.home_page_yandex import HomePageYandex
from pages.order_page import OrderPageScooter
from pages.home_page import HomePageScooter
from data import User1
from  data import User2


class TestOrderPage:

    @staticmethod
    def order_handler(driver, user):

        # Создаём объект страницы заказа
        order_page = OrderPageScooter(driver)
        
        # Вводим имя
        order_page.enter_first_name(user.first_name)

        # Вводим фамилию
        order_page.enter_second_name(user.second_name)

        # Вводим адрес
        order_page.enter_address(user.address)

        # Наводим на поле станции метро
        order_page.enter_metro_station(user.metro_station)

        # Подождать появление выпадающего списка станций метро
        order_page.wait_for_element(user.metro_selection)

        # Выбираем станцию метро из селектора
        order_page.choose_metro_station(user.metro_selection)

        # Вводим номер телефона
        order_page.enter_phone_number(user.phone_number)

        # Нажимаем на кнопку "Далее"
        order_page.click_button_next()

        # Нажимаем на поле "Когда привезти самокат"
        order_page.enter_delivery_date(user.delivery_date)

        # Выбираем нужную дату в календаре
        order_page.select_delivery_date(user.date_selection)

        # Нажимаем на поле "Срок аренды"
        order_page.click_to_select_rental_period()

        # Выбираем срок аренды
        order_page.choose_rental_period(user.rental_period)

        # Выбираем цвет самоката
        order_page.choose_scooter_color(user.scooter_color)

        # Пишем комментарий для курьера
        order_page.enter_comment_for_courier(user.courier_comment)

        # Нажимаем на кнопку "Заказать"
        order_page.click_make_an_order()

        # Ждём загрузки окна подтверждения заказа
        order_page.wait_for_load_confirmation_order()

        # Нажимаем "Да" чтобы подтвердить заказ
        order_page.click_button_yes_to_confirm_order()

        # Ждём загрузки окна об успешном заказе
        return order_page.wait_for_load_successful_order()

    @allure.title('Позитивная проверка заказа самоката по верхней кнопке')
    def test_make_an_order_on_header(self, driver, open_home_page):

        # Создаём объект главной страницы
        home_page = HomePageScooter(driver)

        # Нажимаем на кнопку "Заказать" вверху страницы
        home_page.click_button_order_on_header()

        # Вызываем метод ввода данных User1
        TestOrderPage.order_handler(driver, user=User1)

        # Создаём объект страницы заказа
        order_page = OrderPageScooter(driver)

        # Проверяем, что заказ успешно оформлен
        assert order_page.successful_order_is_displayed(),'Окно с сообщением об успешном создании заказа не отобразилось.'

    @allure.title('Позитивная проверка заказа самоката по нижней кнопке')
    def test_make_an_order_bottom(self, driver, open_home_page):

        # Создаём объект главной страницы
        home_page = HomePageScooter(driver)

        # Скроллим до кнопки "Заказать" внизу страницы
        home_page.scroll_down_to_button_order()

        # Ждём загрузки кнопки "Заказать" внизу страницы
        home_page.wait_for_load_down_button_order()

        # Нажимаем на кнопку "Заказать" внизу страницы
        home_page.click_button_order_bottom()

        # Вызываем метод ввода данных User2
        TestOrderPage.order_handler(driver, user=User2)

        # Создаём объект страницы заказа
        order_page = OrderPageScooter(driver)

        # Проверяем, что заказ успешно оформлен
        assert order_page.successful_order_is_displayed(), 'Окно с сообщением об успешном создании заказа не отобразилось.'


class TestLogoNavigation:
    @allure.title('Проверка перехода на главную страницу "Самоката" при нажатии на логотип "Самокат"')
    def test_clicking_scooter_logo_navigates_to_home_page(self, driver, open_order_page):

        # Создаём объект класса
        order_page = OrderPageScooter(driver)

        # Нажимаем на логотип "Самокат"
        order_page.click_button_logo_scooter()

        # Создаём объект класса
        home_page = HomePageScooter(driver)

        # Ждём загрузки главной страницы Самоката
        home_page.wait_for_load_home_page()

        # Перейти на текущий адрес
        actual_result = home_page.get_current_url()

        # URL главной страницы Самоката
        expected_result = curl.SCOOTER_HOME_PAGE

        # Проверяем, что осуществлен переход на главную страницу Самоката
        assert actual_result == expected_result, f'Ожидаемый адрес: {actual_result}, но получили: {expected_result}'

    @allure.title('Проверка перехода на главную страницу "Дзена" при нажатии на логотип Яндекса')
    def test_clicking_yandex_logo_navigates_to_yandex_home_page(self, driver, open_order_page):

        # Создаём объект класса
        order_page = OrderPageScooter(driver)

        # Нажимаем на логотип "Яндекс"
        order_page.click_button_logo_yandex()

        # Создаём объект класса
        home_page_yandex = HomePageYandex(driver)

        # Переключаемся на новое окно
        home_page_yandex.switch_to_new_window()

        # Ждём загрузки главной страницы Яндекс.Дзен
        home_page_yandex.wait_for_load_home_page()

        # Получаем текущий адрес страницы
        actual_result = home_page_yandex.get_current_url()
        #actual_result = order_page.get_current_url()

        # URL страницы Яндекс.Дзен
        expected_result = curl.YANDEX_HOME_PAGE

        # Проверяем, что осуществлен переход на страницу Яндекс.Дзен
        assert actual_result == expected_result, f'Ожидаемый адрес: {actual_result}, но получили: {expected_result}'