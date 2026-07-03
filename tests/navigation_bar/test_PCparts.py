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

    def test_pc_parts_recommend(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/")

        pc_parts = page.locator('.tmenu_navbar')

        pc_parts.get_by_role('link', name="PC/ Mac").hover()
        page.wait_for_timeout(500)
        expect (page.locator('.tmenu_submenu_type_tab')).to_be_visible()

        expect (pc_parts.get_by_role('tab', name="PC Parts & Components")).to_be_visible()

        expect (page.get_by_text("PC Parts & Components We Recommend")).to_be_visible()
        print(f"The text is seen")

        recommend_parts = page.locator('.tmenu_submenu_tab_active .tmenu_item_layout_image').count()

        for i in range(recommend_parts):
            page.get_by_role('link', name="PC/ Mac").hover()
            page.wait_for_timeout(500)

            page.get_by_role('tab', name="PC Parts & Components").hover()
            page.wait_for_timeout(500)

            parts_comps = page.locator('.tmenu_submenu_tab_active .tmenu_item_layout_image').nth(i)
            expect (parts_comps.locator('.tmenu_image')).to_be_visible()

            parts_comps.locator('.tmenu_item_link').click()

            expect (page).to_have_url(re.compile(r"/products/"))

            page.wait_for_timeout(1000)

            page.go_back()
            page.wait_for_timeout(500)
            print(f"PC/Mac recommended PC Parts & Components {i+1} tested")