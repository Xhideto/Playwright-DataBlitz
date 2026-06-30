from playwright.sync_api import Page, expect
import re

class TestNavBarXboxOne:
    def test_xbox_one_sub_menu(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/")

        xbox_one = page.locator(".tmenu_navbar")

        xbox_one.get_by_title('XBOX').hover()
        page.wait_for_timeout(500)
        expect (page.locator('.tmenu_submenu_type_tab')).to_be_visible()

        expect (xbox_one.get_by_role('tab', name="Xbox One", exact=True)).to_be_visible()

        xbox_one.get_by_role('tab', name="Xbox One", exact=True).click()
        expect (page).to_have_url("https://ecommerce.datablitz.com.ph/collections/xbox-one")
        page.wait_for_timeout(1000)
        page.go_back()
        print(f"Xbox One submenu is visible")

    def test_switch_recommend(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/")

        xbox_one = page.locator('.tmenu_navbar')

        xbox_one.get_by_title('XBOX').hover()
        page.wait_for_timeout(500)
        expect (page.locator('.tmenu_submenu_type_tab')).to_be_visible()

        expect (xbox_one.get_by_role('tab', name="Xbox One", exact=True)).to_be_visible()

        expect (page.get_by_text("Xbox One We Recommend")).to_be_visible()
        print(f"The title is tested")

        recommend_games = page.locator('.tmenu_submenu_tab_active .tmenu_item_layout_image').count()

        for i in range(recommend_games):
            page.locator('.tmenu_navbar').get_by_title('XBOX', exact=True).hover()
            page.wait_for_timeout(500)

            page.get_by_role('tab', name="Xbox One", exact=True).hover()
            page.wait_for_timeout(500)

            game = page.locator('.tmenu_submenu_tab_active .tmenu_item_layout_image').nth(i)
            expect (game.locator('.tmenu_image')).to_be_visible()

            game.hover()
            page.wait_for_timeout(500)
            game.locator('.tmenu_item_link').click()
            expect (page).to_have_url(re.compile(r"/products/"))

            page.wait_for_timeout(1000)

            page.go_back()
            page.wait_for_timeout(500)
            print(f"Switch recommend game {i+1} tested")