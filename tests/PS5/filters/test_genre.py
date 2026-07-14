from playwright.sync_api import Page, expect
import re

class TestDatablitzFilters:
    def test_genre(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/collections/playstation-5")

        filters = page.locator('.card')
        genres = filters.get_by_role('button', name="Genre")

        expect (genres).to_be_visible()
        print(f"'Genres' is visible")

        genres.click()
        page.wait_for_timeout(300)
        genres.click()
        page.wait_for_timeout(300)
        print(f"Genres option is working")

    def test_genres_options(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/collections/playstation-5")

        filters = page.locator('.card')

        options = filters.locator('.boost-pfs-filter-option-genre .boost-pfs-filter-option-item-list li').count()
        print(f"{options}")

        for i in range(options):
            option = filters.locator('.boost-pfs-filter-option-genre .boost-pfs-filter-option-item-list li').nth(i)

            text = option.locator('.boost-pfs-filter-option-value').inner_text()
            expect (option.locator('.boost-pfs-filter-option-value')).to_be_visible()

            option.locator('.boost-pfs-filter-button').click()
            expect (page).to_have_url(re.compile(r"collections"))
            page.locator('.boost-pfs-filter-refine-by-wrapper').locator('button[aria-label="Clear"]').first.click()
            page.wait_for_timeout(500)
            print(f"'{text}' tested")