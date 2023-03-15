from pages.main_and_questions_page import MainPageScooter
from pages.order_page import ScooterOrderPage
import allure

class TestOrderScooter:

    @allure.title('Провека  успешного заказа самоката с переходом на главную страницу заказа 1 вый набор данных ')
    @allure.feature('Заказ самоката 1')
    @allure.story('Проверяем заказ 1')
    def test_order_scooter_success_datatest_1(self, driver):
        NAME = "Васятка"
        LAST_NAME = "Басой"
        ADDRESS = "Где-то  во дворах москвы, 108-2а"
        NUMBER = "+79994955559"
        RENTAL_PERIOD = 1
        TEXT = "есь че по мелочи"

        mainpaigescooter = MainPageScooter(driver)
        mainpaigescooter.open_page_scooter()
        mainpaigescooter.close_about_cooke_block()
        mainpaigescooter.click_on_1st_button_order()
        orderscooter = ScooterOrderPage(driver)
        orderscooter.fill_short_name(NAME)
        orderscooter.fill_last_name(LAST_NAME)
        orderscooter.fill_address(ADDRESS)
        orderscooter.choose_metro_station()
        orderscooter.fill_phone_number(NUMBER)
        orderscooter.go_to_second_step_order()
        orderscooter.choose_date_to_next_month()
        orderscooter.choose_period_rent(RENTAL_PERIOD)
        orderscooter.choose_gray_scooter()
        orderscooter.fill_comment(TEXT)
        orderscooter.execute_order()
        orderscooter.confirm_order()
        orderscooter.check_successful_confirmation_window()
        orderscooter.view_after_confirmation()
        orderscooter.move_to_main_from_tracking_page_by_scooter_logo()

    @allure.title('Провека  успешного заказа самоката спереходом на страаницу яндекса  2 ой набор данных ')
    @allure.feature('Заказ самоката 2')
    @allure.story('Проверяем заказ 2')
    def test_order_scooter_success_datatest_2(self, driver):
        NAME = "Анжелла"
        LAST_NAME = "Стюардеса"
        ADDRESS = "Домодедова, гейт 2"
        NUMBER = "+79139512507"
        RENTAL_PERIOD = 2
        TEXT = "Перевидите свои устройства в режим САМОЛЕТ"

        mainpaigescooter = MainPageScooter(driver)
        mainpaigescooter.open_page_scooter()
        mainpaigescooter.close_about_cooke_block()
        mainpaigescooter.click_on_2nd_button_order()
        orderscooter = ScooterOrderPage(driver)
        orderscooter.fill_short_name(NAME)
        orderscooter.fill_last_name(LAST_NAME)
        orderscooter.fill_address(ADDRESS)
        orderscooter.choose_metro_station()
        orderscooter.fill_phone_number(NUMBER)
        orderscooter.go_to_second_step_order()
        orderscooter.choose_date_to_next_month()
        orderscooter.choose_period_rent(RENTAL_PERIOD)
        orderscooter.choose_gray_scooter()
        orderscooter.fill_comment(TEXT)
        orderscooter.execute_order()
        orderscooter.confirm_order()
        orderscooter.check_successful_confirmation_window()
        orderscooter.view_after_confirmation()
        orderscooter.move_to_main_from_tracking_page_by_yandex_logo()

    @allure.title('Провека  успешного заказа самоката с переходом на главную страницу заказа 3 тий набор данных ')
    @allure.feature('Заказ самоката 3')
    @allure.story('Проверяем заказ 3')
    def test_order_scooter_success_datatest_3(self, driver):
        NAME = "ЧереПавел"
        LAST_NAME = "Морской"
        ADDRESS = "Просторы океана 4 северной долготы"
        NUMBER = "+79986603333"
        RENTAL_PERIOD = 3
        TEXT = "кислород закончился дышать не чем"

        mainpaigescooter = MainPageScooter(driver)
        mainpaigescooter.open_page_scooter()
        mainpaigescooter.close_about_cooke_block()
        mainpaigescooter.click_on_1st_button_order()
        orderscooter = ScooterOrderPage(driver)
        orderscooter.fill_short_name(NAME)
        orderscooter.fill_last_name(LAST_NAME)
        orderscooter.fill_address(ADDRESS)
        orderscooter.choose_metro_station()
        orderscooter.fill_phone_number(NUMBER)
        orderscooter.go_to_second_step_order()
        orderscooter.choose_date_to_next_month()
        orderscooter.choose_period_rent(RENTAL_PERIOD)
        orderscooter.choose_gray_scooter()
        orderscooter.fill_comment(TEXT)
        orderscooter.execute_order()
        orderscooter.confirm_order()
        orderscooter.check_successful_confirmation_window()
        orderscooter.view_after_confirmation()
        orderscooter.move_to_main_from_tracking_page_by_scooter_logo()

    @allure.title('Провека  успешного заказа самоката спереходом на страаницу яндекса  4 ый набор данных ')
    @allure.feature('Заказ самоката 4')
    @allure.story('Проверяем заказ 4')
    def test_order_scooter_success_datatest_4(self, driver):
        NAME = "Кукуруза "
        LAST_NAME = "Царица"
        ADDRESS = "Поле номер 18 "
        NUMBER = "+78444453324"
        RENTAL_PERIOD = 4
        TEXT = "Как зашел на права поверни"

        mainpaigescooter = MainPageScooter(driver)
        mainpaigescooter.open_page_scooter()
        mainpaigescooter.close_about_cooke_block()
        mainpaigescooter.click_on_2nd_button_order()
        orderscooter = ScooterOrderPage(driver)
        orderscooter.fill_short_name(NAME)
        orderscooter.fill_last_name(LAST_NAME)
        orderscooter.fill_address(ADDRESS)
        orderscooter.choose_metro_station()
        orderscooter.fill_phone_number(NUMBER)
        orderscooter.go_to_second_step_order()
        orderscooter.choose_date_to_next_month()
        orderscooter.choose_period_rent(RENTAL_PERIOD)
        orderscooter.choose_gray_scooter()
        orderscooter.fill_comment(TEXT)
        orderscooter.execute_order()
        orderscooter.confirm_order()
        orderscooter.check_successful_confirmation_window()
        orderscooter.view_after_confirmation()
        orderscooter.move_to_main_from_tracking_page_by_yandex_logo()






