from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from data import default_user


class TestLogout:

    def test_logout(self, driver):
        # Проверяем выход по кнопке «Выход» в личном кабинете
        login, password = default_user()
        driver.find_element(*Locators.BUTTON_LOGIN_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            Locators.HEADER_LOGIN_ENTRANCE))
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(login)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.PERSONAL_AREA_BUTTON).click()
        logout_button = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            Locators.LOGOUT_BUTTON_LC))
        logout_button.click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            Locators.HEADER_LOGIN_ENTRANCE))
        assert driver.find_element(*Locators.LOGIN_BUTTON)
