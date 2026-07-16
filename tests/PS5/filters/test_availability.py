from playwright.sync_api import Page, expect
import re

class TestDatablitzFilters:
    def test_availability(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/collections/playstation-5")

        filters = page.locator('.card')
        availability = filters.get_by_role('button', name="Availability")

        expect (availability).to_be_visible()
        print(f"'Availability' is visible")

        availability.click()
        page.wait_for_timeout(300)
        availability.click()
        page.wait_for_timeout(300)
        print(f"Availability option is working")