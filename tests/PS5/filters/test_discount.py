from playwright.sync_api import Page, expect
import re

class TestDatablitzFilters:
    def test_discount_rate(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/collections/playstation-5")

        filters = page.locator('.card')
        rate = filters.get_by_role('button', name="Discount Rate")

        expect (rate).to_be_visible()
        print(f"'Discount Rate' is visible")

        rate.click()
        page.wait_for_timeout(300)
        rate.click()
        page.wait_for_timeout(300)
        print(f"Discount Rate option is working")