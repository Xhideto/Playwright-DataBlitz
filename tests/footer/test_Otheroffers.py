from playwright.sync_api import Page, expect
import re

class TestDatablitzFooter:
    def test_other_offers_footer(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/")

        footer = page.locator('#shopify-section-footer')

        footer.scroll_into_view_if_needed()
        page.wait_for_timeout(500)
        expect (footer).to_be_visible()
        print(f"footer is visible")

        expect (footer.get_by_role('button', name="Other Offers")).to_be_visible()
        expect (footer.get_by_role('button', name="Other Offers")).to_be_disabled()
        page.wait_for_timeout(500)
        print(f"Other offers is visible and disabled")

        offers = page.locator('#block-56673434-cce7-4c62-8291-d4af2c7c7f4a .footer__linklist li').count()

        for i in range(offers):
            page.locator('#shopify-section-footer').scroll_into_view_if_needed()
            page.wait_for_timeout(500)
            expect (page.locator('#shopify-section-footer')).to_be_visible()

            offer = page.locator('#block-56673434-cce7-4c62-8291-d4af2c7c7f4a .footer__linklist li').nth(i)

            link = offer.locator('.footer__link-item')

            text = offer.inner_text()
            expect (offer).to_be_visible()

            target = link.get_attribute('target')

            if target == "_blank":
                with page.expect_popup() as digital_store:
                    link.click()

                    new_page = digital_store.value
                    new_page.wait_for_load_state()

                    expect (new_page).to_have_url(re.compile(r"https://digital.datablitz.com.ph/"))
                    print(f"'{new_page.url}' is working")
                    new_page.close()

            else:

                link.click()

                url = page.url

                if "/collections/" in url:
                    print(f"'{text}' tested")
                elif "/pages/" in url:
                    print(f"'{text}' tested")
                else:
                    print(f"Invalid URL")

                page.go_back()