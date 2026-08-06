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

    def test_product_addon_addtocart_button(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/products/ps5-assassins-creed-black-flag-resynced")
        
        frequently_bought = page.locator('.cbb-frequently-bought-container')

        add_to_cart = frequently_bought.locator('.cbb-frequently-bought-add-button')
        expect (add_to_cart).to_be_visible()
        expect (add_to_cart).to_be_enabled()
        print(f"Add to card button is working")

    def test_product_addon_checkbox(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/products/ps5-assassins-creed-black-flag-resynced")
                
        frequently_bought = page.locator('.cbb-frequently-bought-container')

        checkboxes = frequently_bought.locator('input[type="checkbox"]').all()
        assert len(checkboxes) > 0, "No checkboxes found"

        for i, checkbox in enumerate(checkboxes):
            expect(checkbox).to_be_visible()
            checked = checkbox.is_checked()
            print(f"Checkbox {i+1}  checked: {checked}")

            checkbox.uncheck()
            page.wait_for_timeout(300)
            assert not checkbox.is_checked(), "Checkbox didn't uncheck"
            checkbox.check()
            page.wait_for_timeout(300)
            assert checkbox.is_checked(), "Checkbox didn't check"
        print(f"All of the checkboxes work")
