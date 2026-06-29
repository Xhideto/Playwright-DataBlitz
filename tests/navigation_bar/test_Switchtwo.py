from playwright.sync_api import Page, expect
import re

class TestNavBarSwitch:
    def test_switch_two_sub_menu(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/")

        switch_two = page.locator('.tmenu_navbar')

        switch_two.get_by_title('SWITCH').hover()
        page.wait_for_timeout(500)
        expect (page.locator('.tmenu_submenu_type_tab')).to_be_visible()

        expect (switch_two.get_by_role('tab', name="SWITCH 2")).to_be_visible()
        expect(switch_two.get_by_role("tab", name="Switch 2 NEW!")).to_be_visible()
        print(f"'New' Badge is visible")

        switch_two.get_by_role('tab', name="SWITCH 2").click()
        expect (page).to_have_url("https://ecommerce.datablitz.com.ph/collections/nintendo-switch-2")
        page.wait_for_timeout(1500)
        page.go_back()
        print(f"Switch 2 submenu is seen")

    def test_switch_two_recommend(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/")

        switch_two = page.locator('.tmenu_navbar')

        switch_two.get_by_title('SWITCH').hover()
        page.wait_for_timeout(500)
        expect (page.locator('.tmenu_submenu_type_tab')).to_be_visible()

        expect (switch_two.get_by_role('tab', name="SWITCH 2")).to_be_visible()
        expect(switch_two.get_by_role("tab", name="Switch 2 NEW!")).to_be_visible()
        print(f"'New' Badge is visible")

        expect (page.get_by_text("Switch 2 We Recommend")).to_be_visible()
        print(f"The title is tested")

        recommend_games = page.locator('.tmenu_submenu_tab_active .tmenu_item_layout_image').count()

        for i in range(recommend_games):
            page.locator('.tmenu_navbar').get_by_title('SWITCH', exact=True).hover()
            page.wait_for_timeout(500)

            page.get_by_role('tab', name="SWITCH 2").hover()
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
            print(f"Switch 2 recommend game {i+1} tested")

    def test_switch_two_handhelds(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/")

        switch_two = page.locator('.tmenu_navbar')

        switch_two.get_by_title('SWITCH').hover()
        page.wait_for_timeout(500)
        expect (page.locator('.tmenu_submenu_type_tab')).to_be_visible()

        expect (switch_two.get_by_role('tab', name="SWITCH 2")).to_be_visible()
        expect(switch_two.get_by_role("tab", name="Switch 2 NEW!")).to_be_visible()
        print(f"'New' Badge is visible")

        expect (switch_two.get_by_role('link', name="SWITCH 2 CONSOLE", exact=True)).to_be_visible()
        switch_two.hover()
        page.wait_for_timeout(500)
        switch_two.get_by_role('link', name="SWITCH 2 CONSOLE", exact=True).click()
        expect (page).to_have_url("https://ecommerce.datablitz.com.ph/collections/nintendo-switch-2-consoles")

        page.wait_for_timeout(1000)
        page.go_back()

        page.locator('.tmenu_navbar').get_by_title('SWITCH', exact=True).hover()
        page.wait_for_timeout(500)

        page.get_by_role('tab', name="SWITCH 2").hover()
        page.wait_for_timeout(500)

        link = page.locator('.tmenu_item_level_1.tmenu_col-3:has(a[title="SWITCH 2 CONSOLE"]) .tmenu_item_level_2')

        text = link.locator('.tmenu_item_text').inner_text()
        expect (link.locator('.tmenu_item_text')).to_be_visible()

        link.hover()
        page.wait_for_timeout(500)
        link.locator('.tmenu_item_link').click()
        expect (page).to_have_url("https://ecommerce.datablitz.com.ph/collections/nintendo-switch-2-consoles")
        
        page.wait_for_timeout(1000)
        page.go_back()
        print(f"'{text}' tested")

    def test_switch_two_games(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/")

        switch_two = page.locator('.tmenu_navbar')

        switch_two.get_by_title('SWITCH').hover()
        page.wait_for_timeout(500)
        expect (page.locator('.tmenu_submenu_type_tab')).to_be_visible()

        expect (switch_two.get_by_role('tab', name="SWITCH 2")).to_be_visible()
        expect(switch_two.get_by_role("tab", name="Switch 2 NEW!")).to_be_visible()
        print(f"'New' Badge is visible")

        expect (switch_two.get_by_role('link', name="SWITCH 2 GAMES", exact=True)).to_be_visible()
        switch_two.hover()
        page.wait_for_timeout(500)
        switch_two.get_by_role('link', name="SWITCH 2 GAMES", exact=True).click()
        expect (page).to_have_url("https://ecommerce.datablitz.com.ph/collections/nintendo-switch-2-games-1")

        page.wait_for_timeout(1000)
        page.go_back()

        page.locator('.tmenu_navbar').get_by_title('SWITCH', exact=True).hover()
        page.wait_for_timeout(500)

        games1 = page.locator('.tmenu_item_level_1.tmenu_col-2:has(a[title="SWITCH 2 GAMES"]) .tmenu_item_level_2').count()
        games2 = page.locator('.tmenu_item_level_1.tmenu_col-2:has(a[title="SWITCH 2 GAMES"]) + .tmenu_item_level_1.tmenu_col-2 .tmenu_item_level_2').count()

        for i in range(games1):

            page.locator('.tmenu_navbar').get_by_title('SWITCH', exact=True).hover()
            page.wait_for_timeout(500)

            page.get_by_role('tab', name="SWITCH 2").hover()
            page.wait_for_timeout(500)

            link = page.locator('.tmenu_item_level_1.tmenu_col-2:has(a[title="SWITCH 2 GAMES"]) .tmenu_item_level_2').nth(i)

            text = link.locator('.tmenu_item_text').inner_text()
            expect (link.locator('.tmenu_item_text')).to_be_visible()

            link.locator('.tmenu_item_link').evaluate("el => el.click()")

            expect (page).to_have_url(re.compile(r"/collections/"))
            page.go_back()
            print(f"Genre '{text}' tested")

        for i in range(games2):

            page.locator('.tmenu_navbar').get_by_title('SWITCH', exact=True).hover()
            page.wait_for_timeout(500)

            page.get_by_role('tab', name="SWITCH 2").hover()
            page.wait_for_timeout(500)

            link = page.locator('.tmenu_item_level_1.tmenu_col-2:has(a[title="SWITCH 2 GAMES"]) + .tmenu_item_level_1.tmenu_col-2 .tmenu_item_level_2').nth(i)

            text = link.locator('.tmenu_item_text').inner_text()
            expect (link.locator('.tmenu_item_text')).to_be_visible()

            link.locator('.tmenu_item_link').evaluate("el => el.click()")

            expect (page).to_have_url(re.compile(r"/collections/"))
            page.go_back()
            print(f"Genre '{text}' tested")

    def test_switch_two_accessories(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/")

        switch_two = page.locator('.tmenu_navbar')

        switch_two.get_by_title('SWITCH').hover()
        page.wait_for_timeout(500)
        expect (page.locator('.tmenu_submenu_type_tab')).to_be_visible()

        expect (switch_two.get_by_role('tab', name="SWITCH 2")).to_be_visible()
        expect(switch_two.get_by_role("tab", name="Switch 2 NEW!")).to_be_visible()
        print(f"'New' Badge is visible")

        expect (switch_two.get_by_role('link', name="SWITCH 2 ACCESSORIES", exact=True)).to_be_visible()
        switch_two.hover()
        page.wait_for_timeout(500)
        switch_two.get_by_role('link', name="SWITCH 2 ACCESSORIES", exact=True).click()
        expect (page).to_have_url("https://ecommerce.datablitz.com.ph/collections/nintendo-switch-2-accessories")

        page.wait_for_timeout(1000)
        page.go_back()

        page.locator('.tmenu_navbar').get_by_title('SWITCH', exact=True).hover()
        page.wait_for_timeout(500)

        accessories1 = page.locator('.tmenu_item_level_1.tmenu_col-2:has(a[title="SWITCH 2 ACCESSORIES"]) .tmenu_item_level_2').count()
        accessories2 = page.locator('.tmenu_item_level_1.tmenu_col-2:has(a[title="SWITCH 2 ACCESSORIES"]) + .tmenu_item_level_1.tmenu_col-3 .tmenu_item_level_2').count()

        for i in range(accessories1):

            page.locator('.tmenu_navbar').get_by_title('SWITCH', exact=True).hover()
            page.wait_for_timeout(500)

            page.get_by_role('tab', name="SWITCH 2").hover()
            page.wait_for_timeout(500)

            link = page.locator('.tmenu_item_level_1.tmenu_col-2:has(a[title="SWITCH 2 ACCESSORIES"]) .tmenu_item_level_2').nth(i)

            text = link.locator('.tmenu_item_text').inner_text()
            expect (link.locator('.tmenu_item_text')).to_be_visible()

            link.locator('.tmenu_item_link').evaluate("el => el.click()")

            expect (page).to_have_url(re.compile(r"/collections/"))
            page.go_back()
            print(f"Accessories '{text}' tested")

        for i in range(accessories2):

            page.locator('.tmenu_navbar').get_by_title('SWITCH', exact=True).hover()
            page.wait_for_timeout(500)

            page.get_by_role('tab', name="SWITCH 2").hover()
            page.wait_for_timeout(500)

            link = page.locator('.tmenu_item_level_1.tmenu_col-2:has(a[title="SWITCH 2 ACCESSORIES"]) + .tmenu_item_level_1.tmenu_col-3 .tmenu_item_level_2').nth(i)

            text = link.locator('.tmenu_item_text').inner_text()
            expect (link.locator('.tmenu_item_text')).to_be_visible()

            link.locator('.tmenu_item_link').evaluate("el => el.click()")

            expect (page).to_have_url(re.compile(r"/collections/"))
            page.go_back()
            print(f"Accessories '{text}' tested")
            
