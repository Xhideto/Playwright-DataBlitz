from playwright.sync_api import Page, expect
import re

class TestNavBarCollectibles:
    def test_collectibles_sub_menu(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/")

        collect = page.locator('.tmenu_navbar')

        collect.get_by_role('link', name="Collectibles").hover()
        page.wait_for_timeout(500)
        expect (page.locator('.tmenu_submenu_type_mega')).to_be_visible()

        collect.get_by_role('link', name="Collectibles", exact=True).click()
        expect (page).to_have_url("https://ecommerce.datablitz.com.ph/collections/collectibles")
        page.wait_for_timeout(1000)

        page.go_back
        print(f"Collectibles page is working")

    def test_collectibles_recommend(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/")

        page.locator('.tmenu_navbar').get_by_role('link', name="Collectibles", exact=True).hover()
        page.wait_for_timeout(500)
        expect (page.locator('.tmenu_submenu_type_mega')).to_be_visible()
        print(f"Collectibles submenu is visible")

        expect (page.get_by_text("We Recommend")).to_be_visible()
        print(f"The title is tested")

        recommend_collects = page.locator('.tmenu_item_layout_image').count()

        for i in range(recommend_collects):
            page.locator('.tmenu_navbar').get_by_role('link', name="Collectibles", exact=True).hover()

            collectible = page.locator('.tmenu_item_layout_image').nth(i)
            expect (collectible.locator('.tmenu_image')).to_be_visible()

            collectible.locator('.tmenu_item_link').click()
            expect (page).to_have_url(re.compile(r"/products/"))

            page.wait_for_timeout(1000)
            page.go_back()
            print(f"Recommended collectibles {i+1} tested")