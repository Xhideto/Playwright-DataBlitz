from playwright.sync_api import Page, expect
import re

class TestNavBarPcOthers:
    def test_pc_others_sub_menu(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/")

        pc_others = page.locator('.tmenu_navbar')

        pc_others.get_by_role('link', name="PC/ Mac").hover()
        page.wait_for_timeout(500)
        expect (page.locator('.tmenu_submenu_type_tab')).to_be_visible()

        expect (pc_others.get_by_role('tab', name="Others")).to_be_visible()

        pc_others.get_by_role('tab', name="Others").click()
        expect (page).to_have_url("https://ecommerce.datablitz.com.ph/collections/others")
        page.wait_for_timeout(1000)
        page.go_back()
        print(f"PC Others sub menu is visible")