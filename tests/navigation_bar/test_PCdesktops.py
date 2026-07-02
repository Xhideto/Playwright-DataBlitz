from playwright.sync_api import Page, expect
import re

class TestNavBarPcDesktops:
    def test_pc_desktops_sub_menu(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/")

        pc_laps = page.locator('.tmenu_navbar')

        pc_laps.get_by_role('link', name="PC/ Mac").hover()
        page.wait_for_timeout(500)
        expect (page.locator('.tmenu_submenu_type_tab')).to_be_visible()

        expect (pc_laps.get_by_role('tab', name="Laptops & Desktops")).to_be_visible()

        pc_laps.get_by_role('tab', name="Laptops & Desktops").click()
        expect (page).to_have_url("https://ecommerce.datablitz.com.ph/collections/laptops-desktops")
        page.wait_for_timeout(1000)
        page.go_back()
        print(f"Laptops & Desktops sub menu is visible")