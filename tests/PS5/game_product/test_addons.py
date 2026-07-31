from playwright.sync_api import Page, expect
import re

class TestDatablitzPS5Product:
    def test_product_addon_title(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/products/ps5-assassins-creed-black-flag-resynced")

        frequently_bought = page.locator('.cbb-frequently-bought-container')

        title = (frequently_bought.locator('.cbb-frequently-bought-title'))
        title_text = title.inner_text()

        expect (title).to_be_visible()
        print(f"{title_text}")

    def test_product_addon_image(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/products/ps5-assassins-creed-black-flag-resynced")

        frequently_bought = page.locator('.cbb-frequently-bought-container')

        expect (frequently_bought.locator('.cbb-frequently-bought-products')).to_be_visible()
        print(f"Frequently brought products tested")

    def test_product_addon_total_price(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/products/ps5-assassins-creed-black-flag-resynced")
        
        frequently_bought = page.locator('.cbb-frequently-bought-container')

        expect (frequently_bought.locator('.cbb-frequently-bought-total-price-text')).to_be_visible()

        price = frequently_bought.locator('.cbb-frequently-bought-total-price-regular-price')
        price_text = price.inner_text()

        expect (price).to_be_visible()
        print(f"Total price expected: {price_text}")