from playwright.sync_api import Page, expect
import re

class TestDatablitzPS5:
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
    
    def test_ps5_products(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/collections/playstation-5")

        product = page.locator('.boost-pfs-filter-products .product-item').all()

        LIMIT = 24

        for i, product_img in enumerate(product[:LIMIT]):
            expect (product_img.locator('.product-item__image-wrapper')).to_be_visible()
            product_img.hover()
            page.wait_for_timeout(500)
            expect (product_img.locator('.product-item__image-wrapper--with-secondary')).to_have_count(1)

            product_img.locator('.product-item__image-wrapper').click()
            expect (page).to_have_url(re.compile(r"/collections/"))
            page.wait_for_timeout(500)
            page.go_back()
            print(f"PS5 product {i+1} tested")

            if product_img.locator('.product-label').count() > 0:
                expect (product_img.locator('.product-label')).to_be_visible()
                expect (product_img.locator('.price--highlight')).to_be_visible()
                expect (product_img.locator('.price--compare')).to_be_visible()
                print(f"This product {i+1} has a label on it")
            else:
                expect (product_img.locator('.price')).to_be_visible()
                print(f"Product {i+1} has a standard price")

            product_title = product_img.locator('.product-item__title')
            
            product_txt = product_title.inner_text()
            expect (product_title).to_be_visible()

            product_title.click()
            expect (page).to_have_url(re.compile(r"/collections/"))
            page.wait_for_timeout(500)
            page.go_back()
            print(f"PS5 {product_txt}")

    def test_ps5_product_buttons(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/collections/playstation-5")

        product = page.locator('.boost-pfs-filter-products .product-item').all()

        LIMIT = 24

        for i, product_button in enumerate(product[:LIMIT]):
            add_to_cart = product_button.locator('button[type="submit"]')
            expect (add_to_cart).to_be_visible()
            expect (add_to_cart).to_be_enabled()
            print (f"Add to cart {i+1} been tested")
                
