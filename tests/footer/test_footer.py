from playwright.sync_api import Page, expect
import re

class TestDatablitzFooter:

    def test_gaming_footer(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/")

        footer = page.locator('#shopify-section-footer')

        footer.scroll_into_view_if_needed()
        page.wait_for_timeout(500)
        expect (footer).to_be_visible()
        print(f"footer is visible")

        expect (footer.get_by_role('button', name="Gaming")).to_be_visible()
        expect (footer.get_by_role('button', name="Gaming")).to_be_disabled()
        page.wait_for_timeout(500)
        print(f"Gaming is visible and disabled")

        gaming_links = page.locator('#block-1596597245070 .footer__linklist li').count()

        for i in range(gaming_links):
            page.locator('#shopify-section-footer').scroll_into_view_if_needed()
            page.wait_for_timeout(500)
            expect (page.locator('#shopify-section-footer')).to_be_visible()

            gaming = page.locator('#block-1596597245070 .footer__linklist li').nth(i)

            text = gaming.locator('.footer__link-item').first.inner_text()
            expect (gaming.locator('.footer__link-item')).to_be_visible()

            gaming.locator('.footer__link-item').click()

            expect (page).to_have_url(re.compile(r"/collections/"))
            page.wait_for_timeout(500)
            page.go_back()
            print(f"Footer '{text}' tested")
            