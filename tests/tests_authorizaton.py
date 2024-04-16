import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import conftest

from locators import (
    personal_cabinet_link,
    register_link,
    input_name_registration_form,
    input_email_registration_form,
    input_password_registration_form,
    registration_button
)


# Проверка успешной регистрации с валидными данными
def test_success_authorizaton(driver):
    # Заходим на сайт и кликаем на кнопку "Личный кабинет"
    driver.find_element(*personal_cabinet_link).click()
    # Ожидаем текст на странице "Войти"
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, "//button[text()='Войти']")))
    # Кликаем на кнопку "Зарегистрироваться"
    driver.find_element(*register_link).click()
    # Вводим валидные имя, Email, пароль и кликаем "Зарегистрироваться"
    driver.find_element(*input_name_registration_form).send_keys(conftest.random_name)
    driver.find_element(*input_email_registration_form).send_keys(conftest.random_email)
    driver.find_element(*input_password_registration_form).send_keys(conftest.random_password)
    driver.find_element(*registration_button).click()
    # Ожидаем текст на странице "Вход"
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, "//h2[text()='Вход']")))
    # Проверка регистрации по тексту и url
    element = driver.find_element(By.XPATH, "//h2[text()='Вход']")
    assert element.text == 'Вход'
    assert 'login' in driver.current_url


# Проверка регистрации с невалидным паролем
def test_authorization_with_invalid_password(driver):
    # Заходим на сайт и кликаем на кнопку "Личный кабинет"
    driver.find_element(*personal_cabinet_link).click()
    # Ожидаем текст на странице "Войти"
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, "//button[text()='Войти']")))
    # Кликаем на кнопку "Зарегистрироваться"
    driver.find_element(*register_link).click()
    # Вводим валидные имя, Email и невалидный пароль(<6 символов) и кликаем "Зарегистрироваться"
    driver.find_element(*input_name_registration_form).send_keys(conftest.random_name)
    driver.find_element(*input_email_registration_form).send_keys(conftest.random_email)
    driver.find_element(*input_password_registration_form).send_keys(12345)
    driver.find_element(*registration_button).click()
    # Ожидаем текст на странице "Некорректный пароль"
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, '//p[@class="input__error text_type_main-default" and text()="Некорректный пароль"]')))
    element = driver.find_element(By.XPATH, "//p[text()='Некорректный пароль']")
    # Проверка текста на странице "Некорректный пароль" и нахождения на странице регистрации
    assert element.text == 'Некорректный пароль'
    assert 'register' in driver.current_url


# Проверка регистрации без ввода имени
def test_authorizaton_without_name(driver):
    # Заходим на сайт и кликаем на кнопку "Личный кабинет"
    driver.find_element(*personal_cabinet_link).click()
    # Ожидаем текст на странице "Войти"
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, "//button[text()='Войти']")))
    # Вводим валидные Email, пароль, не вводим имя и кликаем "Зарегистрироваться"
    driver.find_element(*register_link).click()
    driver.find_element(*input_email_registration_form).send_keys(conftest.random_email)
    driver.find_element(*input_password_registration_form).send_keys(conftest.random_password)
    driver.find_element(*registration_button).click()
    time.sleep(1)
    # Проверка нахождения на странице регистрации
    assert 'register' in driver.current_url


# Проверка регистрации с невалидным email
def test_authorizaton_with_invalid_email(driver):
    # Заходим на сайт и кликаем на кнопку "Личный кабинет"
    driver.find_element(*personal_cabinet_link).click()
    # Ожидаем текст на странице "Войти"
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, "//button[text()='Войти']")))
    # Вводим валидные имя, пароль, невалидный email и кликаем "Зарегистрироваться"
    driver.find_element(*register_link).click()
    driver.find_element(*input_name_registration_form).send_keys(conftest.random_name)
    driver.find_element(*input_email_registration_form).send_keys('12345@com')
    driver.find_element(*input_password_registration_form).send_keys(conftest.random_password)
    driver.find_element(*registration_button).click()
    # Ожидаем, что текст на странице "Вход" не появится
    driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()
    WebDriverWait(driver, 5).until_not(expected_conditions.visibility_of_element_located(
        (By.XPATH, "//h2[text()='Вход']")))
    time.sleep(1)
    # Проверка нахождения на странице по url
    assert 'register' in driver.current_url
