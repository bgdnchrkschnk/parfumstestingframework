from allure import title, description, suite, severity, severity_level, feature, story, epic



@suite("Catalog_page tests")
class TestAssessebilityToMenu:
    @title("Verify woman parfum page is available")
    @description("The description of test")
    @severity(severity_level.CRITICAL)
    @feature("Module catalog-page")
    @story("Navigating to catalog")
    @epic("COOR-132")
    def test_catalog_item(self, browser):
        browser.go_to_women_parfums()
        actual = browser.get_price(title="Versace Bright Crystal")
        text = browser.find_item_by_title("Versace Bright Crystal").text
        expected = "1586"
        assert actual == expected and "Versace Bright Crystal" in text, "Price is wrong"

