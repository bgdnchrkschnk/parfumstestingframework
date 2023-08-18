from enum import Enum
from data_models.parfums_menu_href import ParfumsMenuTopic

class MENU_ITEM(Enum):

    def get_xpath_topic(menu_topic: str):
        return f"//li[contains(@class,'menu_item_first')]/a[@href='/ua/category/{menu_topic}']"


    def get_xpath_item(menu_item: str):
        return f"//li[contains(@class,'menu_item_first')]//a[@href='/ua/category/{menu_item}']"
