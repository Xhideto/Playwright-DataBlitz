from playwright.sync_api import Page, expect
import re

class TestNavBarPS5:

    def test_playstation_five_sub_menu(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/")

        psfive = page.locator('.tmenu_navbar')

        psfive.get_by_role('link', name="PS5").hover()
        page.wait_for_timeout(500)
        expect (page.locator('.tmenu_submenu_type_mega')).to_be_visible()
        psfive.get_by_role('link', name="PS5", exact=True).click()
        expect (page).to_have_url("https://ecommerce.datablitz.com.ph/collections/playstation-5")
        page.go_back()
        print(f"PS5 submenu is seen")

    def test_playstation_five_recommended(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/")

        psfive = page.locator('.tmenu_navbar')

        psfive.get_by_role('link', name="PS5", exact=True).hover()
        page.wait_for_timeout(500)
        expect (page.locator('.tmenu_submenu_type_mega')).to_be_visible()
        print(f"PS5 submenu is works")

        expect (page.get_by_text("PS5 We Recommend")).to_be_visible()
        print(f"The title is tested")

        recommend_games = page.locator('.tmenu_item_layout_image').count()

        for i in range(recommend_games):
            page.locator('.tmenu_navbar').get_by_role('link', name="PS5", exact=True).hover()
            page.wait_for_timeout(500)

            game = page.locator('.tmenu_item_layout_image').nth(i)
            expect (game.locator('.tmenu_image')).to_be_visible()

            game.hover()
            page.wait_for_timeout(500)
            game.locator('.tmenu_item_link').click()
            expect (page).to_have_url(re.compile(r"/products/"))

            page.wait_for_timeout(1500)

            page.go_back()
            print(f"PS5 recommend game {i+1} tested")

    def test_playstation_five_consoles(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/")

        psfive = page.locator('.tmenu_navbar')

        psfive.get_by_role('link', name="PS5", exact=True).hover()
        page.wait_for_timeout(500)
        expect (page.locator('.tmenu_submenu_type_mega')).to_be_visible()
        print(f"PS5 submenu is seen")

        expect (psfive.get_by_role("link", name="PS5 CONSOLES")).to_be_visible()
        psfive.hover()
        page.wait_for_timeout(500)
        psfive.get_by_role("link", name="PS5 CONSOLES").click()
        expect (page).to_have_url("https://ecommerce.datablitz.com.ph/collections/playstation-5-consoles")
        print(f"PS5 Consoles is tested")

        page.go_back()

        page.locator('.tmenu_navbar').get_by_role('link', name="PS5", exact=True).hover()
        page.wait_for_timeout(500)

        psfive_links = page.locator('.tmenu_item_level_1.tmenu_col-3:has(a[title="PS5 CONSOLES"]) .tmenu_item_level_2').count()

        for i in range(psfive_links):
            page.locator('.tmenu_navbar').get_by_role('link', name="PS5", exact=True).hover()
            page.wait_for_timeout(500)

            link = page.locator('.tmenu_item_level_1.tmenu_col-3:has(a[title="PS5 CONSOLES"]) .tmenu_item_level_2').nth(i)

            text = link.locator('.tmenu_item_text').inner_text()
            expect (link.locator('.tmenu_item_text')).to_be_visible()

            link.hover()
            page.wait_for_timeout(500)
            link.locator('.tmenu_item_link').click()

            expect(page).to_have_url(re.compile(r"/collections/"))
            page.go_back()
            print(f"'{text}' tested")

    def test_playstation_five_games(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/")

        psfive = page.locator('.tmenu_navbar')

        psfive.get_by_role('link', name="PS5", exact=True).hover()
        page.wait_for_timeout(500)
        expect (page.locator('.tmenu_submenu_type_mega')).to_be_visible()
        print(f"PS5 submenu is seen")

        expect (psfive.get_by_role("link", name="PS5 GAMES")).to_be_visible()
        psfive.hover()
        page.wait_for_timeout(500)
        psfive.get_by_role("link", name="PS5 GAMES").click()
        expect (page).to_have_url("https://ecommerce.datablitz.com.ph/collections/playstation-5?pf_t_categories=Games")
        print(f"PS5 Games is tested")

        page.go_back()

        page.locator('.tmenu_navbar').get_by_role('link', name="PS5", exact=True).hover()
        page.wait_for_timeout(500)

        consoles1 = page.locator('.tmenu_item_level_1.tmenu_col-2:has(a[title="PS5 GAMES"]) .tmenu_item_level_2').count()
        consoles2 = page.locator('.tmenu_item_level_1.tmenu_col-2:has(a[title="PS5 GAMES"]) + .tmenu_item_level_1.tmenu_col-2 .tmenu_item_level_2').count()

        for i in range(consoles1):
            page.locator('.tmenu_navbar').get_by_role('link', name="PS5", exact=True).hover()
            page.wait_for_timeout(500)

            link = page.locator('.tmenu_item_level_1.tmenu_col-2:has(a[title="PS5 GAMES"]) .tmenu_item_level_2').nth(i)

            text = link.locator('.tmenu_item_text').inner_text()
            expect (link.locator('.tmenu_item_text')).to_be_visible()

            link.hover()
            page.wait_for_timeout(500)
            link.locator('.tmenu_item_link').click()

            expect(page).to_have_url(re.compile(r"/collections/"))
            page.go_back()
            print(f"Genre '{text}' tested")

        for i in range(consoles2):
            page.locator('.tmenu_navbar').get_by_role('link', name="PS5", exact=True).hover()
            page.wait_for_timeout(500)

            link = page.locator('.tmenu_item_level_1.tmenu_col-2:has(a[title="PS5 GAMES"]) + .tmenu_item_level_1.tmenu_col-2 .tmenu_item_level_2').nth(i)

            text = link.locator('.tmenu_item_text').inner_text()
            expect (link.locator('.tmenu_item_text')).to_be_visible()

            link.hover()
            page.wait_for_timeout(500)
            link.locator('.tmenu_item_link').click()

            expect(page).to_have_url(re.compile(r"/collections/"))
            page.go_back()
            print(f"Genre '{text}' tested")
