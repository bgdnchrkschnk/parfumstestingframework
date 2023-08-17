from data_models.parfums_menu_href import ParfumsMenuTopic
from data_models.menu_items import ParfumsMenuItems
from locators.base_page import MENU_ITEM
from pages_obj.base_page import BasePage


[print(value) for value in (ParfumsMenuTopic.NIGTI.value, ParfumsMenuItems.NISHEVA_PARF.value, MENU_ITEM.GENERAL_MENU_ITEM.value), BasePage("Fdfb").webdriver]