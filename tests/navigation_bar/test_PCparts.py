from playwright.sync_api import Page, expect
import re

class TestNavBarPcParts:
    def test_pc_parts_sub_menu(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/")

        pc_parts = page.locator('.tmenu_navbar')

        pc_parts.get_by_role('link', name="PC/ Mac").hover()
        page.wait_for_timeout(500)
        expect (page.locator('.tmenu_submenu_type_tab')).to_be_visible()

        expect (pc_parts.get_by_role('tab', name="PC Parts & Components")).to_be_visible()

        pc_parts.get_by_role('tab', name="PC Parts & Components").click()
        expect (page).to_have_url("https://ecommerce.datablitz.com.ph/collections/pc-parts-and-components")
        page.wait_for_timeout(1000)
        page.go_back()
        print(f"PC Parts & Components sub menu is visible")