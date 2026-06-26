from playwright.sync_api import Page, expect
import re

class TestNavBarPS4:

    def test_playstation_four_sub_menu(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/")

        psfour = page.locator('.tmenu_navbar')

        psfour.get_by_role('link', name="PS4").hover()
        page.wait_for_timeout(500)
        expect (page.locator('.tmenu_submenu_type_mega')).to_be_visible()
        psfour.get_by_role('link', name="PS4", exact=True).click()
        expect (page).to_have_url("https://ecommerce.datablitz.com.ph/collections/playstation-4")
        page.wait_for_timeout(1000)
        page.go_back()
        print(f"PS4 submenu is seen")

    def test_playstation_four_recommended(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/")

        psfour = page.locator('.tmenu_navbar')

        psfour.get_by_role('link', name="PS4", exact=True).hover()
        page.wait_for_timeout(500)
        expect (page.locator('.tmenu_submenu_type_mega')).to_be_visible()
        print(f"PS4 submenu is works")

        expect (page.get_by_text("PS4 We Recommend")).to_be_visible()
        print(f"The title is tested")

        recommend_games = page.locator('.tmenu_item_layout_image').count()

        for i in range(recommend_games):
            page.locator('.tmenu_navbar').get_by_role('link', name="PS4", exact=True).hover()
            page.wait_for_timeout(500)

            game = page.locator('.tmenu_item_layout_image').nth(i)
            expect (game.locator('.tmenu_image')).to_be_visible()

            game.hover()
            page.wait_for_timeout(500)
            game.locator('.tmenu_item_link').click()
            expect (page).to_have_url(re.compile(r"/products/"))

            page.wait_for_timeout(1500)

            page.go_back()
            print(f"PS4 recommend game {i+1} tested")

    def test_playstation_four_consoles(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/")

        psfour = page.locator('.tmenu_navbar')

        psfour.get_by_role('link', name="PS4", exact=True).hover()
        page.wait_for_timeout(500)
        expect (page.locator('.tmenu_submenu_type_mega')).to_be_visible()
        print(f"PS4 submenu is seen")

        expect (psfour.get_by_role("link", name="PS4 CONSOLES")).to_be_visible()
        psfour.hover()
        page.wait_for_timeout(500)
        psfour.get_by_role("link", name="PS4 CONSOLES").click()
        expect (page).to_have_url("https://ecommerce.datablitz.com.ph/collections/playstation-4?pf_t_categories=Consoles")
        print(f"PS4 Consoles is tested")

        page.go_back()

        page.locator('.tmenu_navbar').get_by_role('link', name="PS4", exact=True).hover()
        page.wait_for_timeout(500)

        psfour_links = page.locator('.tmenu_item_level_1.tmenu_col-3:has(a[title="PS4 CONSOLES"]) .tmenu_item_level_2').count()

        for i in range(psfour_links):
            page.locator('.tmenu_navbar').get_by_role('link', name="PS4", exact=True).hover()
            page.wait_for_timeout(500)

            link = page.locator('.tmenu_item_level_1.tmenu_col-3:has(a[title="PS4 CONSOLES"]) .tmenu_item_level_2').nth(i)

            text = link.locator('.tmenu_item_text').inner_text()
            expect (link.locator('.tmenu_item_text')).to_be_visible()

            link.hover()
            page.wait_for_timeout(500)
            link.locator('.tmenu_item_link').click()

            expect(page).to_have_url(re.compile(r"/collections/"))
            page.go_back()
            print(f"'{text}' tested")