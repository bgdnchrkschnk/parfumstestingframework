import pytest
from allure import step


def test_catalog_item(browser):
    # browser.go_home_page()
    browser.go_to_women_parfums()
    actual = browser.get_price(title="Versace Bright Crystal")
    text = browser.find_item_by_title("Versace Bright Crystal").text
    expected = "1586"
    assert actual == expected and "Versace Bright Crystal" in text, "Price is wrong"

