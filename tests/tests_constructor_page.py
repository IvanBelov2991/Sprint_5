from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import (
    active_button_buns,
    inactive_button_buns,
    active_button_sauces,
    inactive_button_sauces,
    inactive_button_toppings,
    active_button_toppings,
)


# Проверка перехода в раздел Соусы
def test_enter_to_souces(driver):
    # Заходим на сайт и ожидаем, что раздел Соусы неактивный
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        inactive_button_sauces))
    # Проверка, что раздел Соусы неактивный
    try:
        assert driver.find_element(
            *inactive_button_sauces).is_displayed(), "Элемент inactive_button_sauces отображается на странице"
        print("Элемент inactive_button_sauces успешно отображается на странице")
    except AssertionError as e:
        print("Ошибка:", e)
    # Кликаем на Соусы и ожидаем, что раздел Соусы активный
    driver.find_element(By.XPATH, '//span[text()="Соусы"]').click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        active_button_sauces))
    # Проверка, что раздел Соусы активный
    try:
        assert driver.find_element(
            *active_button_sauces).is_displayed(), "Элемент active_button_sauces отображается на странице"
        print("Элемент active_button_sauces успешно отображается на странице")
    except AssertionError as e:
        print("Ошибка:", e)


# Проверка перехода в раздел Начинки
def test_enter_to_toppings(driver):
    # Заходим на сайт и ожидаем, что раздел Начинки неактивный
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        inactive_button_toppings))
    # Проверка, что раздел Начинки неактивный
    try:
        assert driver.find_element(
            *inactive_button_toppings).is_displayed(), "Элемент inactive_button_toppings отображается на странице"
        print("Элемент inactive_button_toppings успешно отображается на странице")
    except AssertionError as e:
        print("Ошибка:", e)

    # Кликаем на Начинки и ожидаем, что раздел Начинки активный
    driver.find_element(By.XPATH, '//span[text()="Начинки"]').click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        active_button_toppings))
    # Проверка, что раздел Начинки активный
    try:
        assert driver.find_element(
            *active_button_toppings).is_displayed(), "Элемент active_button_toppings отображается на странице"
        print("Элемент active_button_toppings успешно отображается на странице")
    except AssertionError as e:
        print("Ошибка:", e)


# Проверка перехода в раздел Булки
def test_enter_to_buns(driver):
    # Кликаем на Соусы и ожидаем, что раздел Булки неактивный
    driver.find_element(By.XPATH, '//span[text()="Соусы"]').click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        inactive_button_buns))
    # Проверка, что раздел Булки неактивный
    try:
        assert driver.find_element(
            *inactive_button_buns).is_displayed(), "Элемент inactive_button_buns отображается на странице"
        print("Элемент inactive_button_buns успешно отображается на странице")
    except AssertionError as e:
        print("Ошибка:", e)

    # Кликаем на Булки и ожидаем, что раздел Булки активный
    driver.find_element(By.XPATH, '//span[text()="Булки"]').click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        active_button_buns))

    # Проверка, что раздел Булки активный
    try:
        assert driver.find_element(
            *active_button_buns).is_displayed(), "Элемент active_button_buns отображается на странице"
        print("Элемент active_button_buns успешно отображается на странице")
    except AssertionError as e:
        print("Ошибка:", e)
