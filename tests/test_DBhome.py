from playwright.sync_api import Page, expect

class TestDatablitzHomepage:

    # def test_home_title(self, page: Page):
    #     page.goto("https://ecommerce.datablitz.com.ph/")
    #     expect (page).to_have_title("DataBlitz - Your Total Gaming and Multimedia Store")

    # def test_home_first_promo_img(self, page: Page):
    #     page.goto("https://ecommerce.datablitz.com.ph/")

    #     expect (page.locator('.promo-block').nth(0)).to_be_visible()
    #     page.locator('.promo-block').nth(0).click()
    #     expect (page).to_have_url("https://ecommerce.datablitz.com.ph/collections/ayaneo")

    # def test_home_second_promo_img(self, page: Page):
    #     page.goto("https://ecommerce.datablitz.com.ph/")

    #     expect (page.locator('.promo-block').nth(1)).to_be_visible()
    #     page.locator('.promo-block').nth(1).click()
    #     expect (page).to_have_url("https://ecommerce.datablitz.com.ph/collections/gpd-handheld-console")

    # def test_home_third_promo_img(self, page: Page):
    #     page.goto("https://ecommerce.datablitz.com.ph/")

    #     expect (page.locator('.promo-block').nth(2)).to_be_visible()
    #     page.locator('.promo-block').nth(2).click()
    #     expect (page).to_have_url("https://ecommerce.datablitz.com.ph/collections/steam-deck-1")

    # def test_home_first_promo_button(self, page: Page):
    #     page.goto("https://ecommerce.datablitz.com.ph/")

    #     expect (page.locator('text=Shop Now!').nth(0)).to_be_visible()
    #     page.locator('text=Shop Now!').nth(0).click()
    #     expect (page).to_have_url("https://ecommerce.datablitz.com.ph/collections/ayaneo")

    # def test_home_second_promo_button(self, page: Page):
    #     page.goto("https://ecommerce.datablitz.com.ph/")

    #     expect (page.locator('text=Shop Now!').nth(1)).to_be_visible()
    #     page.locator('text=Shop Now!').nth(1).click()
    #     expect (page).to_have_url("https://ecommerce.datablitz.com.ph/collections/gpd-handheld-console")

    # def test_home_third_promo_button(self, page: Page):
    #     page.goto("https://ecommerce.datablitz.com.ph/")

    #     expect (page.locator('text=Shop Now!').nth(2)).to_be_visible()
    #     page.locator('text=Shop Now!').nth(2).click()
    #     expect (page).to_have_url("https://ecommerce.datablitz.com.ph/collections/steam-deck-1")

    # def test_home_begin_content(self, page: Page):
    #     page.goto("https://ecommerce.datablitz.com.ph/")

    #     expect (page.locator("#shopify-section-16428086583d0db429").get_by_alt_text('Your Most Trusted DataBlitz Store')).to_be_visible()
    #     expect (page.locator("#shopify-section-16428086583d0db429").get_by_text('Your Most Trusted DataBlitz Store')).to_be_visible()
    #     expect (page.locator("#shopify-section-16428086583d0db429").get_by_text('100% All Brand New & Original. Shop with confidence!')).to_be_visible()

    #     expect (page.locator("#shopify-section-16428086583d0db429").get_by_text('Fast Shipping Nationwide')).to_be_visible()
    #     expect (page.locator("#shopify-section-16428086583d0db429").get_by_text('Ships in 24 hours! Express and Same-Day Delivery within Metro Manila!')).to_be_visible()

    #     expect (page.locator("#shopify-section-16428086583d0db429").get_by_text('Save on Loyalty Rewards')).to_be_visible()
    #     expect (page.locator("#shopify-section-16428086583d0db429").get_by_text('Sign in to start earning Loyalty Rewards Points!')).to_be_visible()

    #     expect (page.locator("#shopify-section-16428086583d0db429").get_by_text('100% Safe and Secure')).to_be_visible()
    #     expect (page.locator("#shopify-section-16428086583d0db429").get_by_text('All Transactions are Fully Encrypted with State of the Art Technology!')).to_be_visible()

    def test_home_hot_picks(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/")

        expect (page.get_by_role("heading", name="Hot Picks")).to_be_visible()

        #46 hot picks images with next and previous buttons
        # def test_hot_picks_nextb(self, page: Page):
        #     page.goto("https://ecommerce.datablitz.com.ph/")

        #     expect (page.get_by_role('{aria-label="Next"}').click())

    def test_hot_picks_lists(self, page: Page):
         page.goto("https://ecommerce.datablitz.com.ph/")

         #game covers

    def test_hot_picks_nextb(self, page: Page):
            page.goto("https://ecommerce.datablitz.com.ph/")

            # page.locator("#shopify-section-1584623859185").get_by_role("button", name="Next").click()

            next_button = page.locator("#shopify-section-1584623859185").get_by_role("button", name="Next")
            expect(next_button).to_be_visible()
            next_button.click()
        
