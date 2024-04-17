from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import data

from locators import (
    personal_cabinet_link,
    register_link,
    input_name_registration_form,
    input_email_registration_form,
    input_password_registration_form,
    registration_button,
    invalid_password_text,
    enter_authorization_button,
    enter_text
)


class TestSuccessRegistration:
    # Проверка успешной регистрации с валидными данными
    def test_success_registration(self, driver):
        # Заходим на сайт и кликаем на кнопку "Личный кабинет"
        driver.find_element(*personal_cabinet_link).click()
        # Ожидаем кнопку "Войти"
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(enter_authorization_button))
        # Кликаем на текст "Зарегистрироваться"
        driver.find_element(*register_link).click()
        # Вводим валидные имя, Email, пароль и кликаем "Зарегистрироваться"
        driver.find_element(*input_name_registration_form).send_keys(data.random_name)
        driver.find_element(*input_email_registration_form).send_keys(data.random_email)
        driver.find_element(*input_password_registration_form).send_keys(data.random_password)
        driver.find_element(*registration_button).click()
        # Ожидаем текст на странице "Войти"
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(enter_authorization_button))
        # Проверка регистрации по тексту и url
        assert driver.find_element(*enter_text), "Элемент 'Текст Вход' не найден на странице"
        assert 'login' in driver.current_url


class TestInvalidRegistration:
    # Проверка регистрации с невалидным паролем
    def test_registration_with_invalid_password(self, driver):
        # Заходим на сайт и кликаем на кнопку "Личный кабинет"
        driver.find_element(*personal_cabinet_link).click()
        # Ожидаем кнопку "Войти"
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(enter_authorization_button))
        # Кликаем на текст "Зарегистрироваться"
        driver.find_element(*register_link).click()
        # Вводим валидные имя, Email и невалидный пароль(<6 символов) и кликаем "Зарегистрироваться"
        driver.find_element(*input_name_registration_form).send_keys(data.random_name)
        driver.find_element(*input_email_registration_form).send_keys(data.random_email)
        driver.find_element(*input_password_registration_form).send_keys(12345)
        driver.find_element(*registration_button).click()
        # Ожидаем текст на странице "Некорректный пароль"
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(invalid_password_text))
        element = driver.find_element(*invalid_password_text)
        # Проверка текста на странице "Некорректный пароль" и нахождения на странице регистрации
        assert element.text == 'Некорректный пароль'
        assert 'register' in driver.current_url

    # Проверка регистрации без ввода имени
    def test_registration_without_name(self, driver):
        # Заходим на сайт и кликаем на кнопку "Личный кабинет"
        driver.find_element(*personal_cabinet_link).click()
        # Ожидаем кнопку "Войти"
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(enter_authorization_button))
        # Кликаем на текст "Зарегистрироваться"
        driver.find_element(*register_link).click()
        # Вводим валидные Email, пароль, не вводим имя и кликаем "Зарегистрироваться"
        driver.find_element(*input_email_registration_form).send_keys(data.random_email)
        driver.find_element(*input_password_registration_form).send_keys(data.random_password)
        driver.find_element(*registration_button).click()
        # Ожидаем кнопку "Зарегистрироваться" на экране
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(registration_button))
        # Проверка нахождения на странице регистрации
        assert 'register' in driver.current_url

    # Проверка регистрации с невалидным email
    def test_registration_with_invalid_email(self, driver):
        # Заходим на сайт и кликаем на кнопку "Личный кабинет"
        driver.find_element(*personal_cabinet_link).click()
        # Ожидаем кнопку "Войти"
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(enter_authorization_button))
        # Кликаем на текст "Зарегистрироваться"
        driver.find_element(*register_link).click()
        # Вводим валидные имя, пароль, невалидный email и кликаем "Зарегистрироваться"
        driver.find_element(*input_name_registration_form).send_keys(data.random_name)
        driver.find_element(*input_email_registration_form).send_keys('12345@com')
        driver.find_element(*input_password_registration_form).send_keys(data.random_password)
        driver.find_element(*registration_button).click()
        # Ожидаем кнопку "Зарегистрироваться" на экране
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(registration_button))
        # Проверка нахождения на странице по url
        assert 'register' in driver.current_url
