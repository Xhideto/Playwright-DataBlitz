from playwright.sync_api import Page, expect
import re

class TestDatablitzFilters:
    def test_filters_title(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/collections/playstation-5")

        filters = page.locator('.card')

        expect (filters.locator('.card__title--small')).to_be_visible()
        page.wait_for_timeout(500)
        print(f"'Filters' title is visible")