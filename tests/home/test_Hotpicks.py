from playwright.sync_api import Page, expect
import re

class TestDatablitzHotPicks:

    def test_hot_picks_text(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/")

        expect (page.get_by_role("heading", name="Hot Picks")).to_be_visible()

    def test_hot_picks_list(self, page: Page):
         page.goto("https://ecommerce.datablitz.com.ph/")

         hot_picks = page.locator("#shopify-section-1584623859185 .collection-item").count()

         for i in range(hot_picks):
               list = page.locator("#shopify-section-1584623859185 .collection-item").nth(i)
               expect (list.locator('.collection-item__image-wrapper ')).to_be_visible()
               list.hover()
               page.wait_for_timeout(500)
               list.click()
               expect (page).to_have_url(re.compile(r"/collections/"))
               page.go_back()
               print(f"Hot picks product {i+1} tested")

    def test_hot_picks_buttons(self, page: Page):
            page.goto("https://ecommerce.datablitz.com.ph/")

            next_button = page.locator("#shopify-section-1584623859185").get_by_role("button", name="Next")
            expect(next_button).to_be_visible()
            next_button.click()

            previous_button = page.locator("#shopify-section-1584623859185").get_by_role("button", name="Previous")
            expect(previous_button).to_be_visible()
            previous_button.click()