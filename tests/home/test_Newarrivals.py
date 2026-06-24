from playwright.sync_api import Page, expect
import re

class TestDatablitzNewArrivals:

    def test_new_arrivals(self, page: Page):
         page.goto("https://ecommerce.datablitz.com.ph/")

         expect (page.get_by_role("heading", name="New Arrivals")).to_be_visible()

         expect (page.locator("#shopify-section-1590542985479 .section__action-link")).to_be_visible()
         page.locator('#shopify-section-1590542985479 .section__action-link').click()
         expect (page).to_have_url("https://ecommerce.datablitz.com.ph/collections/new-arrivals")
         page.go_back()

    def test_new_arrivals_products(self, page: Page):
         page.goto("https://ecommerce.datablitz.com.ph/")

         LIMIT=6

         product = page.locator("#shopify-section-1590542985479 .product-item").all()

         for i, newa_img in enumerate(product[:LIMIT]):
            #   newa_img = page.locator("#shopify-section-1590542985479 .product-item").nth(i)
              expect(newa_img.locator('.product-item__primary-image')).to_be_visible()
              newa_img.hover()
              page.wait_for_timeout(500)
              expect(newa_img.locator('.product-item__secondary-image')).to_have_count(1)
              
              newa_img.locator('.product-item__image-wrapper').click()
              expect (page).to_have_url(re.compile(r"/collections/new-arrivals/products/"))
              page.go_back()
              print(f"New arrival product image {i+1} been tested")

              expect(newa_img.locator('.price')).to_be_visible()

              expect(newa_img.locator('.product-item__title')).to_be_visible()
              newa_img.locator('.product-item__title').click()
              expect (page).to_have_url(re.compile(r"/collections/new-arrivals/products/"))
              page.go_back()
              print(f"New arrival product {i+1} been tested")

    def test_new_arrivals_buttons(self, page: Page):
         page.goto("https://ecommerce.datablitz.com.ph/")

         product = page.locator("#shopify-section-1590542985479 .product-item").all()

         for i, newa_button in enumerate(product):
                   newa_button.hover()
                   page.wait_for_timeout(500)

                   if newa_button.locator('a[class*="action-button"]').count() > 0:
                        print(f"Choose options {i+1} been tested")
                        expect(newa_button.locator('a[class*="action-button"]')).to_be_visible()
                        newa_button.locator('a[class*="action-button"]').click()
                        expect (page).to_have_url(re.compile(r"/collections/new-arrivals/products/"))
                        page.go_back()
                        page.wait_for_timeout(500)
                        
                   elif newa_button.locator('button[type="submit"]').count() > 0:
                        print(f"Add to cart {i+1} been tested")
                        expect(newa_button.locator('button[type="submit"]')).to_be_visible()
                        expect(newa_button.locator('button[type="submit"]')).to_be_enabled()

                   elif newa_button.locator('button[disabled]').count() > 0:
                        print(f"disabled {i+1} been tested")
                        expect(newa_button.locator('button[disabled]')).to_be_visible()
                        expect(newa_button.locator('button[disabled]')).to_be_disabled()

                   else:
                         print(f"⚠️ Product {i+1}: UNKNOWN button type!")
                         print(newa_button.inner_html()[:500])

    def test_new_arrivals_np_buttons(self, page: Page):
            page.goto("https://ecommerce.datablitz.com.ph/")

            next_button = page.locator("#shopify-section-1590542985479").get_by_role("button", name="Next")
            expect(next_button).to_be_visible()
            next_button.click()

            previous_button = page.locator("#shopify-section-1590542985479").get_by_role("button", name="Previous")
            expect(previous_button).to_be_visible()
            previous_button.click()
