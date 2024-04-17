import random
import string


def generate_random_email():
    domains = ["ya.ru", "gmail.com", "mail.ru"]
    return f"{generate_random_name(5)}@{random.choice(domains)}"


def generate_random_password(length):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))


def generate_random_name(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))
