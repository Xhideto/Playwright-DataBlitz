from playwright.sync_api import Page, expect
import re

class TestDatablitzAccesories:

    def test_featured_console_accesories(self, page: Page):
            page.goto("https://ecommerce.datablitz.com.ph/")

            expect (page.get_by_role("heading", name="Featured Console Accessories")).to_be_visible()

            expect (page.locator("#shopify-section-16166609178585f189").get_by_text("View all ")).to_be_visible()
            page.locator('#shopify-section-16166609178585f189').get_by_text("View all ").click()
            expect (page).to_have_url("https://ecommerce.datablitz.com.ph/collections/featured-console-accessories")
            page.go_back()

    def test_featured_console_accesories_products(self, page: Page):
            page.goto("https://ecommerce.datablitz.com.ph/")

            product = page.locator("#shopify-section-16166609178585f189 .product-item").count()

            for i in range(product):
              accesories_product = page.locator("#shopify-section-16166609178585f189 .product-item").nth(i)
              expect(accesories_product.locator('.product-item__primary-image')).to_be_visible()
              accesories_product.hover()
              page.wait_for_timeout(500)
              expect(accesories_product.locator('.product-item__secondary-image')).to_have_count(1)
              accesories_product.locator('.product-item__image-wrapper').click()
              expect (page).to_have_url(re.compile(r"/products/"))
              page.go_back()

              if accesories_product.locator(".product-label").count() > 0:
                    expect (accesories_product.locator('.product-label')).to_be_visible()
                    expect (accesories_product.locator('.price--highlight')).to_be_visible()
                    expect (accesories_product.locator('.price--compare')).to_be_visible()
                    print(f"Console accesories product {i+1} has a label")

              else:
                    expect(accesories_product.locator('.price')).to_be_visible()
                    print(f"Console accesories {i+1} has a price")

              expect(accesories_product.locator('.product-item__title')).to_be_visible()
              accesories_product.locator('.product-item__title').click()
              expect (page).to_have_url(re.compile(r"/products/"))
              page.go_back()
              print(f"Featured console accesories {i+1} been tested")

    def test_console_accesories_buttons(self, page: Page):
            page.goto("https://ecommerce.datablitz.com.ph/")

            next_button = page.locator("#shopify-section-16166609178585f189").get_by_role("button", name="Next")
            expect(next_button).to_be_visible()
            next_button.click()

            previous_button = page.locator("#shopify-section-16166609178585f189").get_by_role("button", name="Previous")
            expect(previous_button).to_be_visible()
            previous_button.click()

    def test_driving_collections(self, page: Page):
          page.goto("https://ecommerce.datablitz.com.ph/")
          
          driving_devices = page.locator("#shopify-section-1616669569682cb82c .promo-block").count()

          for i in range(driving_devices):
                product = page.locator("#shopify-section-1616669569682cb82c .promo-block").nth(i)

                expect (product.locator('.promo-block__image-wrapper')).to_be_visible()
                product.hover()
                page.wait_for_timeout(500)
                product.locator('.promo-block__image-wrapper').click()
                expect (page).to_have_url(re.compile(r"/collections/"))

                page.go_back()

                expect (product.locator('.promo-block__cta')).to_be_visible()
                product.locator('.promo-block__cta').click()
                expect (page).to_have_url(re.compile(r"/collections/"))

                page.go_back()
                print(f"Game promo product {i+1} been tested")
