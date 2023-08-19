
class CatalogItem:

    def get_element_by_title_xpath(title:str):
        return f"//li[@data-id]//a[contains(@data-default-name, '{title}')]"

    def get_element_price_by_title_xpath():
        return ".//ancestor::div[@class='info-product-wrapper']//span[text() and @class='price_item']"
