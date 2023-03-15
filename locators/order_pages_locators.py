from selenium.webdriver.common.by import By
import random
val = random.randrange(1, 10)
day = random.randrange(10, 14)
class FirstStepOrder:
    # блок локаторов для первой страницы заказа
    input_short_name = [By.XPATH, ".//input[@placeholder='* Имя']"]
    input_last_name = [By.XPATH, ".//input[@placeholder='* Фамилия']"]
    input_address = [By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"]
    input_metro_station = [By.XPATH, ".//input[@placeholder='* Станция метро']"]
    metro_stations_item = [By.XPATH, '//button[@value="'+ str(val) +'"]']
    input_phone_number = [By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']"]
    button_next =  [By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]']

class SecondStepOrder:
    # блок локаторов для второй страницы заказа
    input_delivery_date_order = [By.XPATH, '//input[@placeholder="* Когда привезти самокат"]']
    date_picker_timeline = [By.XPATH, ".//div[@class='react-datepicker__month-container']"]
    button_next_month = [By.XPATH, ".//button[@aria-label='Next Month']"]
    input_day_delivery = [By.XPATH, '//div[@class="react-datepicker__day react-datepicker__day--'+ '0' +str(day) +'"]']
    input_period_rent = [By.XPATH, ".//div[text()='* Срок аренды']"]
    input_drop_down_period_rent = [By.XPATH, ".//div[@class='Dropdown-root is-open']//div[@class='Dropdown-menu']"]
    list_rent_periods = [By.XPATH, ".//div[@class='Dropdown-root is-open']//div[@class='Dropdown-option']"]
    checkbox_color_black = [By.XPATH, '//input[@id="black"]']
    checkbox_color_gray = [By.XPATH, '//input[@id="grey"]']
    input_comment = [By.XPATH, ".//input[@placeholder='Комментарий для курьера']"]
    button_order = [By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"]
    button_order_confirm_order = [By.XPATH, ".//button[text()='Да']"]
    confirmation_order_dialog = [By.XPATH, ".//div[@class='Order_ModalHeader__3FDaJ']"]
    button_view_status_of_order = [By.XPATH, ".//button[text()='Посмотреть статус']"]

class OthersLocators:
    # Блок локаторо для кнопок и иконок
    scooter_logo = [By.XPATH, ".//img[@src='/assets/scooter.svg']"]
    yandex_logo = [By.XPATH, ".//img[@src='/assets/ya.svg']"]
    yandex_button_search = [By.XPATH, ".//button[text()='Найти']"]