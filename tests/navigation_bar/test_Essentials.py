from playwright.sync_api import Page, expect
import re

class TestNavBarMoreEssentials:
    def test_more_essentials_sub_menu(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/")

        essential = page.locator('.tmenu_navbar')

        essential.get_by_role('link', name="More Essentials").hover()
        page.wait_for_timeout(500)
        expect (page.locator('.tmenu_submenu_type_mega')).to_be_visible()

        essential.get_by_role('link', name="More Essentials", exact=True).click()
        expect (page).to_have_url("https://ecommerce.datablitz.com.ph/collections/more-essentials")
        page.wait_for_timeout(1000)

        page.go_back
        print(f"More Essentials page is working")

    def test_more_essentials_recommend(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/")

        page.locator('.tmenu_navbar').get_by_role('link', name="More Essentials", exact=True).hover()
        page.wait_for_timeout(500)
        expect (page.locator('.tmenu_submenu_type_mega')).to_be_visible()
        print(f"More Essentials submenu is visible")

        expect (page.get_by_text("We Recommend")).to_be_visible()
        print(f"The title is tested")

        recommend_essentials = page.locator('.tmenu_item_layout_image').count()

        for i in range(recommend_essentials):
            page.locator('.tmenu_navbar').get_by_role('link', name="More Essentials", exact=True).hover()

            essential = page.locator('.tmenu_item_layout_image').nth(i)
            expect (essential.locator('.tmenu_image')).to_be_visible()

            essential.locator('.tmenu_item_link').click()
            expect (page).to_have_url(re.compile(r"/products/"))

            page.wait_for_timeout(1000)
            page.go_back()
            print(f"Recommended More Essentials {i+1} tested")

    def test_more_essentials_categories(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/")

        essential = page.locator('.tmenu_navbar')

        essential.get_by_role('link', name="More Essentials", exact=True).hover()
        page.wait_for_timeout(500)
        expect (page.locator('.tmenu_submenu_type_mega')).to_be_visible()
        print(f"More Essentials submenu is visible")

        expect (essential.get_by_role('link', name="CATEGORIES")).to_be_visible()
        print(f"Categories Exist")

        essentials = page.locator('.tmenu_item_level_1.tmenu_col:has(a[title="CATEGORIES"]) .tmenu_item_level_2').count()
        essentials2 = page.locator('.tmenu_item_level_1:has(a[title="CATEGORIES"]) + .tmenu_item_level_1:has(a[title=""]) .tmenu_item_level_2').count()
        essentials3 = page.locator('.tmenu_item_level_1:has(a[title="CATEGORIES"]) + .tmenu_item_level_1:has(a[title=""]) + .tmenu_item_level_1:has(a[title=""]) .tmenu_item_level_2').count()

        for i in range(essentials):
            page.locator('.tmenu_navbar').get_by_role('link', name="More Essentials", exact=True).hover()
            page.wait_for_timeout(500)

            link = page.locator('.tmenu_item_level_1.tmenu_col:has(a[title="CATEGORIES"]) .tmenu_item_level_2').nth(i)
            text = link.locator(".tmenu_item_text").inner_text()

            expect (link.locator('.tmenu_item_text')).to_be_visible()

            link.locator('.tmenu_item_link').click()

            expect (page).to_have_url(re.compile(r"/collections/"))

            page.go_back()
            print(f"More Essential '{text}' tested")

        for i in range(essentials2):
            page.locator('.tmenu_navbar').get_by_role('link', name="More Essentials", exact=True).hover()
            page.wait_for_timeout(500)

            link = page.locator('.tmenu_item_level_1:has(a[title="CATEGORIES"]) + .tmenu_item_level_1:has(a[title=""]) .tmenu_item_level_2').nth(i)
            text = link.locator(".tmenu_item_text").inner_text()

            expect (link.locator('.tmenu_item_text')).to_be_visible()

            link.locator('.tmenu_item_link').click()

            expect (page).to_have_url(re.compile(r"/collections/"))

            page.go_back()
            print(f"More Essential '{text}' tested")

        for i in range(essentials3):
            page.locator('.tmenu_navbar').get_by_role('link', name="More Essentials", exact=True).hover()
            page.wait_for_timeout(500)

            link = page.locator('.tmenu_item_level_1:has(a[title="CATEGORIES"]) + .tmenu_item_level_1:has(a[title=""]) + .tmenu_item_level_1:has(a[title=""]) .tmenu_item_level_2').nth(i)
            text = link.locator(".tmenu_item_text").inner_text()

            expect (link.locator('.tmenu_item_text')).to_be_visible()

            link.locator('.tmenu_item_link').evaluate("el => el.click()")

            expect (page).to_have_url(re.compile(r"/collections/"))

            page.go_back()
            print(f"More Essential '{text}' tested")