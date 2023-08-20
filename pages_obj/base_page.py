from time import sleep

from selenium.webdriver import Chrome, ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators.base_page import MENU_ITEM
from data_models.parfums_menu_href import ParfumsMenuTopic
from data_models.menu_items import ParfumsMenuItems


class BasePage:
    def __init__(self, webdriver: Chrome):
        self.__webdriver: Chrome = webdriver
        self.__actions = ActionChains(self.__webdriver)
        self.__wait = WebDriverWait(self.__webdriver, 20)

    @property
    def webdriver(self):
        return self.__webdriver

    @property
    def actions(self):
        return self.__actions

    @property
    def wait(self):
        return self.__wait


    def __get_menu_topic_element(self, menu_topic):
        return self.__wait.until(
            EC.element_to_be_clickable((By.XPATH, MENU_ITEM.get_xpath_topic(menu_topic=menu_topic))))

    def __get_menu_item_element(self, menu_item):
        return self.__wait.until(
            EC.visibility_of_element_located((By.XPATH, MENU_ITEM.get_xpath_item(menu_item=menu_item))))

    def __navigate_to_menu_item(self, menu_topic, menu_item):
        self.__actions.move_to_element(to_element=self.__get_menu_topic_element(menu_topic=menu_topic)).perform()
        sleep(2)
        self.__get_menu_item_element(menu_item=menu_item).click()

    def go_to_women_parfums(self):
        from pages_obj.catalog_page import CatalogPage

        self.__navigate_to_menu_item(menu_topic=ParfumsMenuTopic.PARFUMERIA.value,
                                   menu_item=ParfumsMenuItems.JINOCHA_PARF.value)

        return CatalogPage(self.webdriver)