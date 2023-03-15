from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.main_and_questions_pages_locators import QuestionsBlock, MainPagesButtons


class MainPageScooter:

    def __init__(self, driver):
        self.driver = driver

    def open_page_scooter(self):
        self.driver.get("https://qa-scooter.praktikum-services.ru/")

    def close_about_cooke_block(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(MainPagesButtons.cookie_button))
        self.driver.find_element(*MainPagesButtons.cookie_button).click()

    def scroll_to_questions_block(self):
        header = self.driver.find_element(*QuestionsBlock.heading_questions_block)
        self.driver.execute_script("arguments[0].scrollIntoView();", header)

    def wait_loading_block_about_important(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(QuestionsBlock.heading_questions_block))

    def click_on_questions_1(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(QuestionsBlock.heading_questions_block))
        self.driver.find_element(*QuestionsBlock.drop_down_question_1).click()

    def click_on_questions_2(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(QuestionsBlock.drop_down_question_2))
        self.driver.find_element(*QuestionsBlock.drop_down_question_2).click()

    def click_on_questions_3(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(QuestionsBlock.drop_down_question_3))
        self.driver.find_element(*QuestionsBlock.drop_down_question_3).click()

    def click_on_questions_4(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(QuestionsBlock.drop_down_question_4))
        self.driver.find_element(*QuestionsBlock.drop_down_question_4).click()

    def click_on_questions_5(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(QuestionsBlock.drop_down_question_5))
        self.driver.find_element(*QuestionsBlock.drop_down_question_5).click()

    def click_on_questions_6(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(QuestionsBlock.drop_down_question_6))
        self.driver.find_element(*QuestionsBlock.drop_down_question_6).click()

    def click_on_questions_7(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(QuestionsBlock.drop_down_question_7))
        self.driver.find_element(*QuestionsBlock.drop_down_question_7).click()

    def click_on_questions_8(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(QuestionsBlock.drop_down_question_8))
        self.driver.find_element(*QuestionsBlock.drop_down_question_8).click()

    def click_on_1st_button_order(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(MainPagesButtons.order_small_button))
        self.driver.find_element(*MainPagesButtons.order_small_button).click()

    def click_on_2nd_button_order(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(MainPagesButtons.order_big_button))
        big_button = self.driver.find_element(*MainPagesButtons.order_big_button)
        self.driver.execute_script("arguments[0].scrollIntoView();", big_button)
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(MainPagesButtons.order_big_button))
        big_button.click()

