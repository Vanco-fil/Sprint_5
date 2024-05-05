from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from data import create_random_user, incorrect_password_user


class TestBurgerRegistration:

    def test_successful_registration(self, driver):
        # Проверяем успешную регистрацию
        name, login, password = create_random_user()
        driver.find_element(*Locators.PERSONAL_AREA_BUTTON).click()
        button_register = WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.REGISTER_LINK_BUTTON))
        button_register.click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            Locators.REGISRATION_TITLE))
        driver.find_element(*Locators.NAME_INPUT).send_keys(name)
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(login)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.REGISRATION_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            Locators.LOGIN_BUTTON))
        assert driver.find_element(*Locators.HEADER_LOGIN_ENTRANCE)

    def test_error_incorrect_password_registration(self, driver):
        # Проверяем ошибку для некорректного пароля
        name, login, password = incorrect_password_user()
        driver.find_element(*Locators.PERSONAL_AREA_BUTTON).click()
        button_register = WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.REGISTER_LINK_BUTTON))
        button_register.click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            Locators.REGISRATION_TITLE))
        driver.find_element(*Locators.NAME_INPUT).send_keys(name)
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(login)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.REGISRATION_BUTTON).click()
        input_error_element = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            Locators.ALLERT_EROR_PASSWORD))
        assert input_error_element.text == 'Некорректный пароль'
