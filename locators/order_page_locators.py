from selenium.webdriver.common.by import By


class OrderPageLocators:
        # Кнопка логотипа "Самокат"
        BUTTON_LOGO_SCOOTER = [By.XPATH, './/a[@class="Header_LogoScooter__3lsAR"]']

        # Кнопка логотипа "Яндекс"
        BUTTON_LOGO_YANDEX = [By.XPATH, './/a[@class="Header_LogoYandex__3TSOI"]']

        # Панель ввода данных "Для кого самокат"
        PANEL_ORDER = [By.XPATH, './/div[@class="Order_Content__bmtHS"]']

        # Поле ввода "Имя"
        INPUT_FIRST_NAME_FIELD = [By.XPATH, './/input[@placeholder="* Имя"]']

        # Поле ввода "Фамилия"
        INPUT_SECOND_NAME_FIELD = [By.XPATH, './/input[@placeholder="* Фамилия"]']

        # Поле ввода "Адрес: куда привезти заказ"
        INPUT_ADDRESS_FIELD = [By.XPATH, './/input[@placeholder="* Адрес: куда привезти заказ"]']

        # Поле ввода "Станция метро"
        INPUT_METRO_STATION_SEARCH = [By.XPATH, './/input[@placeholder="* Станция метро"]']

        # Выпадающий список станций метро
        SELECT_SEARCH_METRO_STATION = [By.XPATH, './/input[@placeholder="* Станция метро"]//*']

        # Кнопка выбора станции для первого заказчика "Третьяковская"
        BUTTON_TVERSKAYA_STATE = [By.XPATH, './/*[text()="Тверская"]']

        # Кнопка выбора станции для второго заказчика "Рижская"
        BUTTON_RIZHSKAYA_STATE = [By.XPATH, './/*[text()="Рижская"]']

        # Поле ввода "Телефон: на него позвонит курьер"
        INPUT_PHONE_NUMBER_FIELD = [By.XPATH, './/input[@placeholder="* Телефон: на него позвонит курьер"]']

        # Кнопка "Далее"
        BUTTON_NEXT = [By.XPATH, './/button[text()="Далее"]']

        # Поле ввода "Когда привезти самокат"
        INPUT_DELIVERY_DATE = [By.XPATH, './/input[@placeholder="* Когда привезти самокат"]']

        # Выбор даты аренды самоката для первого заказчика "10.05.2025"
        SELECT_10_MAY_2025 = [By.XPATH, './/div[@aria-label="Choose суббота, 10-е мая 2025 г."]']

        # Выбор даты аренды самоката для второго заказчика "12.05.2025"
        SELECT_12_MAY_2025 = [By.XPATH, './/div[@aria-label="Choose понедельник, 12-е мая 2025 г."]']

        # Поле ввода "Срок аренды"
        SELECT_RENTAL_PERIOD = [By.XPATH, './/div[text()="* Срок аренды"]']

        # Опция срока аренды "сутки"
        OPTION_RENTAL_PERIOD_ONE_DAY = [By.XPATH, './/div[text()="сутки"]']

        # Опция срока аренды "двое суток"
        OPTION_RENTAL_PERIOD_TWO_DAY = [By.XPATH, './/div[text()="двое суток"]']

        # Опция срока аренды "трое суток"
        OPTION_RENTAL_PERIOD_THREE_DAY = [By.XPATH, './/div[text()="трое суток"]']

        # Опция срока аренды "четверо суток"
        OPTION_RENTAL_PERIOD_FOUR_DAY = [By.XPATH, './/div[text()="четверо суток"]']

        # Опция срока аренды "пятеро суток"
        OPTION_RENTAL_PERIOD_FIVE_DAY = [By.XPATH, './/div[text()="пятеро суток"]']

        # Опция срока аренды "шестеро суток"
        OPTION_RENTAL_PERIOD_SIX_DAY = [By.XPATH, './/div[text()="шестеро суток"]']

        # Опция срока аренды "семеро суток"
        OPTION_RENTAL_PERIOD_SEVEN_DAY = [By.XPATH, './/div[text()="семеро суток"]']

        # Поле ввода "Цвет самоката - чёрный жемчуг"
        CHECKBOX_BLACK_COLOR = [By.ID, 'black']

        # Поле ввода "Цвет самоката - серая безысходность"
        CHECKBOX_GREY_COLOR = [By.ID, 'grey']

        # Поле ввода "Комментарий для курьера"
        INPUT_COMMENT_FOR_COURIER = [By.XPATH, './/input[@placeholder="Комментарий для курьера"]']

        # Кнопка "Назад"
        BUTTON_MAKE_AN_ORDER = [By.XPATH, './/button[@class="Button_Button__ra12g Button_Middle__1CSJM"]']

        # Панель подтверждения заказа
        PANEL_CONFIRMATION_TO_ORDER = [By.XPATH, './/div[@class="Order_Modal__YZ-d3"]']

        # Кнопка "Заказать"
        BUTTON_ORDER = [By.XPATH, './/button[text()="Заказать"]']

        # Кнопка "Да"
        BUTTON_YES = [By.XPATH, './/button[text()="Да"]']

        # Кнопка "Нет"
        BUTTON_NO = [By.XPATH, './/button[text()="Нет"]']

        # Всплывающее окно с сообщением "Заказ оформлен"
        PANEL_SUCCESSFUl_ORDER = [By.XPATH, './/div[@class="Order_ModalHeader__3FDaJ" and text()="Заказ оформлен"]']