from playwright.sync_api import Page, expect
import re

class TestDatablitzFooter:
    def test_social_media_footer(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/")

        footer = page.locator('#shopify-section-footer')

        footer.scroll_into_view_if_needed()
        page.wait_for_timeout(500)
        expect (footer).to_be_visible()
        print(f"footer is visible")

        expect (footer.get_by_role('button', name="Follow Us")).to_be_visible()
        expect (footer.get_by_role('button', name="Follow Us")).to_be_disabled()
        page.wait_for_timeout(500)
        print(f"Follow Us is visible and disabled")

        with page.expect_popup() as social_media:
            footer.get_by_role("link", name='Facebook', exact=True).click()

        new_tab = social_media.value
        new_tab.wait_for_load_state()

        expect (new_tab).to_have_url(re.compile(r"facebook.com", re.IGNORECASE))
        page.wait_for_timeout(1000)
        print(f"'{new_tab.url}' is working")
        new_tab.close()

        with page.expect_popup() as social_media:
            footer.get_by_role("link", name='Twitter', exact=True).click()

        new_tab = social_media.value
        new_tab.wait_for_load_state()

        expect (new_tab).to_have_url(re.compile(r"x.com", re.IGNORECASE))
        page.wait_for_timeout(1000)
        print(f"'{new_tab.url}' is working")
        new_tab.close()

        with page.expect_popup() as social_media:
            footer.get_by_role("link", name='Instagram', exact=True).click()

        new_tab = social_media.value
        new_tab.wait_for_load_state()

        expect (new_tab).to_have_url(re.compile(r"instagram.com", re.IGNORECASE))
        page.wait_for_timeout(1000)
        print(f"'{new_tab.url}' is working")
        new_tab.close()

        print(f"All Datablitz social media are working")