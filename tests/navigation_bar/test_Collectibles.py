from playwright.sync_api import Page, expect
import re

class TestNavBarCollectibles:
    def test_collectibles_sub_menu(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/")

        collect = page.locator('.tmenu_navbar')

        collect.get_by_role('link', name="Collectibles").hover()
        page.wait_for_timeout(500)
        expect (page.locator('.tmenu_submenu_type_mega')).to_be_visible()

        collect.get_by_role('link', name="Collectibles", exact=True).click()
        expect (page).to_have_url("https://ecommerce.datablitz.com.ph/collections/collectibles")
        page.wait_for_timeout(1000)

        page.go_back
        print(f"Collectibles page is working")