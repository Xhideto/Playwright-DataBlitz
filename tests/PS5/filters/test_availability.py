from playwright.sync_api import Page, expect
import re

class TestDatablitzFilters:
    def test_availability(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/collections/playstation-5")

        filters = page.locator('.card')
        availability = filters.get_by_role('button', name="Availability")

        expect (availability).to_be_visible()
        print(f"'Availability' is visible")

        availability.click()
        page.wait_for_timeout(300)
        availability.click()
        page.wait_for_timeout(300)
        print(f"Availability option is working")

    def test_availability_checkbox(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/collections/playstation-5")

        filters = page.locator('.card')

        option = filters.locator('.boost-pfs-filter-option-availability .boost-pfs-filter-option-item-list')

        text = option.locator('.boost-pfs-filter-option-value').inner_text()
        expect (option.locator('.boost-pfs-filter-option-value')).to_be_visible()

        option.locator('.boost-pfs-check-box').click()
        expect (page).to_have_url(re.compile(r"collections"))
        page.locator('.boost-pfs-filter-refine-by-wrapper').locator('button[aria-label="Clear"]').first.click()
        page.wait_for_timeout(500)
        print(f"'{text}' tested")

    def test_availability_text_button(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/collections/playstation-5")

        filters = page.locator('.card')

        option = filters.locator('.boost-pfs-filter-option-availability .boost-pfs-filter-option-item-list')

        text = option.locator('.boost-pfs-filter-option-value').inner_text()
        expect (option.locator('.boost-pfs-filter-option-value')).to_be_visible()

        option.locator('.boost-pfs-filter-button').click()
        expect (page).to_have_url(re.compile(r"collections"))
        page.locator('.boost-pfs-filter-refine-by-wrapper').locator('button[aria-label="Clear"]').first.click()
        page.wait_for_timeout(500)
        print(f"'{text}' tested")