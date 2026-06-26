from playwright.sync_api import Page, expect
import re

class TestNavBarPS4:

    def test_playstation_four_sub_menu(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/")

        psfour = page.locator('.tmenu_navbar')

        psfour.get_by_role('link', name="PS4").hover()
        page.wait_for_timeout(500)
        expect (page.locator('.tmenu_submenu_type_mega')).to_be_visible()
        psfour.get_by_role('link', name="PS4", exact=True).click()
        expect (page).to_have_url("https://ecommerce.datablitz.com.ph/collections/playstation-4")
        page.wait_for_timeout(1000)
        page.go_back()
        print(f"PS4 submenu is seen")