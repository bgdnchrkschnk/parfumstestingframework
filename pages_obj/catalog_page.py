from pages_obj.base_page import *
from locators.catalog_item import CatalogItem
from web_elements.catalog_item import CatalogItemElement


class CatalogPage(BasePage):
    def __find_catalog_item_by_title(self, title: str):
        return self.wait.until(
            EC.element_to_be_clickable((By.XPATH, str(CatalogItem.get_element_by_title_xpath(title=title)))))

    def find_item_by_title(self, title:str):
        return self.__find_catalog_item_by_title(title=title)

    def get_price(self, title:str):
        element = self.find_item_by_title(title=title)
        el = CatalogItemElement(web_element=element)
        return el.price
