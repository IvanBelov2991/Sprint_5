from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import (
    personal_cabinet_link,
    enter_account_link,
    input_authorization_name,
    input_authorization_password,
    enter_authorization_button,
    logo_burger,
    personal_name_in_personal_cabinet,
    constructor_button,
    build_burger,
    here_you_can_change_data_text
)


class TestMainPageNavigation:
    # Проверка входа в личный кабинет
    def test_enter_to_personal_account(self, driver):
        # Заходим на сайт и кликаем на кнопку "Войти в аккаунт"
        driver.find_element(*enter_account_link).click()
        # Ожидаем кнопку "Войти"
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(enter_authorization_button))
        # Вводим валидные Email, пароль (Пользователь уже зарегистрирован) и кликаем на вход
        driver.find_element(*input_authorization_name).send_keys('ivankobelov_4@gmail.com')
        driver.find_element(*input_authorization_password).send_keys('Onlyforyoumyfriend')
        driver.find_element(*enter_authorization_button).click()
        # Ожидаем текст на странице "Соберите бургер"
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(build_burger))
        # Кликаем на кнопку "Личный кабинет"
        driver.find_element(*personal_cabinet_link).click()
        # Ожидаем текст на странице 'В этом разделе вы можете изменить свои персональные данные'
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(here_you_can_change_data_text))
        # Проверка наличия имени в личном кабинете
        # Проверка нахождения в личном кабинете
        username = driver.find_element(*personal_name_in_personal_cabinet)
        assert username.get_attribute("value") == "Иван Сергеевич"
        assert "account" in driver.current_url

    # Проверка перехода к главной странице по клику на лого бургера
    def test_return_to_main_page_through_logo(self, driver):
        # Заходим на сайт и кликаем на кнопку "Войти в аккаунт"
        driver.find_element(*enter_account_link).click()
        # Ожидаем кнопку "Войти"
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(enter_authorization_button))
        # Вводим валидные Email, пароль (Пользователь уже зарегистрирован) и кликаем на вход
        driver.find_element(*input_authorization_name).send_keys('ivankobelov_4@gmail.com')
        driver.find_element(*input_authorization_password).send_keys('Onlyforyoumyfriend')
        driver.find_element(*enter_authorization_button).click()
        # Ожидаем текст на странице "Соберите бургер"
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(build_burger))
        # Кликаем на кнопку "Личный кабинет"
        driver.find_element(*personal_cabinet_link).click()
        # Ожидаем текст на странице "В этом разделе вы можете изменить свои персональные данные"
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(here_you_can_change_data_text))
        # Кликаем на Лого Stellar burgers
        driver.find_element(*logo_burger).click()
        # Ожидаем текст на странице "Соберите бургер"
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(build_burger))
        # Проверка нахождения на главной страницы по тексту и url
        element = driver.find_element(*build_burger)
        assert element.text == 'Соберите бургер'
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    # Проверка перехода к главной странице по кнопке Конструктор
    def test_return_to_main_page_through_button_constructor(self, driver):
        # Заходим на сайт и кликаем на кнопку "Войти в аккаунт"
        driver.find_element(*enter_account_link).click()
        # Ожидаем кнопку "Войти"
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(enter_authorization_button))
        # Вводим валидные Email, пароль (Пользователь уже зарегистрирован) и кликаем на вход
        driver.find_element(*input_authorization_name).send_keys('ivankobelov_4@gmail.com')
        driver.find_element(*input_authorization_password).send_keys('Onlyforyoumyfriend')
        driver.find_element(*enter_authorization_button).click()
        # Авторизуемся и ожидаем текст на странице "Соберите бургер"
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(build_burger))
        # Кликаем на кнопку "Личный кабинет"
        driver.find_element(*personal_cabinet_link).click()
        # Ожидаем текст на странице "В этом разделе вы можете изменить свои персональные данные"
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(here_you_can_change_data_text))
        # Кликаем на кнопку "Конструктор"
        driver.find_element(*constructor_button).click()
        # Ожидаем текст на странице "Соберите бургер"
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(build_burger))
        # Проверка нахождения на главной страницы по тексту и url
        element = driver.find_element(*build_burger)
        assert element.text == 'Соберите бургер'
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
