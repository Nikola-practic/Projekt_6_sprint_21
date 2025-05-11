from selenium.webdriver.common.by import By


class HomePageLocators:
    # Панель главной страницы Scooter
    PANEL_HOME_FIRST_PART = [By.CLASS_NAME, 'Home_FirstPart__3g6vG']

    # Верхняя кнопка "Заказать"
    BUTTON_ORDER_ON_HEADER = [By.XPATH, './/button[@class="Button_Button__ra12g"]']

    # Нижняя кнопка "Заказать"
    BUTTON_ORDER_ON_BOTTOM = [By.XPATH, './/button[@class="Button_Button__ra12g Button_Middle__1CSJM"]']

    # Панель "Вопросы о важном"
    PANEL_IMPORTANT_QUESTIONS = [By.CLASS_NAME, 'Home_FourPart__1uthg']

    # Вопрос - 0: "Сколько стоит? И как оплатить?"
    BUTTON_COST_AND_PAYMENT = [By.XPATH, './/div[@id="accordion__heading-0"]']

    # Ответ - 0: "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
    TEXT_COST_AND_PAYMENT_INFO = [By.XPATH, './/*[@id="accordion__panel-0"]/p']

    # Вопрос - 1: "Хочу сразу несколько самокатов! Так можно?"
    BUTTON_MULTIPLE_SCOOTERS = [By.XPATH, './/div[@id="accordion__heading-1"]']

    # Ответ - 1: "Пока что у нас так: один заказ — один самокат.
    # Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."
    TEXT_MULTIPLE_SCOOTERS_INFO = [By.XPATH, './/*[@id="accordion__panel-1"]/p']

    # Вопрос - 2: "Хочу сразу несколько самокатов! Так можно?"
    BUTTON_RENTAL_TIME_CALCULATION = [By.XPATH, './/div[@id="accordion__heading-2"]']

    # Ответ - 2: "Пока что у нас так: один заказ — один самокат.
    # Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."
    TEXT_RENTAL_TIME_CALCULATION_INFO = [By.XPATH, './/*[@id="accordion__panel-2"]/p']

    # Вопрос - 3: "Как рассчитывается время аренды?"
    BUTTON_ORDER_TODAY = [By.XPATH, './/div[@id="accordion__heading-3"]']

    # Ответ - 3: "опустим, вы оформляете заказ на 8 мая.
    #     # Мы привозим самокат 8 мая в течение дня.
    #     # Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру.
    #     # Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."
    TEXT_ORDER_TODAY_INFO = [By.XPATH, './/*[@id="accordion__panel-3"]/p']

    # Вопрос - 4: "Можно ли продлить заказ или вернуть самокат раньше?"
    BUTTON_EXTEND_OR_EARLY_RETURN = [By.XPATH, './/div[@id="accordion__heading-4"]']

    # Ответ - 4: "Пока что нет!
    #     # Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
    TEXT_EXTEND_OR_EARLY_RETURN_INFO = [By.XPATH, './/*[@id="accordion__panel-4"]/p']

    # Вопрос - 5: "Вы привозите зарядку вместе с самокатом?"
    BUTTON_CHARGER_INCLUDED = [By.XPATH, './/div[@id="accordion__heading-5"]']

    # Ответ - 5: "Самокат приезжает к вам с полной зарядкой.
    #     # Этого хватает на восемь суток — даже если будете кататься без передышек и во сне.
    #     # Зарядка не понадобится."
    TEXT_CHARGER_INCLUDED_INFO = [By.XPATH, './/*[@id="accordion__panel-5"]/p']

    # Вопрос - 6: "Можно ли отменить заказ?"
    BUTTON_CANCEL_ORDER = [By.XPATH, './/div[@id="accordion__heading-6"]']

    # Ответ - 6: "Да, пока самокат не привезли.
    #     # Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."
    TEXT_CANCEL_ORDER_INFO = [By.XPATH, './/*[@id="accordion__panel-6"]/p']

    # Вопрос - 7: "Я жизу за МКАДом, привезёте?"
    BUTTON_DELIVERY_BEYOND_MKAD = [By.XPATH, './/div[@id="accordion__heading-7"]']

    # Ответ - 7: "Да, обязательно. Всем самокатов! И Москве, и Московской области."
    TEXT_DELIVERY_BEYOND_INFO = [By.XPATH, './/*[@id="accordion__panel-7"]/p']