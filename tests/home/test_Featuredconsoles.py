from playwright.sync_api import Page, expect
import re

class TestDatablitzFeaturedConsoles:

    def test_featured_consoles(self, page: Page):
            page.goto("https://ecommerce.datablitz.com.ph/")

            expect (page.get_by_role("heading", name="Featured Gaming Consoles")).to_be_visible()

            expect (page.locator("#shopify-section-1616576385b0defc44").get_by_text("View all ")).to_be_visible()
            page.locator('#shopify-section-1616576385b0defc44').get_by_text("View all ").click()
            expect (page).to_have_url("https://ecommerce.datablitz.com.ph/collections/featured-gaming-consoles")
            page.go_back()

    def test_featured_consoles_products(self, page: Page):
            page.goto("https://ecommerce.datablitz.com.ph/")

            # LIMIT=6

            product = page.locator("#shopify-section-1616576385b0defc44 .product-item").count()

            for i in range(product):
              featuredc_product = page.locator("#shopify-section-1616576385b0defc44 .product-item").nth(i)
              expect(featuredc_product.locator('.product-item__primary-image')).to_be_visible()
              featuredc_product.hover()
              page.wait_for_timeout(500)
              expect(featuredc_product.locator('.product-item__secondary-image')).to_have_count(1)
              featuredc_product.click()
              expect (page).to_have_url(re.compile(r"/products/"))
              page.go_back()

              if featuredc_product.locator(".product-label").count() > 0:
                    expect (featuredc_product.locator('.product-label')).to_be_visible()
                    expect (featuredc_product.locator('.price--highlight')).to_be_visible()
                    expect (featuredc_product.locator('.price--compare')).to_be_visible()
                    print(f"Product {i+1} has a label")

              else:
                    expect(featuredc_product.locator('.price')).to_be_visible()
                    print(f"Product {i+1} has a price")

              expect(featuredc_product.locator('.product-item__title')).to_be_visible()
              featuredc_product.locator('.product-item__title').click()
              expect (page).to_have_url(re.compile(r"/products/"))
              page.go_back()
              print(f"Featured consoles product {i+1} been tested")

    def test_featured_consoles_buttons(self, page: Page):
            page.goto("https://ecommerce.datablitz.com.ph/")

            next_button = page.locator("#shopify-section-1616576385b0defc44").get_by_role("button", name="Next")
            next_button.hover()
            page.wait_for_timeout(500)
            expect(next_button).to_be_visible()
            next_button.click()

            previous_button = page.locator("#shopify-section-1616576385b0defc44").get_by_role("button", name="Previous")
            next_button.hover()
            page.wait_for_timeout(500)
            expect(previous_button).to_be_visible()
            previous_button.click()
