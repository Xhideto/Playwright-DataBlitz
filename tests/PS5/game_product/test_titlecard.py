from playwright.sync_api import Page, expect
import re

class TestDatablitzPS5Product:
    def test_product_title(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/products/ps5-assassins-creed-black-flag-resynced")

        card = page.locator('.card__section')

        expect (card.locator('.product-meta__title')).to_be_visible()
        print(f"PS5 Assassins Creed Black Flag Resynced (Asian) is Visible")

    def test_product_reviews(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/products/ps5-assassins-creed-black-flag-resynced")
        page.wait_for_timeout(500)

        card = page.locator('.card__section')

        expect (card.locator('.gw-rv-rating-stars').first).to_be_visible()
        print(f"Review stars are visible")

        review_text = card.locator('.gw-text.gw-text--heading-sm').inner_text()
        print(f"Review count text: '{review_text}'")

        assert "Reviews" in review_text, "No Review text found"
        print(f"Review count text is verified and visible")

        expect (card.locator('.gw-rv-star-rating-summary')).to_be_visible()

        card.locator('.gw-rv-star-rating-summary').hover()
        page.wait_for_timeout(500)
        expect (page.locator('.gw-tooltip__wrapper')).to_be_visible()
        print(f"Review ratings is visible")

    def test_product_reference(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/products/ps5-assassins-creed-black-flag-resynced")

        card = page.locator('.card__section')
        reference = card.locator('.product-meta__reference')

        expect (reference.locator('.product-meta__vendor')).to_be_visible()

        reference.locator('.product-meta__vendor').click()
        expect (page).to_have_url(re.compile(r"/collections/"))
        page.wait_for_timeout(500)
        page.go_back()
        print(f"Ubisoft link is working")

        expect (reference.locator('.product-meta__sku')).to_be_visible()
        print(f"The product SKU is visible")

    def test_product_share_socials(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/products/ps5-assassins-creed-black-flag-resynced")
        
        card = page.locator('.card__section')
        socials = card.locator('.social-media__item-list').first

        expect (socials).to_be_visible()
        print(f"Social items are visible")

        links = socials.locator('a[target="_blank"]').count()
        assert links > 0, "No social links found"
        print(f"Found {links} social links")

        for i in range(links):
            social = page.locator('.social-media__item-list')
            link = social.locator('a[target="_blank"]').nth(i)

            href = link.get_attribute('href')
            print(f"{href}")

            if href and href.startswith('mailto'):
                assert 'mailto' in href
                print(f"Link {i+1} is email share link ✅")
                continue 

            with page.expect_popup() as social_media:
                link.click()

            new_tab = social_media.value
            new_tab.wait_for_load_state()

            url = new_tab.url
            expect (new_tab).to_have_url(re.compile(r"https"))
            page.wait_for_timeout(1000)
            print(f"{i+1} {url} is working")
            new_tab.close()

    def test_product_description(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/products/ps5-assassins-creed-black-flag-resynced")
                
        card = page.locator('.card__section')
        short_descript = card.locator('.product-meta__short-description')

        expect (short_descript.locator('.rte').first).to_be_visible()
        print(f"The short description is visible")

        expect (short_descript.get_by_role('link', name="See full description")).to_be_visible()
        short_descript.get_by_role('link', name="See full description").click()
        page.wait_for_timeout(500)
        print(f"Full description expected")