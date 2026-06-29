from playwright.sync_api import Page, expect
import re

class TestNavBarSwitch:
    def test_switch_sub_menu(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/")

        switch = page.locator('.tmenu_navbar')

        switch.get_by_title('SWITCH').hover()
        page.wait_for_timeout(500)
        expect (page.locator('.tmenu_submenu_type_tab')).to_be_visible()

        expect (switch.get_by_role('tab', name="Switch", exact=True)).to_be_visible()

        switch.get_by_role('tab', name="Switch", exact=True).click()
        expect (page).to_have_url("https://ecommerce.datablitz.com.ph/collections/nintendo-switch")
        page.wait_for_timeout(1500)
        page.go_back()
        print(f"Switch submenu is seen")