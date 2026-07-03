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

    def test_pc_others_recommend(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/")

        pc_others = page.locator('.tmenu_navbar')

        pc_others.get_by_role('link', name="PC/ Mac").hover()
        page.wait_for_timeout(500)
        expect (page.locator('.tmenu_submenu_type_tab')).to_be_visible()

        expect (pc_others.get_by_role('tab', name="Others").nth(0)).to_be_visible()

        expect (page.get_by_text("Others").nth(1)).to_be_visible()
        print(f"The text is seen")

        recommend_others = page.locator('.tmenu_submenu_tab_active .tmenu_item_layout_image').count()

        for i in range(recommend_others):
            page.get_by_role('link', name="PC/ Mac").hover()
            page.wait_for_timeout(500)

            page.get_by_role('tab', name="Others").hover()
            page.wait_for_timeout(500)

            others = page.locator('.tmenu_submenu_tab_active .tmenu_item_layout_image').nth(i)
            expect (others.locator('.tmenu_image')).to_be_visible()

            others.locator('.tmenu_item_link').click()

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
            print(f"PC/Mac recommended Others {i+1} tested")

    def test_pc_others_categories(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/")

        pc_others = page.locator('.tmenu_navbar')

        pc_others.get_by_role('link', name="PC/ Mac").hover()
        page.wait_for_timeout(500)
        expect (page.locator('.tmenu_submenu_type_tab')).to_be_visible()

        expect (pc_others.get_by_role('tab', name="Others")).to_be_visible()
        pc_others.get_by_role('tab', name="Others").hover()

        expect (pc_others.locator('.tmenu_submenu_tab_active').get_by_role('link', name="Categories")).to_be_visible()
        pc_others.locator('.tmenu_submenu_tab_active').get_by_role('link', name="Categories").click()
        expect (page).to_have_url("https://ecommerce.datablitz.com.ph/collections/category-nintendo-switch-console?pf_t_categories=Consoles") #When clicked idk why it directs to this link

        page.wait_for_timeout(1000)
        page.go_back()

        print(f"Categories is working")

        page.locator('.tmenu_navbar').get_by_role('link', name="PC/ Mac").hover()
        page.wait_for_timeout(500)

        categories1 = page.locator('#tmenu-tabpanel-tmenu-menu-478782 .tmenu_item_level_1.tmenu_col-4:has(a[title="Categories"]) .tmenu_item_level_2').count()
        categories2 = page.locator('#tmenu-tabpanel-tmenu-menu-478782 .tmenu_item_level_1.tmenu_col-4:has(a[title="Categories"]) + .tmenu_item_level_1.tmenu_col-4 .tmenu_item_level_2').count()
        categories3 = page.locator('#tmenu-tabpanel-tmenu-menu-478782 .tmenu_item_level_1.tmenu_col-4:has(a[title="Categories"]) + .tmenu_item_level_1.tmenu_col-4 + .tmenu_item_level_1.tmenu_col-4 .tmenu_item_level_2').count()

        for i in range(categories1):
            page.get_by_role('link', name="PC/ Mac").hover()
            page.wait_for_timeout(500)

            page.get_by_role('tab', name="Others").hover()
            page.wait_for_timeout(500)

            link = page.locator('#tmenu-tabpanel-tmenu-menu-478782 .tmenu_item_level_1.tmenu_col-4:has(a[title="Categories"]) .tmenu_item_level_2').nth(i)

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

            page.get_by_role('tab', name="Others").hover()
            page.wait_for_timeout(500)

            link = page.locator('#tmenu-tabpanel-tmenu-menu-478782 .tmenu_item_level_1.tmenu_col-4:has(a[title="Categories"]) + .tmenu_item_level_1.tmenu_col-4 .tmenu_item_level_2').nth(i)

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

            page.get_by_role('tab', name="Others").hover()
            page.wait_for_timeout(500)

            link = page.locator('#tmenu-tabpanel-tmenu-menu-478782 .tmenu_item_level_1.tmenu_col-4:has(a[title="Categories"]) + .tmenu_item_level_1.tmenu_col-4 + .tmenu_item_level_1.tmenu_col-4 .tmenu_item_level_2').nth(i)

            text = link.locator('.tmenu_item_text').inner_text()
            expect (link.locator('.tmenu_item_text')).to_be_visible()

            link.locator('.tmenu_item_link').evaluate("el => el.click()")

            expect (page).to_have_url(re.compile(r"/collections/"))
            page.wait_for_timeout(500)
            page.go_back()
            print(f"Categories '{text}' tested")