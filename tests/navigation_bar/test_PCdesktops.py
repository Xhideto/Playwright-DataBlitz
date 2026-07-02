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

    def test_pc_desktops_recommend(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/")

        pc_laps = page.locator('.tmenu_navbar')

        pc_laps.get_by_role('link', name="PC/ Mac").hover()
        page.wait_for_timeout(500)
        expect (page.locator('.tmenu_submenu_type_tab')).to_be_visible()

        expect (pc_laps.get_by_role('tab', name="Laptops & Desktops")).to_be_visible()

        expect (page.get_by_text("Laptops & Desktops We Recommend")).to_be_visible()
        print(f"The text is seen")

        recommend_laps = page.locator('.tmenu_submenu_tab_active .tmenu_item_layout_image').count()

        for i in range(recommend_laps):
            page.get_by_role('link', name="PC/ Mac").hover()
            page.wait_for_timeout(500)

            page.get_by_role('tab', name="Laptops & Desktops").hover()
            page.wait_for_timeout(500)

            peripherals_desks = page.locator('.tmenu_submenu_tab_active .tmenu_item_layout_image').nth(i)
            expect (peripherals_desks.locator('.tmenu_image')).to_be_visible()

            peripherals_desks.locator('.tmenu_item_link').click()

            url = page.url

            if "/products/" in url:
                print(f"Recommend {url} product {i+1} tested")
            elif "/collections/" in url:
                print(f"Recommend {url} collection {i+1} tested")
            else:
                print(f"No url found")

            page.wait_for_timeout(1000)

            page.go_back()
            page.wait_for_timeout(500)
            print(f"PC/Mac recommended Laptops & Desktops {i+1} tested")