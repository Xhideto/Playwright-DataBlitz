from playwright.sync_api import Page, expect
import re

class TestDatablitzFilters:
    def test_price(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/collections/playstation-5")

        filters = page.locator('.card')
        price = filters.get_by_role('button', name="Price")

        expect (price).to_be_visible()
        print(f"'Price' is visible")

        price.click()
        page.wait_for_timeout(300)
        price.click()
        page.wait_for_timeout(300)
        print(f"Price option is working")

    def test_min_price_input_box(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/collections/playstation-5")

        filters = page.locator('.card')
        price_box = filters.locator('.boost-pfs-filter-option-range-amount')

        price_box.get_by_label('Min Price').fill('1000')
        expect (price_box.get_by_label('Min Price')).to_have_value('1000')
        page.keyboard.press('Enter')

        expect (page).to_have_url(re.compile(r"/collections/"))
        page.wait_for_timeout(500)
        print(f"1000 price range is entered")

        page.locator('.boost-pfs-filter-clear').first.click()
        page.wait_for_timeout(500)
        print(f"Price is now clear")

    def test_max_price_input_box(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/collections/playstation-5")

        filters = page.locator('.card')
        price_box = filters.locator('.boost-pfs-filter-option-range-amount')

        price_box.get_by_label('Max Price').fill('5000')
        expect (price_box.get_by_label('Max Price')).to_have_value('5000')
        page.keyboard.press('Enter')

        expect (page).to_have_url(re.compile(r"/collections/"))
        page.wait_for_timeout(500)
        print(f"5000 price range is entered")

        page.locator('.boost-pfs-filter-clear').first.click()
        page.wait_for_timeout(500)
        print(f"Price is now clear")
