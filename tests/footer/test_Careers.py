from playwright.sync_api import Page, expect
import re

class TestDatablitzFooter:
    def test_careers_footer(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/")

        footer = page.locator('#shopify-section-footer')

        footer.scroll_into_view_if_needed()
        page.wait_for_timeout(500)
        expect (footer).to_be_visible()
        print(f"footer is visible")

        expect (footer.get_by_role('button', name="Explore")).to_be_visible()
        expect (footer.get_by_role('button', name="Explore")).to_be_disabled()
        page.wait_for_timeout(500)
        print(f"Explore is visible and disabled")

        text = footer.locator('#block-6b978821-65ed-49a5-9305-d4ad46b66192 .footer__link-item').inner_text()

        expect (footer.locator('#block-6b978821-65ed-49a5-9305-d4ad46b66192 .footer__link-item')).to_be_visible()
        footer.locator('#block-6b978821-65ed-49a5-9305-d4ad46b66192 .footer__link-item').click()

        expect (page).to_have_url("https://ecommerce.datablitz.com.ph/pages/careers")
        page.wait_for_timeout(1000)
        page.go_back()

        print(f"Footer '{text}' tested")