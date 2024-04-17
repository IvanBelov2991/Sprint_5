from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import (
    active_button_buns,
    inactive_button_buns,
    active_button_sauces,
    inactive_button_sauces,
    inactive_button_toppings,
    active_button_toppings,
    sauces_button,
    toppings_button,
    buns_button
)


class TestConstructorBurgers:
    # Проверка перехода в раздел Соусы
    def test_enter_to_souces(self, driver):
        # Заходим на сайт и ожидаем, что раздел Соусы неактивный
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(inactive_button_sauces))
        # Проверка, что раздел Соусы неактивный
        assert driver.find_element(*inactive_button_sauces).is_displayed(),\
            "Элемент inactive_button_sauces не отображается на странице"
        # Кликаем на Соусы и ожидаем, что раздел Соусы активный
        driver.find_element(*sauces_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(active_button_sauces))
        # Проверка, что раздел Соусы активный
        assert driver.find_element(*active_button_sauces).is_displayed(),\
            "Элемент active_button_sauces не отображается на странице"

    # Проверка перехода в раздел Начинки
    def test_enter_to_toppings(self, driver):
        # Заходим на сайт и ожидаем, что раздел Начинки неактивный
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(inactive_button_toppings))
        # Проверка, что раздел Начинки неактивный
        assert driver.find_element(*inactive_button_toppings).is_displayed(),\
            "Элемент inactive_button_toppings не отображается на странице"
        # Кликаем на Начинки и ожидаем, что раздел Начинки активный
        driver.find_element(*toppings_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(active_button_toppings))
        # Проверка, что раздел Начинки активный
        assert driver.find_element(*active_button_toppings).is_displayed(),\
            "Элемент active_button_toppings не отображается на странице"

    # Проверка перехода в раздел Булки
    def test_enter_to_buns(self, driver):
        # Кликаем на Соусы и ожидаем, что раздел Булки неактивный
        driver.find_element(*sauces_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(inactive_button_buns))
        # Проверка, что раздел Булки неактивный
        assert driver.find_element(*inactive_button_buns).is_displayed(),\
            "Элемент inactive_button_buns не отображается на странице"
        # Кликаем на Булки и ожидаем, что раздел Булки активный
        driver.find_element(*buns_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(active_button_buns))
        # Проверка, что раздел Булки активный
        assert driver.find_element(*active_button_buns).is_displayed(),\
            "Элемент active_button_buns не отображается на странице"
