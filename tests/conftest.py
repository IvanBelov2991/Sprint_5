import random
import string
import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get('https://stellarburgers.nomoreparties.site/')
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


def generate_random_email():
    domains = ["ya.ru", "gmail.com", "mail.ru"]
    return f"{generate_random_name(5)}@{random.choice(domains)}"


def generate_random_password(length):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))


def generate_random_name(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


random_email = generate_random_email()
random_password = generate_random_password(6)
random_name = generate_random_name(8)
