# Sprint_5. Покрытие UI автотестами сайт [Stellar Burgers](https://stellarburgers.nomoreparties.site)

## Структура проекта
- `Sprint_5/`
  - `tests/`
    - `conftest.py`
    - `test_login.py`
    - `test_logout.py`
    - `test_registration.py`
    - `test_transitions.py`
  - `locators.py`
  - `.gitignore`

#### conftest
Содержит стартовую фикстуру для тестов в браузере Google Chrome.


#### locators
Содержит локаторы для тестов


#### test_login
Содержит функции которые проверяют авторизацию на сайте через различные входы.

`test_login_in_main_page`
Проверяет вход по кнопке «Войти в аккаунт» на главной странице

`test_login_in_personal_account`
Проверяет вход через раздел «Личный кабинет» на сайте

`test_login_via_registration_page`
Проверяет вход через гиперссылку "Войти" на странице регистрации сайта

`test_login_via_password_recovery`
Проверяет вход через гиперссылку "Войти" на форме восстановления пароля


#### test_logout
Содержит функцию на проверку разлогина

`test_logout`
Проверяет выход из аккаунта по кнопке «Выйти» в личном кабинете


#### test_registration
Содержит функции для регистрации на сайте

`test_successful_registration`
Проверяет успешную регистрацию с валидными данными

`test_error_incorrect_password_registration`
Проверяет ошибку при регистрации с некорректным паролем


#### test_transitions
Содержит функции с кликами для перехода в различные разделы

`test_transition_to_constructor`
Проверяет переход кликом в раздел «Конструктор»

`test_transition_to_logo_burgers`
Проверяет переход по клику в логотип Stellar Burgers на главную страницу

`test_transition_to_logo_burgers`
Проверяет переход по табу в раздел «Соусы»

`test_transition_to_logo_burgers`
Проверяет переход по табу в раздел «Булки»

`test_transition_to_logo_burgers`
Проверяет переход по табу в раздел «Начинки»