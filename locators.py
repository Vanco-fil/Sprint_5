from selenium.webdriver.common.by import By


class Locators:
    """Локаторы для страницы авторизации/регистрации"""
    # Заголовок блока регистрации с текстом 'Регистрация'
    REGISRATION_TITLE = (By.XPATH, "//h2[text()='Регистрация']")
    # Плейсхолдер и поле ввода 'Имя'
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    # Плейсхолдер и поле ввода 'Email'
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    # Плейсхолдер и поле ввода 'Пароль'
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    # Кнопка 'Зарегистрироваться'
    REGISRATION_BUTTON = (By.XPATH, "//button[@class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa' and text()='Зарегистрироваться']")
    # Аллерт на некорректный пароль
    ALLERT_EROR_PASSWORD = (By.XPATH, "//p[@class = 'input__error text_type_main-default']")
    # Текст гиперссылка 'Зарегистрироваться' для регистрации нового пользователя
    REGISTER_LINK_BUTTON = (By.XPATH, "// a[text() = 'Зарегистрироваться']")
    # Заголовок блока авторизации с текстом 'Вход'
    HEADER_LOGIN_ENTRANCE = (By.XPATH, "//h2[text() = 'Вход']")
    # Кнопка Войти для авторизации аккаунта
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    # Текст гиперссылка 'Войти' на странице регистрации пользователя
    LOGIN_LINK_BUTTON = (By.XPATH, "//a[@class='Auth_link__1fOlj' and text()='Войти']")
    # Текст гиперссылка 'Восстановить пароль' на странице регистрации пользователя
    RESTORE_PASSWORD_LINK_BUTTON = (By.XPATH, "//a[@class='Auth_link__1fOlj' and text()='Восстановить пароль']")
    # Заголовок блока восстановления пароля с текстом
    HEADER_PASSWORD_RECOVERY = (By.XPATH, "//h2[text()='Восстановление пароля']")

    """Локаторы навбара сайта"""
    # Кнопка раздела Личного Кабинета
    PERSONAL_AREA_BUTTON = (By.XPATH, "//a[@class='AppHeader_header__link__3D_hX']/p[text()='Личный Кабинет']")
    # Кнопка раздела Конструктора
    DESIGN_BUTTON = (By.XPATH, "//a[@class='AppHeader_header__link__3D_hX']/p[text()='Конструктор']")
    # Логотип StellarBurgers
    STELLAR_LOGO_HEADER = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")

    """Локаторы на главной странице сайта"""
    # Кнопка Войти в аккаунт
    BUTTON_LOGIN_ACCOUNT = (By.XPATH, "//button[text()='Войти в аккаунт']")
    # Заголовок блока соберите бургер конструктора
    HEADER_CONSTRUCTOR = (By.XPATH, "//h1[@class='text text_type_main-large mb-5 mt-10' and text()='Соберите бургер']")
    # Кнопка раздела 'Булки' конструкторов бургеров
    BUNS_SECTION_BUTTON = (By.XPATH, '//span[@class="text text_type_main-default" and text()="Булки"]')
    # Кнопка раздела 'Соусы' конструкторов бургеров
    SAUCE_SECTION_BUTTON = (By.XPATH, '//span[@class="text text_type_main-default" and text()="Соусы"]')
    # Кнопка раздела 'Начинки' конструкторов бургеров
    FILLINGS_SECTION_BUTTTON = (By.XPATH, '//span[@class="text text_type_main-default" and text()="Начинки"]')
    # Родительский локатор кнопки раздела 'Булки' конструкторов бургеров
    PARENT_BUNS_SECTION_BUTTON = (By.XPATH, '//span[@class="text text_type_main-default" and text()="Булки"]/..')
    # Родительский локатор кнопки раздела 'Соусы' конструкторов бургеров
    PARENT_SAUCE_SECTION_BUTTON = (By.XPATH, '//span[@class="text text_type_main-default" and text()="Соусы"]/..')
    # Родительский локатор кнопки раздела 'Начинки' конструкторов бургеров
    PARENT_FILLINGS_SECTION_BUTTTON = (By.XPATH, '//span[@class="text text_type_main-default" and text()="Начинки"]//.')

    """Локаторы на странице Личного Кабинета (ЛК)"""
    # Кнопка выхода из аккаунта
    LOGOUT_BUTTON_LC = (By.XPATH, '//button[@type="button" and text()="Выход"]')
    # Кнопка профиль лк
    PROFILE_BUTTON_LC = (By.XPATH, '//a[@aria-current="page" and text()="Профиль"]')
