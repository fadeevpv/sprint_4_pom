from locators.order_pages_locators import FirstStepOrder, SecondStepOrder, OthersLocators
from locators.main_and_questions_pages_locators import QuestionsBlock
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
import time


class ScooterOrderPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_order_page(self):
        self.driver.get("https://qa-scooter.praktikum-services.ru/order")

    def fill_short_name(self, name):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(FirstStepOrder.input_short_name))
        self.driver.find_element(*FirstStepOrder.input_short_name).send_keys(name)

    def fill_last_name(self, last_name):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(FirstStepOrder.input_last_name))
        self.driver.find_element(*FirstStepOrder.input_last_name).send_keys(last_name)

    def fill_address(self, address):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(FirstStepOrder.input_address))
        self.driver.find_element(*FirstStepOrder.input_address).send_keys(address)

    def choose_metro_station(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(FirstStepOrder.input_metro_station))
        self.driver.find_element(*FirstStepOrder.input_metro_station).click()
        self.driver.find_element(*FirstStepOrder.metro_stations_item).click()

    def fill_phone_number(self, number):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(FirstStepOrder.input_phone_number))
        self.driver.find_element(*FirstStepOrder.input_phone_number).send_keys(number)

    def go_to_second_step_order(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(FirstStepOrder.button_next))
        self.driver.find_element(*FirstStepOrder.button_next).click()

    def choose_date_to_next_month(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(SecondStepOrder.input_delivery_date_order))
        self.driver.find_element(*SecondStepOrder.input_delivery_date_order).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(SecondStepOrder.date_picker_timeline))
        self.driver.find_element(*SecondStepOrder.button_next_month).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(SecondStepOrder.input_day_delivery))
        self.driver.find_element(*SecondStepOrder.input_day_delivery).click()

    def choose_period_rent(self, rental_period):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(SecondStepOrder.input_period_rent))
        self.driver.find_element(*SecondStepOrder.input_period_rent).click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(SecondStepOrder.input_drop_down_period_rent))
        all_periods = self.driver.find_elements(*SecondStepOrder.list_rent_periods)
        selected_period = all_periods[rental_period]
        selected_period.click()

    def choose_gray_scooter(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(SecondStepOrder.checkbox_color_gray))
        self.driver.find_element(*SecondStepOrder.checkbox_color_gray).click()

    def choose_black_scooter(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(SecondStepOrder.checkbox_color_black))
        self.driver.find_element(*SecondStepOrder.checkbox_color_black).click()

    def fill_comment(self, text):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(SecondStepOrder.input_comment))
        self.driver.find_element(*SecondStepOrder.input_comment).send_keys(text)

    def execute_order(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(SecondStepOrder.button_order))
        self.driver.find_element(*SecondStepOrder.button_order).click()

    def confirm_order(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(SecondStepOrder.button_order_confirm_order))
        confirm_button = self.driver.find_element(*SecondStepOrder.button_order_confirm_order)
        self.driver.execute_script("arguments[0].click();", confirm_button)

    def check_successful_confirmation_window(self):
        expected_message = "Заказ оформлен"
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(SecondStepOrder.confirmation_order_dialog))
        actual_message = self.driver.find_element(*SecondStepOrder.confirmation_order_dialog).text
        assert expected_message in actual_message

    def view_after_confirmation(self):
        time.sleep(3)
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(SecondStepOrder.button_view_status_of_order))
        button_view_status = self.driver.find_element(*SecondStepOrder.button_view_status_of_order)
        self.driver.execute_script("arguments[0].click();", button_view_status)

    def move_to_main_from_tracking_page_by_scooter_logo(self):
        initial_url = self.driver.current_url
        main_page_url = "https://qa-scooter.praktikum-services.ru/"
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(OthersLocators.scooter_logo))
        self.driver.find_element(*OthersLocators.scooter_logo).click()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(QuestionsBlock.heading_questions_block))
        actual_url = self.driver.current_url
        assert actual_url == main_page_url != initial_url


    def move_to_main_from_tracking_page_by_yandex_logo(self):
        initial_url = self.driver.current_url
        yandex_page_url = "https://dzen.ru/?yredirect=true"
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(OthersLocators.yandex_logo))
        self.driver.find_element(*OthersLocators.yandex_logo).click()
        next_tab = self.driver.window_handles[1]
        self.driver.switch_to.window(next_tab)
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(OthersLocators.yandex_button_search))
        actual_url = self.driver.current_url
        assert actual_url == yandex_page_url != initial_url
