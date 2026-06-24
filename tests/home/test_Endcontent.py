from playwright.sync_api import Page, expect

class TestDatablitzEndContent:

    def test_home_title(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/")
        expect (page).to_have_title("DataBlitz - Your Total Gaming and Multimedia Store")

    def test_home_end_content(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/")

        expect (page.locator("#shopify-section-static-text-with-icons").get_by_text('Your Most Trusted DataBlitz Store')).to_be_visible()
        expect (page.locator("#shopify-section-static-text-with-icons").get_by_text('100% All Brand New & Original. Shop with confidence!')).to_be_visible()

        expect (page.locator("#shopify-section-static-text-with-icons").get_by_text('Fast Shipping Nationwide')).to_be_visible()
        expect (page.locator("#shopify-section-static-text-with-icons").get_by_text('Ships in 24 hours! Express and Same-Day Delivery within Metro Manila!')).to_be_visible()

        expect (page.locator("#shopify-section-static-text-with-icons").get_by_text('Save on Loyalty Rewards')).to_be_visible()
        expect (page.locator("#shopify-section-static-text-with-icons").get_by_text('Sign in to start earning Loyalty Rewards Points!')).to_be_visible()

        expect (page.locator("#shopify-section-static-text-with-icons").get_by_text('100% Safe and Secure')).to_be_visible()
        expect (page.locator("#shopify-section-static-text-with-icons").get_by_text('All Transactions are Fully Encrypted with State of the Art Technology!')).to_be_visible()
