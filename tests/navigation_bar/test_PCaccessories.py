from playwright.sync_api import Page, expect
import re

class TestNavBarPcAccessories:
    def test_pc_accessories_sub_menu(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/")

        pc_perip = page.locator('.tmenu_navbar')

        pc_perip.get_by_role('link', name="PC/ Mac").hover()
        page.wait_for_timeout(500)
        expect (page.locator('.tmenu_submenu_type_tab')).to_be_visible()

        pc_perip.get_by_role('link', name="PC/ Mac", exact=True).click()
        expect (page).to_have_url("https://ecommerce.datablitz.com.ph/collections/pc-mac")
        page.wait_for_timeout(1000)
        page.go_back()
        print(f"PC/ Mac sub menu is visible")

        # pc_perip.get_by_role('link', name="PC/ Mac").hover()
        # page.wait_for_timeout(500)
        # expect (page.locator('.tmenu_submenu_type_tab')).to_be_visible()

        expect (pc_perip.get_by_role('tab', name="Peripherals & Accessories")).to_be_visible()

        pc_perip.get_by_role('tab', name="Peripherals & Accessories").click()
        expect (page).to_have_url("https://ecommerce.datablitz.com.ph/collections/pc-mac")
        page.wait_for_timeout(1000)
        page.go_back()
        print(f"Peripherals & Accessories sub menu is visible")