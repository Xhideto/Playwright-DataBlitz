from playwright.sync_api import Page, expect
import re

class TestDatablitzFilters:
    def test_filters_title(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/collections/playstation-5")

        filters = page.locator('.card')

        expect (filters.locator('.card__title--small')).to_be_visible()
        page.wait_for_timeout(500)
        print(f"'Filters' title is visible")

    def test_categories_option(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/collections/playstation-5")

        filters = page.locator('.card')
        categories = filters.get_by_role('button', name="Categories")

        expect (categories).to_be_visible()
        print(f"'Categories' is visible")

        categories.click()
        page.wait_for_timeout(300)
        categories.click()
        page.wait_for_timeout(300)
        print(f"Categories option is working")