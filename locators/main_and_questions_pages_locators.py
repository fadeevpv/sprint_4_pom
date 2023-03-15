from selenium.webdriver.common.by import By


class QuestionsBlock:
    # локаторы блока вопросов.
    # Впросы идут по порядку.
    heading_questions_block = [By.XPATH, '/html/body/div/div/div/div[5]/div[1]']
    drop_down_question_1 = [By.XPATH, '//div[@id="accordion__heading-0"]']
    drop_down_question_2 = [By.XPATH, '//div[@id="accordion__heading-1"]']
    drop_down_question_3 = [By.XPATH, '//div[@id="accordion__heading-2"]']
    drop_down_question_4 = [By.XPATH, '//div[@id="accordion__heading-3"]']
    drop_down_question_5 = [By.XPATH, '//div[@id="accordion__heading-4"]']
    drop_down_question_6 = [By.XPATH, '//div[@id="accordion__heading-5"]']
    drop_down_question_7 = [By.XPATH, '//div[@id="accordion__heading-6"]']
    drop_down_question_8 = [By.XPATH, '//div[@id="accordion__heading-7"]']


class AnswersBlock:
    # локаторы болка ответов
    # ответы идут по порядку
    answer_in_drop_down_list_1 = [By.XPATH, '//div[@id="accordion__panel-0"]/p']
    answer_in_drop_down_list_2 = [By.XPATH, '//div[@id="accordion__panel-1"]/p']
    answer_in_drop_down_list_3 = [By.XPATH, '//div[@id="accordion__panel-2"]/p']
    answer_in_drop_down_list_4 = [By.XPATH, '//div[@id="accordion__panel-3"]/p']
    answer_in_drop_down_list_5 = [By.XPATH, '//div[@id="accordion__panel-4"]/p']
    answer_in_drop_down_list_6 = [By.XPATH, '//div[@id="accordion__panel-5"]/p']
    answer_in_drop_down_list_7 = [By.XPATH, '//div[@id="accordion__panel-6"]/p']
    answer_in_drop_down_list_8 = [By.XPATH, '//div[@id="accordion__panel-7"]/p']


class GlobalVeriables:
    ANSWER_1 = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
    ANSWER_2 = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'
    ANSWER_3 = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'
    ANSWER_4 = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
    ANSWER_5 = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
    ANSWER_6 = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'
    ANSWER_7 = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'
    ANSWER_8 = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'


class MainPagesButtons:
    # блок локаторы кнопок на главной странице
    cookie_button = [By.XPATH, '//button[@id="rcc-confirm-button"]']
    order_small_button = [By.XPATH, ".//button[@class='Button_Button__ra12g']"]
    order_big_button = [By.XPATH, '/html/body/div/div/div/div[4]/div[2]/div[5]/button']
    scooter_logo_button = [By.XPATH, ".//img[@src='/assets/scooter.svg']"]
    yandex_logo_button = [By.XPATH, ".//img[@src='/assets/ya.svg']"]
