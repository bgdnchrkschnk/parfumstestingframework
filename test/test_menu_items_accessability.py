from time import sleep


class TestMenuItemsAccessability:
    def test_menu_item_accessability(self, home_page):
        home_page.go_to_women_parfums()
        sleep(5)
