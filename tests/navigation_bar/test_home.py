from playwright.sync_api import Page, expect
import re

class TestNavBarHome:

    def test_nav_bar(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/")

        home = page.locator('.tmenu_navbar')

        expect (home.get_by_role('link', name="Home")).to_be_visible()
        home.get_by_role('link', name="Home").click()
        expect (page).to_have_url("https://ecommerce.datablitz.com.ph/")
        print(f"it works")