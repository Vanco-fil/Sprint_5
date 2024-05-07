import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def driver():
    """Фикстура для запуска браузера Google Chrome."""
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site")
    yield driver
    driver.quit()
