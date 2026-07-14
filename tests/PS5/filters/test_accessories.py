from playwright.sync_api import Page, expect
import re

class TestDatablitzFilters:
    def test_accessories(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/collections/playstation-5")

        filters = page.locator('.card')
        accessories = filters.get_by_role('button', name="Accessories")

        expect (accessories).to_be_visible()
        print(f"'Accessories' is visible")

        accessories.click()
        page.wait_for_timeout(300)
        accessories.click()
        page.wait_for_timeout(300)
        print(f"Accessories option is working")