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

    def test_pc_accessories_recommend(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/")

        pc_perip = page.locator('.tmenu_navbar')

        pc_perip.get_by_role('link', name="PC/ Mac").hover()
        page.wait_for_timeout(500)
        expect (page.locator('.tmenu_submenu_type_tab')).to_be_visible()

        expect (pc_perip.get_by_role('tab', name="Peripherals & Accessories")).to_be_visible()

        expect (page.get_by_text("Peripherals & Accessories We Recommend")).to_be_visible()
        print(f"The text is seen")

        recommend_perip = page.locator('.tmenu_submenu_tab_active .tmenu_item_layout_image').count()

        for i in range(recommend_perip):
            page.get_by_role('link', name="PC/ Mac").hover()
            page.wait_for_timeout(500)

            page.get_by_role('tab', name="Peripherals & Accessories").hover()
            page.wait_for_timeout(500)

            peripherals_access = page.locator('.tmenu_submenu_tab_active .tmenu_item_layout_image').nth(i)
            expect (peripherals_access.locator('.tmenu_image')).to_be_visible()

            peripherals_access.locator('.tmenu_item_link').click()
            expect (page).to_have_url(re.compile(r"/products/"))

            page.wait_for_timeout(1000)

            page.go_back()
            page.wait_for_timeout(500)
            print(f"PC/Mac recommended peripherals {i+1} tested")

    def test_pc_accessories_categories(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/")

        pc_perip = page.locator('.tmenu_navbar')

        pc_perip.get_by_role('link', name="PC/ Mac").hover()
        page.wait_for_timeout(500)
        expect (page.locator('.tmenu_submenu_type_tab')).to_be_visible()

        expect (pc_perip.get_by_role('tab', name="Peripherals & Accessories")).to_be_visible()
        pc_perip.get_by_role('tab', name="Peripherals & Accessories").hover()

        expect (pc_perip.locator('.tmenu_submenu_tab_active').get_by_role('link', name="Categories")).to_be_visible()
        pc_perip.locator('.tmenu_submenu_tab_active').get_by_role('link', name="Categories").click()
        expect (page).to_have_url("https://ecommerce.datablitz.com.ph/collections/nintendo-switch-2-games-1") #When clicked idk why it directs to this link

        page.wait_for_timeout(1000)
        page.go_back()

        print(f"Categories is working")

        page.locator('.tmenu_navbar').get_by_role('link', name="PC/ Mac").hover()
        page.wait_for_timeout(500)

        categories1 = page.locator('.tmenu_submenu_tab_active .tmenu_item_level_1.tmenu_col-4:has(a[title="Categories"]) .tmenu_item_level_2').count()
        categories2 = page.locator('.tmenu_submenu_tab_active .tmenu_item_level_1.tmenu_col-4:has(a[title="Categories"]) + .tmenu_item_level_1.tmenu_col-4 .tmenu_item_level_2').count()
        categories3 = page.locator('.tmenu_submenu_tab_active .tmenu_item_level_1.tmenu_col-4:has(a[title="Categories"]) + .tmenu_item_level_1.tmenu_col-4 + .tmenu_item_level_1.tmenu_col-4 .tmenu_item_level_2').count()

        for i in range(categories1):
            page.get_by_role('link', name="PC/ Mac").hover()
            page.wait_for_timeout(500)

            page.get_by_role('tab', name="Peripherals & Accessories").hover()
            page.wait_for_timeout(500)

            link = page.locator('.tmenu_submenu_tab_active .tmenu_item_level_1.tmenu_col-4:has(a[title="Categories"]) .tmenu_item_level_2').nth(i)

            text = link.locator('.tmenu_item_text').inner_text()
            expect (link.locator('.tmenu_item_text')).to_be_visible()

            link.locator('.tmenu_item_link').evaluate("el => el.click()")

            expect (page).to_have_url(re.compile(r"/collections/"))
            page.wait_for_timeout(500)
            page.go_back()
            print(f"Categories '{text}' tested")

        for i in range(categories2):
            page.get_by_role('link', name="PC/ Mac").hover()
            page.wait_for_timeout(500)

            page.get_by_role('tab', name="Peripherals & Accessories").hover()
            page.wait_for_timeout(500)

            link = page.locator('.tmenu_submenu_tab_active .tmenu_item_level_1.tmenu_col-4:has(a[title="Categories"]) + .tmenu_item_level_1.tmenu_col-4 .tmenu_item_level_2').nth(i)

            text = link.locator('.tmenu_item_text').inner_text()
            expect (link.locator('.tmenu_item_text')).to_be_visible()

            link.locator('.tmenu_item_link').evaluate("el => el.click()")

            expect (page).to_have_url(re.compile(r"/collections/"))
            page.wait_for_timeout(500)
            page.go_back()
            print(f"Categories '{text}' tested")

        for i in range(categories3):
            page.get_by_role('link', name="PC/ Mac").hover()
            page.wait_for_timeout(500)

            page.get_by_role('tab', name="Peripherals & Accessories").hover()
            page.wait_for_timeout(500)

            link = page.locator('.tmenu_submenu_tab_active .tmenu_item_level_1.tmenu_col-4:has(a[title="Categories"]) + .tmenu_item_level_1.tmenu_col-4 + .tmenu_item_level_1.tmenu_col-4 .tmenu_item_level_2').nth(i)

            text = link.locator('.tmenu_item_text').inner_text()
            expect (link.locator('.tmenu_item_text')).to_be_visible()

            link.locator('.tmenu_item_link').evaluate("el => el.click()")

            expect (page).to_have_url(re.compile(r"/collections/"))
            page.wait_for_timeout(500)
            page.go_back()
            print(f"Categories '{text}' tested")

        
