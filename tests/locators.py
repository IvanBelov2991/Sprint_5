from selenium.webdriver.common.by import By


# Локаторы

# Личный кабинет
personal_cabinet_link = (By.XPATH, "//a[p[text()='Личный Кабинет']]")
# Ссылка "Зарегистрироваться"
register_link = By.XPATH, "//a[text()='Зарегистрироваться']"
# Инпут для имени в форме регистрации
input_name_registration_form = By.XPATH, "//label[text()='Имя']/following-sibling::input"
# Инпут для email в форме регистрации
input_email_registration_form = By.XPATH, "//label[text()='Email']/following-sibling::input"
# Инпут для пароля в форме регистрации
input_password_registration_form = By.NAME, "Пароль"
# Кнопка "Зарегистрироваться"
registration_button = By.XPATH, "//button[text()='Зарегистрироваться']"
# Кнопка "Войти в аккаунт"
enter_account_link = By.XPATH, "//button[text()='Войти в аккаунт']"
# Инпут "Имя" в форме авторизации
input_authorization_name = By.NAME, "name"
# Инпут "Пароль" в форме авторизации
input_authorization_password = By.NAME, "Пароль"
# Кнопка "Войти" на форме авторизации
enter_authorization_button = By.XPATH, "//button[text()='Войти']"
# Кнопка "Оформить заказ"
set_an_order_button = By.XPATH, "//button[@class='button_button__33qZ0' and text()='Оформить заказ']"
# Кнопка "Восстановить пароль"
recover_password_button = By.XPATH, "//a[@class='Auth_link__1fOlj'" \
                                    " and @href='/forgot-password' and text()='Восстановить пароль']"
# Кнопка "Войти" на странице восстановления пароля
enter_authorization_button_on_recover_password_page = By.XPATH, "//a[@class='Auth_link__1fOlj'" \
                                                                " and text()='Войти']"
# Кнопка выйти (разлогиниться) в личном кабинете
logout_button = By.XPATH, "// button[text() = 'Выход']"
# Кнопка Логотип Бургера
logo_burger = By.XPATH, "/html/body/div/div/header/nav/div[@class='AppHeader_header__logo__2D0X2']"
# Кнопка Конструктор
constructor_button = By.XPATH, "//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Конструктор']"
# Неактивная кнопка Соусы
inactive_button_sauces = By.XPATH, '//div[@class="tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect"]/span[text()="Соусы"]'
# Активная кнопка Соусы
active_button_sauces = By.XPATH, '//div[@class="tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 ' \
                                 'noselect"]/span[text()="Соусы"]'
# Неактивная кнопка Начинки
inactive_button_toppings = By.XPATH, '//div[@class="tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect"]/span[text(' \
                                     ')="Начинки"]'
# Активная кнопка Начинки
active_button_toppings = By.XPATH, '//div[@class="tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 ' \
                                   'noselect"]/span[text()="Начинки"]'
# Неактивная кнопка Булки
inactive_button_buns = By.XPATH, '//div[@class="tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect"]/span[text()="Булки"]'
# Активная кнопка Булки
active_button_buns = By.XPATH, '//div[@class="tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 ' \
                               'noselect"]/span[text()="Булки"]'
# Текст "Вход"
enter_text = By.XPATH, "//h2[text()='Вход']"
# Текст "Соберите бургер"
build_burger = By.XPATH, "//h1[@class='text text_type_main-large mb-5 mt-10' and text()='Соберите бургер']"
# Текст "Некорректный пароль"
invalid_password_text = By.XPATH, "//p[text()='Некорректный пароль']"
# Текст 'В этом разделе вы можете изменить свои персональные данные'
here_you_can_change_data_text = By.XPATH, "//p[@class='Account_text__fZAIn text text_type_main-default'" \
                                          " and text()='В этом разделе вы можете изменить свои персональные данные']"
# Имя в персональном кабинете (Иван Сергеевич)
personal_name_in_personal_cabinet = By.XPATH, "//input[@class='text input__textfield" \
                                              " text_type_main-default input__textfield-disabled'" \
                                                " and @name='Name' and @value='Иван Сергеевич']"
# Раздел Соусы
sauces_button = By.XPATH, '//span[text()="Соусы"]'
# Раздел Начинки
toppings_button = By.XPATH, '//span[text()="Начинки"]'
# Раздел Булки
buns_button = By.XPATH, '//span[text()="Булки"]'
# Текст "Восстановление пароля"
recover_password_text = By.XPATH, "//h2[text()='Восстановление пароля']"
