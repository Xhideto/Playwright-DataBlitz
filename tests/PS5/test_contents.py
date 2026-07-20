from playwright.sync_api import Page, expect
import re

class TestDatablitzFooter:
    def test_ps5_banner_image(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/collections/playstation-5")

        collection = page.locator('.collection')

        expect (collection.locator('.collection__image')).to_be_visible()
        banner = collection.locator('.collection__image')
        assert banner, "No image found"
        print(f"PS5 banner is visible")