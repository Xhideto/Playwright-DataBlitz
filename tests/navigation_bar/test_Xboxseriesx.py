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

    def test_xbox_x_recommend(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/")

        xbox_x = page.locator('.tmenu_navbar')

        xbox_x.get_by_title('XBOX').hover()
        page.wait_for_timeout(500)
        expect (page.locator('.tmenu_submenu_type_tab')).to_be_visible()

        expect (xbox_x.get_by_role('tab', name="Xbox Series X")).to_be_visible()

        expect (page.get_by_text("Xbox Series X We Recommend")).to_be_visible()
        print(f"The title is tested")

        recommend_games = page.locator('.tmenu_submenu_tab_active .tmenu_item_layout_image').count()

        for i in range(recommend_games):
            page.locator('.tmenu_navbar').get_by_title('XBOX', exact=True).hover()
            page.wait_for_timeout(500)

            page.get_by_role('tab', name="Xbox Series X").hover()
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
            print(f"Xbox Series X recommend game {i+1} tested")

    def test_xbox_x_console(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/")

        xbox_x = page.locator('.tmenu_navbar')

        xbox_x.get_by_title('XBOX').hover()
        page.wait_for_timeout(500)
        expect (page.locator('.tmenu_submenu_type_tab')).to_be_visible()

        expect (xbox_x.get_by_role('tab', name="Xbox Series X", exact=True)).to_be_visible()
        page.get_by_role('tab', name="Xbox Series X", exact=True).hover()
        page.wait_for_timeout(500)

        expect (xbox_x.get_by_role('link', name="XBOXSX CONSOLE", exact=True)).to_be_visible()
        xbox_x.hover()
        page.wait_for_timeout(500)
        xbox_x.get_by_role('link', name="XBOXSX CONSOLE", exact=True).click()
        expect (page).to_have_url("https://ecommerce.datablitz.com.ph/collections/xbox-series-x?pf_t_categories=Consoles")

        page.wait_for_timeout(1000)
        page.go_back()

        page.locator('.tmenu_navbar').get_by_title('XBOX', exact=True).hover()
        page.wait_for_timeout(500)

        page.get_by_role('tab', name="Xbox Series X").hover()
        page.wait_for_timeout(500)

        link = page.locator('.tmenu_item_level_1.tmenu_col-3:has(a[title="XBOXSX CONSOLE"]) .tmenu_item_level_2')

        text = link.locator('.tmenu_item_text').inner_text()
        expect (link.locator('.tmenu_item_text')).to_be_visible()

        link.hover()
        page.wait_for_timeout(500)
        link.locator('.tmenu_item_link').click()
        expect (page).to_have_url("https://ecommerce.datablitz.com.ph/collections/xbox-series-x?pf_t_categories=Consoles")
        
        page.wait_for_timeout(1000)
        page.go_back()
        print(f"'{text}' tested")

    def test_xbox_x_games(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/")

        xbox_x = page.locator('.tmenu_navbar')

        xbox_x.get_by_title('XBOX').hover()
        page.wait_for_timeout(500)
        expect (page.locator('.tmenu_submenu_type_tab')).to_be_visible()

        expect (xbox_x.get_by_role('tab', name="Xbox Series X")).to_be_visible()
        page.get_by_role('tab', name="Xbox Series X").hover()
        page.wait_for_timeout(500)

        expect (xbox_x.get_by_role('link', name="XBOXSX GAMES", exact=True)).to_be_visible()
        xbox_x.hover()
        page.wait_for_timeout(500)
        xbox_x.get_by_role('link', name="XBOXSX GAMES", exact=True).click()
        expect (page).to_have_url("https://ecommerce.datablitz.com.ph/collections/xbox-games")

        page.wait_for_timeout(1000)
        page.go_back()

        page.locator('.tmenu_navbar').get_by_title('XBOX', exact=True).hover()
        page.wait_for_timeout(500)

        games1 = page.locator('.tmenu_item_level_1.tmenu_col-2:has(a[title="XBOXSX GAMES"]) .tmenu_item_level_2').count()
        games2 = page.locator('.tmenu_item_level_1.tmenu_col-2:has(a[title="XBOXSX GAMES"]) + .tmenu_item_level_1.tmenu_col-2 .tmenu_item_level_2').count()

        for i in range(games1):

            page.locator('.tmenu_navbar').get_by_title('XBOX', exact=True).hover()
            page.wait_for_timeout(500)

            page.get_by_role('tab', name="Xbox Series X").hover()
            page.wait_for_timeout(500)

            link = page.locator('.tmenu_item_level_1.tmenu_col-2:has(a[title="XBOXSX GAMES"]) .tmenu_item_level_2').nth(i)

            text = link.locator('.tmenu_item_text').inner_text()
            expect (link.locator('.tmenu_item_text')).to_be_visible()

            link.locator('.tmenu_item_link').evaluate("el => el.click()")

            expect (page).to_have_url(re.compile(r"/collections/"))
            page.go_back()
            print(f"Genre '{text}' tested")

        for i in range(games2):

            page.locator('.tmenu_navbar').get_by_title('XBOX', exact=True).hover()
            page.wait_for_timeout(500)

            page.get_by_role('tab', name="Xbox Series X").hover()
            page.wait_for_timeout(500)

            link = page.locator('.tmenu_item_level_1.tmenu_col-2:has(a[title="XBOXSX GAMES"]) + .tmenu_item_level_1.tmenu_col-2 .tmenu_item_level_2').nth(i)

            text = link.locator('.tmenu_item_text').inner_text()
            expect (link.locator('.tmenu_item_text')).to_be_visible()

            link.locator('.tmenu_item_link').evaluate("el => el.click()")

            expect (page).to_have_url(re.compile(r"/collections/"))
            page.go_back()
            print(f"Genre '{text}' tested")