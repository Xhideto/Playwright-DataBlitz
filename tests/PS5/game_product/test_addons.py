from playwright.sync_api import Page, expect
import re

class TestDatablitzPS5Product:
    def test_product_addon_title(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/products/ps5-assassins-creed-black-flag-resynced")

        frequently_bought = page.locator('.cbb-frequently-bought-container')

        title = (frequently_bought.locator('.cbb-frequently-bought-title'))
        title_text = (title).inner_text()

        expect (title).to_be_visible()
        print(f"{title_text}")