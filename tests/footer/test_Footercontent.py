from playwright.sync_api import Page, expect
import re

class TestDatablitzFooter:
    def test_footer_content(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/")

        footer = page.locator("#shopify-section-footer")

        footer.scroll_into_view_if_needed()
        page.wait_for_timeout(500)
        expect (footer).to_be_visible()
        print(f"Footer is visible")

        expect (footer.locator(".footer__block-list")).to_be_visible()
        print(f"Footer contents are visible")

        expect (footer.locator('img[src*="DataBlitz-Brandnew.jpg"]')).to_be_visible()
        image_badge = footer.locator('img[src*="DataBlitz-Brandnew.jpg"]').evaluate("el => el.naturalWidth > 0")
        assert image_badge, "Image is not visible"
        print(f"Datablitz image badge is visible")

        expect (footer.locator('.hidden-pocket')).to_be_visible()
        print(f"Datablitz all rights reserved is visible")