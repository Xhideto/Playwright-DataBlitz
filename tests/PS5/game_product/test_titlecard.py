from playwright.sync_api import Page, expect
import re

class TestDatablitzPS5Product:
    def test_product_title(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/products/ps5-assassins-creed-black-flag-resynced")
        card = page.locator('.card__section')

        expect (card.locator('.product-meta__title')).to_be_visible()
        print(f"PS5 Assassins Creed Black Flag Resynced (Asian) is Visible")