from playwright.sync_api import Page, expect
import re

class TestDatablitzFilters:
    def test_genre(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/collections/playstation-5")

        filters = page.locator('.card')
        genres = filters.get_by_role('button', name="Genre")

        expect (genres).to_be_visible()
        print(f"'Genres' is visible")

        genres.click()
        page.wait_for_timeout(300)
        genres.click()
        page.wait_for_timeout(300)
        print(f"Genres option is working")