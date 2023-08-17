from selenium.webdriver import Chrome

from pages_obj.catalog_page import CatalogPage


class HomePage(CatalogPage):
    def __init__(self, webdriver: Chrome):
        super().__init__(webdriver=webdriver)