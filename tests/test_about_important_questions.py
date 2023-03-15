from locators.main_and_questions_pages_locators import GlobalVeriables, AnswersBlock
from pages.main_and_questions_page import MainPageScooter
import allure


class TestDropDownList:

    @allure.title('Провека ответа на первый вопрос')
    def test_check_answer_1_on_questions_1(self, driver):
        mainpaigescooter = MainPageScooter(driver)
        mainpaigescooter.open_page_scooter()
        mainpaigescooter.close_about_cooke_block()
        mainpaigescooter.wait_loading_block_about_important()
        mainpaigescooter.scroll_to_questions_block()
        mainpaigescooter.click_on_questions_1()
        expected_answer_1 = GlobalVeriables.ANSWER_1
        actual_answer_1 = driver.find_element(*AnswersBlock.answer_in_drop_down_list_1)
        assert actual_answer_1.text == expected_answer_1

    @allure.title('Провека ответа на второй вопрос')
    def test_check_answer_2_on_questions_2(self, driver):
        mainpaigescooter = MainPageScooter(driver)
        mainpaigescooter.open_page_scooter()
        mainpaigescooter.close_about_cooke_block()
        mainpaigescooter.wait_loading_block_about_important()
        mainpaigescooter.scroll_to_questions_block()
        mainpaigescooter.click_on_questions_2()
        expected_answer_2 = GlobalVeriables.ANSWER_2
        actual_answer_2 = driver.find_element(*AnswersBlock.answer_in_drop_down_list_2)
        assert actual_answer_2.text == expected_answer_2

    @allure.title('Провека ответа на третий вопрос')
    def test_check_answer_3_on_questions_3(self, driver):
        mainpaigescooter = MainPageScooter(driver)
        mainpaigescooter.open_page_scooter()
        mainpaigescooter.close_about_cooke_block()
        mainpaigescooter.wait_loading_block_about_important()
        mainpaigescooter.scroll_to_questions_block()
        mainpaigescooter.click_on_questions_3()
        expected_answer_3 = GlobalVeriables.ANSWER_3
        actual_answer_3 = driver.find_element(*AnswersBlock.answer_in_drop_down_list_3)
        assert actual_answer_3.text == expected_answer_3

    @allure.title('Провека ответа на четвертый вопрос')
    def test_check_answer_4_on_questions_4(self, driver):
        mainpaigescooter = MainPageScooter(driver)
        mainpaigescooter.open_page_scooter()
        mainpaigescooter.close_about_cooke_block()
        mainpaigescooter.wait_loading_block_about_important()
        mainpaigescooter.scroll_to_questions_block()
        mainpaigescooter.click_on_questions_4()
        expected_answer_4 = GlobalVeriables.ANSWER_4
        actual_answer_4 = driver.find_element(*AnswersBlock.answer_in_drop_down_list_4)
        assert actual_answer_4.text == expected_answer_4

    @allure.title('Провека ответа на пятый вопрос')
    def test_check_answer_5_on_questions_5(self, driver):
        mainpaigescooter = MainPageScooter(driver)
        mainpaigescooter.open_page_scooter()
        mainpaigescooter.close_about_cooke_block()
        mainpaigescooter.wait_loading_block_about_important()
        mainpaigescooter.scroll_to_questions_block()
        mainpaigescooter.click_on_questions_5()
        expected_answer_5 = GlobalVeriables.ANSWER_5
        actual_answer_5 = driver.find_element(*AnswersBlock.answer_in_drop_down_list_5)
        assert actual_answer_5.text == expected_answer_5

    @allure.title('Провека ответа на шестой вопрос')
    def test_check_answer_6_on_questions_6(self, driver):
        mainpaigescooter = MainPageScooter(driver)
        mainpaigescooter.open_page_scooter()
        mainpaigescooter.close_about_cooke_block()
        mainpaigescooter.wait_loading_block_about_important()
        mainpaigescooter.scroll_to_questions_block()
        mainpaigescooter.click_on_questions_6()
        expected_answer_6 = GlobalVeriables.ANSWER_6
        actual_answer_6 = driver.find_element(*AnswersBlock.answer_in_drop_down_list_6)
        assert actual_answer_6.text == expected_answer_6

    @allure.title('Провека ответа на седьмой вопрос')
    def test_check_answer_7_on_questions_7(self, driver):
        mainpaigescooter = MainPageScooter(driver)
        mainpaigescooter.open_page_scooter()
        mainpaigescooter.close_about_cooke_block()
        mainpaigescooter.wait_loading_block_about_important()
        mainpaigescooter.scroll_to_questions_block()
        mainpaigescooter.click_on_questions_7()
        expected_answer_7 = GlobalVeriables.ANSWER_7
        actual_answer_7 = driver.find_element(*AnswersBlock.answer_in_drop_down_list_7)
        assert actual_answer_7.text == expected_answer_7

    @allure.title('Провека ответа на восьмой вопрос')
    def test_check_answer_8_on_questions_8(self, driver):
        mainpaigescooter = MainPageScooter(driver)
        mainpaigescooter.open_page_scooter()
        mainpaigescooter.close_about_cooke_block()
        mainpaigescooter.wait_loading_block_about_important()
        mainpaigescooter.scroll_to_questions_block()
        mainpaigescooter.click_on_questions_8()
        expected_answer_8 = GlobalVeriables.ANSWER_8
        actual_answer_8 = driver.find_element(*AnswersBlock.answer_in_drop_down_list_8)
        assert actual_answer_8.text == expected_answer_8
