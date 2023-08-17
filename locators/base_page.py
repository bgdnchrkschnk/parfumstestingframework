from enum import Enum

class MENU_ITEM(Enum):
    GENERAL_MENU_ITEM = "//li[contains(@class,'menu_item_first')]//a[@href='/ua/category/{menu_item}']"
    GENERAL_MENU_TOPIC = "//li[contains(@class,'menu_item_first')]/a[@href='/ua/category/{menu_topic}']"