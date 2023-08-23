from selenium.webdriver import Chrome

from pages_obj.catalog_page import CatalogPage
from allure import attach, attachment_type


class HomePage(CatalogPage):
    def __init__(self, webdriver: Chrome, url):
        super().__init__(webdriver=webdriver)
        self.webdriver.get(url=url)
        attach(self.webdriver.get_screenshot_as_png(), name="Home page screenshot", attachment_type=attachment_type.PNG)