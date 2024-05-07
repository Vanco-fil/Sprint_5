from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators


class TestTransitions:

    def test_transition_to_constructor(self, driver):
        # Проверяем переход на «Конструктор»
        driver.find_element(*Locators.PERSONAL_AREA_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.REGISTER_LINK_BUTTON))
        driver.find_element(*Locators.DESIGN_BUTTON).click()
        assert driver.find_element(*Locators.HEADER_CONSTRUCTOR)

    def test_transition_to_logo_burgers(self, driver):
        # Проверяем переход по клику на логотип Stellar Burgers
        driver.find_element(*Locators.PERSONAL_AREA_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.REGISTER_LINK_BUTTON))
        driver.find_element(*Locators.STELLAR_LOGO_HEADER).click()
        assert driver.find_element(*Locators.HEADER_CONSTRUCTOR)

    def test_transition_to_sauce_section(self, driver):
        # Проверяем переход по разделу «Соусы»
        driver.find_element(*Locators.SAUCE_SECTION_BUTTON).click()
        parent_sauce_button = driver.find_element(*Locators.PARENT_SAUCE_SECTION_BUTTON).get_attribute('class')
        assert 'tab_tab_type_current__2BEPc' in parent_sauce_button

    def test_transition_to_buns_section(self, driver):
        # Проверяем переход по разделу «Булки»
        driver.find_element(*Locators.SAUCE_SECTION_BUTTON).click()
        buns_button_unselected = driver.find_element(*Locators.PARENT_BUNS_SECTION_BUTTON).get_attribute('class')
        assert not 'tab_tab_type_current__2BEPc' in buns_button_unselected
        driver.find_element(*Locators.BUNS_SECTION_BUTTON).click()
        buns_button_selected = driver.find_element(*Locators.PARENT_BUNS_SECTION_BUTTON).get_attribute('class')
        assert buns_button_selected != buns_button_unselected

    def test_transition_to_fillings_section(self, driver):
        # Проверяем переход по разделу «Начинки»
        driver.find_element(*Locators.SAUCE_SECTION_BUTTON).click()
        parent_fillings_button = driver.find_element(*Locators.PARENT_SAUCE_SECTION_BUTTON).get_attribute('class')
        assert 'tab_tab_type_current__2BEPc' in parent_fillings_button
