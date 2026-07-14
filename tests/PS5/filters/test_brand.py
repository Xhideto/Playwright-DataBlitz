from playwright.sync_api import Page, expect
import re

class TestDatablitzFilters:
    def test_brand(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/collections/playstation-5")

        filters = page.locator('.card')
        brand = filters.get_by_role('button', name="Brand")

        expect (brand).to_be_visible()
        print(f"'Brand' is visible")

        brand.click()
        page.wait_for_timeout(300)
        brand.click()
        page.wait_for_timeout(300)
        print(f"Brand option is working")