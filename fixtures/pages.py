import pytest as pytest
from selenium import webdriver

from pages_obj.home_page import HomePage

'''Create logic for created command options selected'''
def get_browser_driver(browser_name:str):
    if browser_name == "chrome":
        return webdriver.Chrome()
    elif browser_name == "firefox":
        return webdriver.Firefox()
    elif browser_name == "safari":
        return webdriver.Safari()
    else:
        raise AssertionError("Wrong browser name entered!")


# @pytest.fixture
# def browser(request):
#
#     browser_name = request.config.getoption("--browser")
#
#     driver = get_browser_driver(browser_name=browser_name)
#     driver.maximize_window()
#     yield HomePage(driver)
#     driver.quit()


@pytest.fixture
def browser(request):

    url, browser_name = request.param
    driver = get_browser_driver(browser_name=browser_name)
    driver.maximize_window()
    yield HomePage(webdriver=driver, url=url)
    driver.quit()
