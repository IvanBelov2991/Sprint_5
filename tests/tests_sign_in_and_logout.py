from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import data
from locators import (
    personal_cabinet_link,
    enter_account_link,
    input_authorization_name,
    input_authorization_password,
    enter_authorization_button,
    enter_authorization_button_on_recover_password_page,
    recover_password_button,
    logout_button,
    build_burger,
    here_you_can_change_data_text,
    recover_password_text
)


class TestLogin:
    # Проверка входа по кнопке «Войти в аккаунт» на главной
    def test_sign_in_through_button_on_main_page(self, driver):
        # Заходим на сайт и кликаем на кнопку "Войти в аккаунт"
        driver.find_element(*enter_account_link).click()
        # Ожидаем кнопку "Войти"
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(enter_authorization_button))
        # Вводим валидные Email, пароль (Пользователь уже зарегистрирован) и кликаем на кнопку вход
        driver.find_element(*input_authorization_name).send_keys('ivankobelov_4@gmail.com')
        driver.find_element(*input_authorization_password).send_keys('Onlyforyoumyfriend')
        driver.find_element(*enter_authorization_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(build_burger))
        element = driver.find_element(*build_burger)
        # Проверка нахождения на главной страницы по тексту и url
        assert element.text == 'Соберите бургер'
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    # Проверка входа через кнопку «Личный кабинет»
    def test_sign_in_through_personal_account_form(self, driver):
        # Заходим на сайт и кликаем на кнопку "Личный кабинет"
        driver.find_element(*personal_cabinet_link).click()
        # Ожидаем кнопку "Войти"
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(enter_authorization_button))
        # Вводим валидные Email, пароль (Пользователь уже зарегистрирован) и кликаем на кнопку вход
        driver.find_element(*input_authorization_name).send_keys('ivankobelov_4@gmail.com')
        driver.find_element(*input_authorization_password).send_keys('Onlyforyoumyfriend')
        driver.find_element(*enter_authorization_button).click()
        # Ожидаем текст на странице "Соберите бургер"
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(build_burger))
        element = driver.find_element(*build_burger)
        # Проверка нахождения на главной страницы по тексту и url
        assert element.text == 'Соберите бургер'
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    # Проверка входа через кнопку в форме восстановления пароля
    def test_sign_in_through_button_recover_password(self, driver):
        # Заходим на сайт и кликаем на кнопку "Личный кабинет"
        driver.find_element(*personal_cabinet_link).click()
        # Ожидаем кнопку "Войти"
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(enter_authorization_button))
        # Кликаем на кнопку "Восстановить пароль" и ожидаем текст "Восстановление пароля"
        driver.find_element(*recover_password_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(recover_password_text))
        # Проверка нахождения на странице "Восстановление пароля"
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/forgot-password'
        # Кликаем на кнопку "Войти"
        driver.find_element(*enter_authorization_button_on_recover_password_page).click()
        # Ожидаем кнопку "Войти"
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(enter_authorization_button))
        # Вводим валидные Email, пароль (Пользователь уже зарегистрирован) и кликаем на кнопку вход
        driver.find_element(*input_authorization_name).send_keys('ivankobelov_4@gmail.com')
        driver.find_element(*input_authorization_password).send_keys('Onlyforyoumyfriend')
        driver.find_element(*enter_authorization_button).click()
        # Ожидаем текст на странице "Соберите бургер"
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(build_burger))
        element = driver.find_element(*build_burger)
        # Проверка нахождения на главной страницы по тексту и url
        assert element.text == 'Соберите бургер'
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    # Проверка входа без предварительной авторизации (невалидные вводные)
    def test_sign_in_with_invalid_data(self, driver):
        # Заходим на сайт и кликаем на кнопку "Войти в аккаунт"
        driver.find_element(*enter_account_link).click()
        # Ожидаем кнопку "Войти"
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(enter_authorization_button))
        # Вводим невалидные рандомные Email, пароль и кликаем на кнопку вход
        driver.find_element(*input_authorization_name).send_keys(data.random_email)
        driver.find_element(*input_authorization_password).send_keys(data.random_password)
        driver.find_element(*enter_authorization_button).click()
        # Ожидаем, что текст "Соберите бургер" не появится на странице
        WebDriverWait(driver, 5).until_not(expected_conditions.visibility_of_element_located(build_burger))
        # Проверка, что логин не прошёл, и мы остались на странице входа по url
        assert 'login' in driver.current_url


class TestLogout:
    # Проверка выхода из аккаунта
    def test_log_out(self, driver):
        # Заходим на сайт и кликаем на кнопку "Личный кабинет"
        driver.find_element(*personal_cabinet_link).click()
        # Ожидаем кнопку "Войти"
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(enter_authorization_button))
        # Вводим валидные Email, пароль (Пользователь уже зарегистрирован) и кликаем на кнопку вход
        driver.find_element(*input_authorization_name).send_keys('ivankobelov_4@gmail.com')
        driver.find_element(*input_authorization_password).send_keys('Onlyforyoumyfriend')
        driver.find_element(*enter_authorization_button).click()
        # Ожидаем текст на странице "Соберите бургер"
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(build_burger))
        # Заходим на сайт и кликаем на кнопку "Личный кабинет"
        driver.find_element(*personal_cabinet_link).click()
        # Ожидаем текст на странице 'В этом разделе вы можете изменить свои персональные данные'
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(here_you_can_change_data_text))
        # Кликаем на кнопку "Выход"
        driver.find_element(*logout_button).click()
        # Ожидаем кнопку "Войти" на странице
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(enter_authorization_button))
        # Проверка разлогина и нахождения на главной страницы по тексту и url
        element = driver.find_element(*enter_authorization_button)
        assert element.text == 'Войти'
        assert 'login' in driver.current_url
