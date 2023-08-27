from selenium.webdriver.common.by import By
from locators.catalog_item import CatalogItem

class CatalogItemElement:
    def __init__(self, web_element):
        self.__web_element = web_element

    @property
    def price(self):
        element = self.__web_element.find_element(By.XPATH, str(CatalogItem.get_element_price_by_title_xpath()))
        return element.text
