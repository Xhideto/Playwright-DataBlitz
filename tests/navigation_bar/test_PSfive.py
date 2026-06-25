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

    def test_playstation_five_titles(self, page: Page):
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
        print(f"The title is tested")

        page.go_back()

        page.locator('.tmenu_navbar').get_by_role('link', name="PS5", exact=True).hover()
        page.wait_for_timeout(500)

        expect (psfive.get_by_role("link", name="PS5 GAMES", exact=True)).to_be_visible()
        psfive.hover()
        page.wait_for_timeout(500)
        psfive.get_by_role("link", name="PS5 GAMES", exact=True).click()
        expect (page).to_have_url("https://ecommerce.datablitz.com.ph/collections/playstation-5?pf_t_categories=Games")
        print(f"PS5 Games tested")

        page.go_back()

        page.locator('.tmenu_navbar').get_by_role('link', name="PS5", exact=True).hover()
        page.wait_for_timeout(500)

        expect (psfive.get_by_role("link", name="PS5 ACCESSORIES", exact=True)).to_be_visible()
        psfive.hover()
        page.wait_for_timeout(500)
        psfive.get_by_role("link", name="PS5 ACCESSORIES", exact=True).click()
        expect (page).to_have_url("https://ecommerce.datablitz.com.ph/collections/playstation-5?pf_t_categories=accessories")
        print(f"PS5 Accessories tested")

        page.go_back()

    def test_playstation_five_submenus(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/")

        psfive = page.locator('.tmenu_navbar')

        psfive.get_by_role('link', name="PS5", exact=True).hover()
        page.wait_for_timeout(500)
        expect (page.locator('.tmenu_submenu_type_mega')).to_be_visible()
        print(f"PS5 submenu is seen")

        submenus = page.locator('.tmenu_item_level_2.tmenu_item_layout_text').count()

        for i in range(submenus):
            page.locator('.tmenu_navbar').get_by_role('link', name="PS5", exact=True).hover()
            page.wait_for_timeout(500)

            submenu = page.locator('.tmenu_item_level_2.tmenu_item_layout_text').nth(i)

            expect (submenu.locator('.tmenu_item_text')).to_be_visible()

            submenu.hover()
            page.wait_for_timeout(500)
            submenu.locator('.tmenu_item_link').click()

            expect(page).to_have_url(re.compile(r"/collections/"))
            page.go_back()
            print(f"submenu title links {i+1} tested")

