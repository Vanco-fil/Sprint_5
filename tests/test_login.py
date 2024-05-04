from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators


class TestLogin:
    login = "Ivan_Ashchepkov_8_123@yandex.ru"
    password = "123456"

    def test_login_in_main_page(self, driver):
        # Проверяем вход по кнопке «Войти в аккаунт» на главной
        driver.find_element(*Locators.BUTTON_LOGIN_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            Locators.HEADER_LOGIN_ENTRANCE))
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(self.login)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(self.password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.invisibility_of_element_located(
            Locators.LOGIN_BUTTON))

    def test_login_in_personal_account(self, driver):
        # Проверяем вход через кнопку «Личный кабинет»
        driver.find_element(*Locators.PERSONAL_AREA_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            Locators.HEADER_LOGIN_ENTRANCE))
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(self.login)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(self.password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.invisibility_of_element_located(
            Locators.LOGIN_BUTTON))

    def test_login_via_registration_page(self, driver):
        # Проверяем вход через кнопку в форме регистрации
        driver.find_element(*Locators.PERSONAL_AREA_BUTTON).click()
        button_register = WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.REGISTER_LINK_BUTTON))
        button_register.click()
        driver.find_element(*Locators.LOGIN_LINK_BUTTON).click()
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(self.login)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(self.password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.invisibility_of_element_located(
            Locators.LOGIN_BUTTON))

    def test_login_via_password_recovery(self, driver):
        # Проверяем вход через кнопку в форме восстановления пароля
        driver.find_element(*Locators.PERSONAL_AREA_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.REGISTER_LINK_BUTTON))
        driver.find_element(*Locators.RESTORE_PASSWORD_LINK_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.HEADER_PASSWORD_RECOVERY))
        driver.find_element(*Locators.LOGIN_LINK_BUTTON).click()
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(self.login)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(self.password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.invisibility_of_element_located(
            Locators.LOGIN_BUTTON))
