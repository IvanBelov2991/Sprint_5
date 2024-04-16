from selenium.webdriver.common.by import By


# Локаторы

# Личный кабинет
def personal_cabinet_link():
    return By.XPATH, "//a[p[text()='Личный Кабинет']]"


# Ссылка "Зарегистрироваться"
def register_link():
    return By.XPATH, "//a[text()='Зарегистрироваться']"


# Инпут для имени в форме регистрации
def input_name_registration_form():
    return By.XPATH, "//label[text()='Имя']/following-sibling::input"


# Инпут для email в форме регистрации
def input_email_registration_form():
    return By.XPATH, "//label[text()='Email']/following-sibling::input"


# Инпут для пароля в форме регистрации
def input_password_registration_form():
    return By.NAME, "Пароль"


# Кнопка "Зарегистрироваться"
def registration_button():
    return By.XPATH, "//button[text()='Зарегистрироваться']"


# Кнопка "Войти в аккаунт"
def enter_account_link():
    return By.XPATH, "//button[text()='Войти в аккаунт']"


# Инпут "Имя" в форме авторизации
def input_authorization_name():
    return By.NAME, "name"


# Инпут "Пароль" в форме авторизации
def input_authorization_password():
    return By.NAME, "Пароль"


# Кнопка "Войти" на форме авторизации
def enter_authorization_button():
    return By.XPATH, "//button[text()='Войти']"


# Кнопка "Оформить заказ"
def set_an_order_button():
    return By.XPATH, "//button[@class='button_button__33qZ0' and text()='Оформить заказ']"


# Кнопка "Восстановить пароль"
def recover_password_button():
    return By.XPATH, "//a[@class='Auth_link__1fOlj' and @href='/forgot-password' and text()='Восстановить пароль']"


# Кнопка "Войти" на странице восстановления пароля
def enter_authorization_button_on_recover_password_page():
    return By.XPATH, "//a[@class='Auth_link__1fOlj' and text()='Войти']"


# Кнопка выйти (разлогиниться) в личном кабинете
def logout_button():
    return By.XPATH, "// button[text() = 'Выход']"

# Кнопка Логотип Бургера
def logo_burger():
    return By.XPATH, "/html/body/div/div/header/nav/div[@class='AppHeader_header__logo__2D0X2']"

# Кнопка Конструктор
def constructor_button():
    return By.XPATH, "//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Конструктор']"

# Неактивная кнопка Соусы
def inactive_button_sauces():
    return By.XPATH, '//div[@class="tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect"]/span[text()="Соусы"]'

# Активная кнопка Соусы
def active_button_sauces():
    return By.XPATH, '//div[@class="tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]/span[text()="Соусы"]'


# Неактивная кнопка Начинки
def inactive_button_toppings():
    return By.XPATH, '//div[@class="tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect"]/span[text()="Начинки"]'

# Активная кнопка Начинки
def active_button_toppings():
    return By.XPATH, '//div[@class="tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]/span[text()="Начинки"]'

# Неактивная кнопка Булки
def inactive_button_buns():
    return By.XPATH, '//div[@class="tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect"]/span[text()="Булки"]'

# Активная кнопка Булки
def active_button_buns():
    return By.XPATH, '//div[@class="tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]/span[text()="Булки"]'

inactive_button_buns = inactive_button_buns()
active_button_buns = active_button_buns()
active_button_toppings = active_button_toppings()
inactive_button_toppings = inactive_button_toppings()
active_button_sauces = active_button_sauces()
inactive_button_sauces = inactive_button_sauces()
constructor_button = constructor_button()
logo_burger = logo_burger()
logout_button = logout_button()
enter_authorization_button_on_recover_password_page = enter_authorization_button_on_recover_password_page()
recover_password_button = recover_password_button()
set_an_order_button = set_an_order_button()
enter_authorization_button = enter_authorization_button()
input_authorization_password = input_authorization_password()
input_authorization_name = input_authorization_name()
enter_account_link = enter_account_link()
personal_cabinet_link = personal_cabinet_link()
register_link = register_link()
input_name_registration_form = input_name_registration_form()
input_email_registration_form = input_email_registration_form()
input_password_registration_form = input_password_registration_form()
registration_button = registration_button()
