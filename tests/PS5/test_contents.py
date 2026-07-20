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
    
    def test_ps5_header(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/collections/playstation-5")

        header = page.locator('.card__header')
        
        expect (header.locator('.collection__title')).to_be_visible()
        print(f"PS5 header title is visible")

        product_count = header.locator('.boost-pfs-filter-total-product').inner_text()
        print(f"Product count: {product_count}")

    def test_ps5_sort_by_tool(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/collections/playstation-5")

        sort = page.locator('.collection__toolbar')

        expect (sort.locator('.value-picker-button')).to_be_visible()
        print(f"Sort by tool is visible")

        sort.locator('.value-picker-button').click()
        expect(page.locator('.value-picker')).to_be_visible()
        print(f"Sort selectors are visible")

        selectors = page.locator('.value-picker__choice-list button').count()
        print(f"{selectors}")

        for i in range(selectors):
            page.locator('.collection__toolbar').locator('.value-picker-button').click()

            sort_by = page.locator('.value-picker__choice-list button').nth(i)

            text = sort_by.inner_text()
            expect (sort_by).to_be_visible()

            sort_by.click()
            page.wait_for_timeout(500)
            expect (page).to_have_url(re.compile(r"/collections/"))

            print(f"Sort by: {text}")

    def test_ps5_product_views(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/collections/playstation-5")

        view = page.locator('.collection__toolbar')

        expect(view.locator('.collection__layout-label')).to_be_visible()
        print(f"View is visible")

        view.locator('button[aria-label="Display products as list"]').click()
        page.wait_for_timeout(500)
        print("Products are in list")

        view.locator('button[aria-label="Display products as grid"]').click()
        page.wait_for_timeout(500)
        print(f"Products are once again in grid")