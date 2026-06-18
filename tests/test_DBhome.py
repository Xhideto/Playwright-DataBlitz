from playwright.sync_api import Page, expect
import re

class TestDatablitzHomepage:

    def test_home_title(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/")
        expect (page).to_have_title("DataBlitz - Your Total Gaming and Multimedia Store")

    def test_home_first_promo_img(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/")

        expect (page.locator('.promo-block').nth(0)).to_be_visible()
        page.locator('.promo-block').nth(0).click()
        expect (page).to_have_url("https://ecommerce.datablitz.com.ph/collections/ayaneo")

    def test_home_second_promo_img(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/")

        expect (page.locator('.promo-block').nth(1)).to_be_visible()
        page.locator('.promo-block').nth(1).click()
        expect (page).to_have_url("https://ecommerce.datablitz.com.ph/collections/gpd-handheld-console")

    def test_home_third_promo_img(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/")

        expect (page.locator('.promo-block').nth(2)).to_be_visible()
        page.locator('.promo-block').nth(2).click()
        expect (page).to_have_url("https://ecommerce.datablitz.com.ph/collections/steam-deck-1")

    def test_home_first_promo_button(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/")

        expect (page.locator('text=Shop Now!').nth(0)).to_be_visible()
        page.locator('text=Shop Now!').nth(0).click()
        expect (page).to_have_url("https://ecommerce.datablitz.com.ph/collections/ayaneo")

    def test_home_second_promo_button(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/")

        expect (page.locator('text=Shop Now!').nth(1)).to_be_visible()
        page.locator('text=Shop Now!').nth(1).click()
        expect (page).to_have_url("https://ecommerce.datablitz.com.ph/collections/gpd-handheld-console")

    def test_home_third_promo_button(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/")

        expect (page.locator('text=Shop Now!').nth(2)).to_be_visible()
        page.locator('text=Shop Now!').nth(2).click()
        expect (page).to_have_url("https://ecommerce.datablitz.com.ph/collections/steam-deck-1")

    def test_home_begin_content(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/")

        expect (page.locator("#shopify-section-16428086583d0db429").get_by_alt_text('Your Most Trusted DataBlitz Store')).to_be_visible()
        expect (page.locator("#shopify-section-16428086583d0db429").get_by_text('Your Most Trusted DataBlitz Store')).to_be_visible()
        expect (page.locator("#shopify-section-16428086583d0db429").get_by_text('100% All Brand New & Original. Shop with confidence!')).to_be_visible()

        expect (page.locator("#shopify-section-16428086583d0db429").get_by_text('Fast Shipping Nationwide')).to_be_visible()
        expect (page.locator("#shopify-section-16428086583d0db429").get_by_text('Ships in 24 hours! Express and Same-Day Delivery within Metro Manila!')).to_be_visible()

        expect (page.locator("#shopify-section-16428086583d0db429").get_by_text('Save on Loyalty Rewards')).to_be_visible()
        expect (page.locator("#shopify-section-16428086583d0db429").get_by_text('Sign in to start earning Loyalty Rewards Points!')).to_be_visible()

        expect (page.locator("#shopify-section-16428086583d0db429").get_by_text('100% Safe and Secure')).to_be_visible()
        expect (page.locator("#shopify-section-16428086583d0db429").get_by_text('All Transactions are Fully Encrypted with State of the Art Technology!')).to_be_visible()

    def test_hot_picks_text(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/")

        expect (page.get_by_role("heading", name="Hot Picks")).to_be_visible()

    def test_hot_picks_list(self, page: Page):
         page.goto("https://ecommerce.datablitz.com.ph/")

         page.locator("#shopify-section-1584623859185 .collection-item").nth(0).click()
         page.go_back()
         page.locator("#shopify-section-1584623859185 .collection-item").nth(1).click()
         page.go_back()
         page.locator("#shopify-section-1584623859185 .collection-item").nth(2).click()
         page.go_back()
         page.locator("#shopify-section-1584623859185 .collection-item").nth(3).click()
         page.go_back()
         page.locator("#shopify-section-1584623859185 .collection-item").nth(4).click()
         page.go_back()
         page.locator("#shopify-section-1584623859185 .collection-item").nth(5).click()
         expect (page).to_have_url(re.compile(r"/collections/"))

    def test_hot_picks_nextb(self, page: Page):
            page.goto("https://ecommerce.datablitz.com.ph/")

            next_button = page.locator("#shopify-section-1584623859185").get_by_role("button", name="Next")
            expect(next_button).to_be_visible()
            next_button.click()

    def test_hot_picks_previousb(self, page: Page):
            page.goto("https://ecommerce.datablitz.com.ph/")

            next_button = page.locator("#shopify-section-1584623859185").get_by_role("button", name="Next")
            expect(next_button).to_be_visible()
            next_button.click()

            previous_button = page.locator("#shopify-section-1584623859185").get_by_role("button", name="Previous")
            expect(previous_button).to_be_visible()
            previous_button.click()

    def test_new_arrivals(self, page: Page):
         page.goto("https://ecommerce.datablitz.com.ph/")

         expect (page.get_by_role("heading", name="New Arrivals")).to_be_visible()

         expect (page.locator("#shopify-section-1590542985479").get_by_text("View all ")).to_be_visible()
         page.locator('#shopify-section-1590542985479').get_by_text("View all ").click()
         expect (page).to_have_url("https://ecommerce.datablitz.com.ph/collections/new-arrivals")
         page.go_back()

    # def test_new_arrivals_content(self, page: Page):
    #      page.goto("https://ecommerce.datablitz.com.ph/")

    #      newa_img = page.locator("#shopify-section-1590542985479 .product-item").nth(0)
    #      expect(newa_img.locator('.product-item__primary-image')).to_be_visible()
    #      newa_img.hover()
    #      page.wait_for_timeout(500)
    #      expect(newa_img.locator('.product-item__secondary-image')).to_have_count(1)
    #      newa_img.click()
    #      expect (page).to_have_url(re.compile(r"/collections/new-arrivals/products/"))
    #      page.go_back()

        #  expect(newa_img.locator('.price')).to_be_visible

        #  expect(newa_img.locator('.product-item__title')).to_be_visible()
        #  newa_img.locator('.product-item__title').click()
        #  expect (page).to_have_url(re.compile(r"/collections/new-arrivals/products/"))
        #  page.go_back()

    #      newa_img.hover()
    #      page.wait_for_timeout(500)

    #      expect(newa_img.locator('#product_form_id_15412342292851_1590542985479').get_by_role('link', name="Choose options")).to_be_visible()
    #      newa_img.locator('#product_form_id_15412342292851_1590542985479').get_by_role('link', name="Choose options").click()
    #      expect (page).to_have_url(re.compile(r"/collections/new-arrivals/products/"))
    #      page.go_back()

    def test_new_arrivals_iterate(self, page: Page):
         page.goto("https://ecommerce.datablitz.com.ph/")

         LIMIT=6

         count = page.locator("#shopify-section-1590542985479 .product-item").all()

         for i, newa_img in enumerate(count[:LIMIT]):
            #   newa_img = page.locator("#shopify-section-1590542985479 .product-item").nth(i)
              expect(newa_img.locator('.product-item__primary-image')).to_be_visible()
              newa_img.hover()
              page.wait_for_timeout(500)
              expect(newa_img.locator('.product-item__secondary-image')).to_have_count(1)
              newa_img.click()
              expect (page).to_have_url(re.compile(r"/collections/new-arrivals/products/"))
              page.go_back()

              expect(newa_img.locator('.price')).to_be_visible

              expect(newa_img.locator('.product-item__title')).to_be_visible()
              newa_img.locator('.product-item__title').click()
              expect (page).to_have_url(re.compile(r"/collections/new-arrivals/products/"))
              page.go_back()
              print(f"New arrival product {i+1} been tested")