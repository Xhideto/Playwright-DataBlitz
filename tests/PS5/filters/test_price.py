from playwright.sync_api import Page, expect
import re

class TestDatablitzFilters:
    def test_price(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/collections/playstation-5")

        filters = page.locator('.card')
        price = filters.get_by_role('button', name="Price")

        expect (price).to_be_visible()
        print(f"'Price' is visible")

        price.click()
        page.wait_for_timeout(300)
        price.click()
        page.wait_for_timeout(300)
        print(f"Price option is working")