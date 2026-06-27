from playwright.sync_api import Page, expect
import re

class TestNavBarSwitch:
    def test_switch_two_sub_menu(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/")

        switch_two = page.locator('.tmenu_navbar')

        switch_two.get_by_role('link', name="SWITCH").hover()
        page.wait_for_timeout(500)
        expect (page.locator('.tmenu_submenu_type_tab')).to_be_visible()

        expect (switch_two.get_by_role('link', name="SWITCH 2", exact=True)).to_be_visible()

        switch_two.get_by_role('link', name="SWITCH 2", exact=True).click()
        expect (page).to_have_url("https://ecommerce.datablitz.com.ph/collections/nintendo-switch-2")
        page.go_back()
        print(f"Switch 2 submenu is seen")