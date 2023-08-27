from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators.catalog_item import CatalogItem

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 20)
driver.get(url="https://parfums.ua/ua/category/lady")


first_element = wait.until(EC.element_to_be_clickable((By.XPATH, str(CatalogItem.get_element_by_title_xpath("Versace Bright Crystal")))))
second_element = first_element.find_element(By.XPATH, ".//ancestor::div[@class='info-product-wrapper']//span[text() and @class='price_item']")
print(type(first_element), type(second_element))


# другий теж буде обʼєктом webdriverwait? тобто його можна юзати далі в коді, і на нього теж буде працювати очікування 20 сек?