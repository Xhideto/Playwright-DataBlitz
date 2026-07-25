from playwright.sync_api import Page, expect
import re

class TestDatablitzPS5Product:
    def test_product_title(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/products/ps5-assassins-creed-black-flag-resynced")

        card = page.locator('.card__section')

        expect (card.locator('.product-meta__title')).to_be_visible()
        print(f"PS5 Assassins Creed Black Flag Resynced (Asian) is Visible")

    def test_product_reviews(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/products/ps5-assassins-creed-black-flag-resynced")
        page.wait_for_timeout(500)

        card = page.locator('.card__section')

        expect (card.locator('.gw-rv-rating-stars').nth(1)).to_be_visible()
        print(f"Review stars are visible")

        review_text = card.locator('.gw-text.gw-text--heading-sm').inner_text()
        print(f"Review count text: '{review_text}'")

        assert "Reviews" in review_text, "No Review text found"
        print(f"Review count text is verified and visible")

        expect (card.locator('.gw-rv-star-rating-summary')).to_be_visible()

        card.locator('.gw-rv-star-rating-summary').hover()
        page.wait_for_timeout(500)
        expect (page.locator('.gw-tooltip__wrapper')).to_be_visible()
        print(f"Review ratings is visible")