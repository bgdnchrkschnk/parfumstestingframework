from time import sleep

class TestMenuItemsAccessability:
    def test_menu_item_accessability(self, browser):
        browser\
            .get("https://parfums.ua/ua")
        browser.go_to_women_parfums()
