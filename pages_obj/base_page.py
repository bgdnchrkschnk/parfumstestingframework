from time import sleep

from allure import step, attach, attachment_type
from selenium.common import NoSuchElementException
from selenium.webdriver import Chrome, ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators.base_page import MENU_ITEM
from data_models.parfums_menu_href import ParfumsMenuTopic
from data_models.menu_items import ParfumsMenuItems


class BasePage:
    def __init__(self, webdriver: Chrome, logger):
        self.__webdriver: Chrome = webdriver
        self.__actions = ActionChains(self.__webdriver)
        self.__wait = WebDriverWait(self.__webdriver, 20)
        self.__logger = logger


    @property
    def webdriver(self):
        return self.__webdriver

    @property
    def actions(self):
        return self.__actions

    @property
    def wait(self):
        return self.__wait

    @property
    def logger(self):
        return self.__logger


    def __get_menu_topic_element(self, menu_topic):
        try:
            self.logger.debug(f"Searching {menu_topic} element on page with {MENU_ITEM.get_xpath_topic(menu_topic=menu_topic)} XPath locator")
            menu_topic_element = self.__wait.until(
                EC.element_to_be_clickable((By.XPATH, MENU_ITEM.get_xpath_topic(menu_topic=menu_topic))))
            return menu_topic_element
        except TimeoutError as te:
            self.logger.error(f"Menu topic element has not been found by {MENU_ITEM.get_xpath_topic(menu_topic=menu_topic)} locator")
            raise TimeoutError(str(te))


    def __get_menu_item_element(self, menu_item):
        try:
            self.logger.debug(f"Searching {menu_item} element on page with {MENU_ITEM.get_xpath_item(menu_item=menu_item)} XPath locator")
            menu_item_element = self.__wait.until(
                EC.visibility_of_element_located((By.XPATH, MENU_ITEM.get_xpath_item(menu_item=menu_item))))
            return menu_item_element
        except TimeoutError as te:
            self.logger.error(f"Menu item element has not been found by {ENU_ITEM.get_xpath_item(menu_item=menu_item)} locator")
            raise TimeoutError(str(te))


    def __navigate_to_menu_item(self, menu_topic, menu_item):
        try:
            self.logger.debug(f"Moving to {menu_topic} element...")
            self.__actions.move_to_element(to_element=self.__get_menu_topic_element(menu_topic=menu_topic)).perform()
            sleep(2)
            self.logger.debug(f"Clicking on {menu_item} element...")
            self.__get_menu_item_element(menu_item=menu_item).click()
        except NoSuchElementException as ns:
            self.logger.error(f"Moving on {menu_topic} or clicking on {menu_item} is unsuccessfull :(")
            raise NoSuchElementException(str(ns))



    @step("Navigate to women parfums catalog - jinocha parfum")
    def go_to_women_parfums(self):
        from pages_obj.catalog_page import CatalogPage
        try:
            self.logger.info(f"Navigating to women parfumeria item...With ParfumsMenuTopic.PARFUMERIA.value, ParfumsMenuItems.JINOCHA_PARF.value")
            self.__navigate_to_menu_item(menu_topic=ParfumsMenuTopic.PARFUMERIA.value, menu_item=ParfumsMenuItems.JINOCHA_PARF.value)
            self.logger.info("Making a png screenshot...")
            attach(self.webdriver.get_screenshot_as_png(), name="Screenshot of women parfums page", attachment_type=attachment_type.PNG)
            attach("THIS IS TEST COMMENT", name="Name of attach", attachment_type=attachment_type.TEXT)
            return CatalogPage(self.webdriver, logger=self.logger)
        except:
            self.logger.error(f"Navigating to woman parfums catalog with ParfumsMenuTopic.PARFUMERIA.value, ParfumsMenuItems.JINOCHA_PARF.value using self.__navigate_to_menu_item() is unsuccessfull")
            raise TimeoutError(TimeoutError)