from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import (
    personal_cabinet_link,
    enter_account_link,
    input_authorization_name,
    input_authorization_password,
    enter_authorization_button,
    logo_burger,
    constructor_button
)


# Проверка входа в личный кабинет
def test_enter_to_personal_account(driver):
    # Заходим на сайт и кликаем на кнопку "Войти в аккаунт"
    driver.find_element(*enter_account_link).click()
    # Ожидаем текст на странице "Вход"
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, "//h2[text()='Вход']")))
    # Вводим валидные Email, пароль (Пользователь уже зарегистрирован) и кликаем на вход
    driver.find_element(*input_authorization_name).send_keys('ivankobelov_4@gmail.com')
    driver.find_element(*input_authorization_password).send_keys('Onlyforyoumyfriend')
    driver.find_element(*enter_authorization_button).click()
    # Ожидаем текст на странице "Соберите бургер"
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, "//h1[@class='text text_type_main-large mb-5 mt-10' and text()='Соберите бургер']")))
    # Кликаем на кнопку "Личный кабинет"
    driver.find_element(*personal_cabinet_link).click()
    # Ожидаем текст на странице "В этом разделе вы можете изменить свои персональные данные"
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, "//p[@class='Account_text__fZAIn text text_type_main-default'"
                   " and text()='В этом разделе вы можете изменить свои персональные данные']")))
    # Проверка наличия имени в личном кабинете
    # Проверка нахождения в личном кабинете
    username = driver.find_element(By.XPATH,
                                   "//input[@class='text input__textfield"
                                   " text_type_main-default input__textfield-disabled'"
                                   " and @name='Name' and @value='Иван Сергеевич']")
    assert username.get_attribute("value") == "Иван Сергеевич"
    assert "account" in driver.current_url


# Проверка перехода к главной странице по клику на лого бургера
def test_return_to_main_page_through_logo(driver):
    # Заходим на сайт и кликаем на кнопку "Войти в аккаунт"
    driver.find_element(*enter_account_link).click()
    # Ожидаем текст на странице "Вход"
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, "//h2[text()='Вход']")))
    # Вводим валидные Email, пароль (Пользователь уже зарегистрирован) и кликаем на вход
    driver.find_element(*input_authorization_name).send_keys('ivankobelov_4@gmail.com')
    driver.find_element(*input_authorization_password).send_keys('Onlyforyoumyfriend')
    driver.find_element(*enter_authorization_button).click()
    # Ожидаем текст на странице "Соберите бургер"
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, "//h1[@class='text text_type_main-large mb-5 mt-10' and text()='Соберите бургер']")))
    # Кликаем на кнопку "Личный кабинет"
    driver.find_element(*personal_cabinet_link).click()
    # Ожидаем текст на странице "В этом разделе вы можете изменить свои персональные данные"
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, "//p[@class='Account_text__fZAIn text text_type_main-default'"
                   " and text()='В этом разделе вы можете изменить свои персональные данные']")))
    # Кликаем на Лого Stellar burgers
    driver.find_element(*logo_burger).click()
    # Ожидаем текст на странице "Соберите бургер"
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, "//h1[@class='text text_type_main-large mb-5 mt-10' and text()='Соберите бургер']")))
    element = driver.find_element(By.XPATH, "//h1[@class='text text_type_main-large mb-5 mt-10'"
                                            " and text()='Соберите бургер']")
    # Проверка нахождения на главной страницы по тексту и url
    assert element.text == 'Соберите бургер'
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'


# Проверка перехода к главной странице по кнопке Конструктор
def test_return_to_main_page_through_button_constructor(driver):
    # Заходим на сайт и кликаем на кнопку "Войти в аккаунт"
    driver.find_element(*enter_account_link).click()
    # Ожидаем текст на странице "Вход"
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, "//h2[text()='Вход']")))
    # Вводим валидные Email, пароль (Пользователь уже зарегистрирован) и кликаем на вход
    driver.find_element(*input_authorization_name).send_keys('ivankobelov_4@gmail.com')
    driver.find_element(*input_authorization_password).send_keys('Onlyforyoumyfriend')
    driver.find_element(*enter_authorization_button).click()
    # Авторизуемся и ожидаем текст на странице "Соберите бургер"
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, "//h1[@class='text text_type_main-large mb-5 mt-10' and text()='Соберите бургер']")))
    # Кликаем на кнопку "Личный кабинет"
    driver.find_element(*personal_cabinet_link).click()
    # Ожидаем текст на странице "В этом разделе вы можете изменить свои персональные данные"
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, "//p[@class='Account_text__fZAIn text text_type_main-default'"
                   " and text()='В этом разделе вы можете изменить свои персональные данные']")))
    # Кликаем на кнопку "Конструктор"
    driver.find_element(*constructor_button).click()

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, "//h1[@class='text text_type_main-large mb-5 mt-10' and text()='Соберите бургер']")))
    element = driver.find_element(By.XPATH, "//h1[@class='text text_type_main-large mb-5 mt-10'"
                                            " and text()='Соберите бургер']")
    # Проверка нахождения на главной страницы по тексту и url
    assert element.text == 'Соберите бургер'
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
