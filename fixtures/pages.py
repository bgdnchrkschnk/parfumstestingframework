import pytest as pytest
from selenium import webdriver

from pages_obj.home_page import HomePage


@pytest.fixture
def home_page():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://parfums.ua/ua")
    yield HomePage(driver)
    driver.quit()
