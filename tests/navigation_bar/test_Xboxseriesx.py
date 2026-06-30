from playwright.sync_api import Page, expect
import re

class TestNavBarXboxSeriesX:
    def test_xbox_x_sub_menu(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/")

        xbox_x = page.locator('.tmenu_navbar')

        xbox_x.get_by_title('XBOX').hover()
        page.wait_for_timeout(500)
        expect (page.locator('.tmenu_submenu_type_tab')).to_be_visible()

        expect (xbox_x.get_by_role('tab', name="Xbox Series X")).to_be_visible()

        xbox_x.get_by_role('tab', name="Xbox Series X").click()
        expect (page).to_have_url("https://ecommerce.datablitz.com.ph/collections/xbox-series-x")
        page.wait_for_timeout(1500)
        page.go_back()
        print(f"Xbox Series X submenu is visible")