from playwright.sync_api import Page, expect
import re

class TestDatablitzPS5Product:
    def test_product_gallery(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/products/ps5-assassins-creed-black-flag-resynced")

        image = page.locator('.card__section')

        scroller = image.locator('.product-gallery__thumbnail-list a').count()
        print(f"Found {scroller} thumbnails")

        for i in range(scroller):
            thumbnail = image.locator('.product-gallery__thumbnail-list a').nth(i)

            expect (thumbnail).to_be_visible()

            thumbnail.click()
            page.wait_for_timeout(500)

            expect (thumbnail).to_have_class(re.compile(r"is-nav-selected"))
            print(f"Scroller thumbnail {i+1} tested")


