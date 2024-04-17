import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get('https://stellarburgers.nomoreparties.site/')
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()
