import random
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators


class TestBurgerRegistration:
    login = f"Ivan_Ashchepkov_8_{random.randint(100, 999)}@yandex.ru"
    password = random.randint(100000, 999999)

    def test_successful_registration(self, driver):
        # Проверяем успешную регистрацию
        driver.find_element(*Locators.PERSONAL_AREA_BUTTON).click()
        button_register = WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.REGISTER_LINK_BUTTON))
        button_register.click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            Locators.REGISRATION_TITLE))
        driver.find_element(*Locators.NAME_INPUT).send_keys("Иван")
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(self.login)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(self.password)
        driver.find_element(*Locators.REGISRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            Locators.HEADER_LOGIN_ENTRANCE))

    def test_error_incorrect_password_registration(self, driver):
        # Проверяем ошибку для некорректного пароля
        driver.find_element(*Locators.PERSONAL_AREA_BUTTON).click()
        button_register = WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.REGISTER_LINK_BUTTON))
        button_register.click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            Locators.REGISRATION_TITLE))
        driver.find_element(*Locators.NAME_INPUT).send_keys("Иван")
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(self.login)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys("12345")
        driver.find_element(*Locators.REGISRATION_BUTTON).click()
        input_error_element = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            Locators.ALLERT_EROR_PASSWORD))
        assert input_error_element.text == 'Некорректный пароль'
