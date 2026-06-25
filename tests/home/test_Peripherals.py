from playwright.sync_api import Page, expect
import re

class TestDatablitzPeripherals:

    def test_featured_computer_peripherals(self, page: Page):
            page.goto("https://ecommerce.datablitz.com.ph/")

            expect (page.get_by_role("heading", name="Featured Computer Peripherals & Accessories")).to_be_visible()

            expect (page.locator("#shopify-section-161666667899e763df").get_by_text("View all ")).to_be_visible()
            page.locator('#shopify-section-161666667899e763df').get_by_text("View all ").click()
            expect (page).to_have_url("https://ecommerce.datablitz.com.ph/collections/featured-computer-peripherals")
            page.go_back()

    def test_featured_computer_peripherals_products(self, page: Page):
            page.goto("https://ecommerce.datablitz.com.ph/")

            product = page.locator("#shopify-section-161666667899e763df .product-item").count()

            for i in range(product):
              peripherals_product = page.locator("#shopify-section-161666667899e763df .product-item").nth(i)
              expect(peripherals_product.locator('.product-item__primary-image')).to_be_visible()
              peripherals_product.hover()
              page.wait_for_timeout(500)
              expect(peripherals_product.locator('.product-item__secondary-image')).to_have_count(1)
              peripherals_product.locator('.product-item__image-wrapper').click()
              expect (page).to_have_url(re.compile(r"/products/"))
              page.go_back()

              if peripherals_product.locator(".product-label").count() > 0:
                    expect (peripherals_product.locator('.product-label')).to_be_visible()
                    expect (peripherals_product.locator('.price--highlight')).to_be_visible()
                    expect (peripherals_product.locator('.price--compare')).to_be_visible()
                    print(f"Computer peripherals product {i+1} has a label")

              else:
                    expect(peripherals_product.locator('.price')).to_be_visible()
                    print(f"Computer peripherals {i+1} has a price")

              expect(peripherals_product.locator('.product-item__title')).to_be_visible()
              peripherals_product.locator('.product-item__title').click()
              expect (page).to_have_url(re.compile(r"/products/"))
              page.go_back()
              print(f"Featured computer peripherals {i+1} been tested")

    def test_computer_peripherals_buttons(self, page: Page):
            page.goto("https://ecommerce.datablitz.com.ph/")

            next_button = page.locator("#shopify-section-161666667899e763df").get_by_role("button", name="Next")
            expect(next_button).to_be_visible()
            next_button.click()

            previous_button = page.locator("#shopify-section-161666667899e763df").get_by_role("button", name="Previous")
            expect(previous_button).to_be_visible()
            previous_button.click()

    def test_peripherals_collections(self, page: Page):
          page.goto("https://ecommerce.datablitz.com.ph/")
          
          peripherals_accessories = page.locator("#shopify-section-1590416962605 .promo-block").count()

          for i in range(peripherals_accessories):
                product = page.locator("#shopify-section-1590416962605 .promo-block").nth(i)

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
                print(f"Product peripherals & accessories {i+1} been tested")

    def test_peripherals_collections_extend(self, page: Page):
         page.goto("https://ecommerce.datablitz.com.ph/")

         peripherals_accessories = page.locator("#shopify-section-68a94125-6c7a-4f7d-bec8-e60f4da85b01 .collection-item").count()

         for i in range(peripherals_accessories):
               product = page.locator("#shopify-section-68a94125-6c7a-4f7d-bec8-e60f4da85b01 .collection-item").nth(i)
               expect (product.locator('.collection-item__image-wrapper ')).to_be_visible()
               product.hover()
               page.wait_for_timeout(500)
               product.click()

               expect (page).to_have_url(re.compile(r"/collections/"))
               page.go_back()
               print(f"Extended peripherals collections {i+1} tested")

    def test_browse_peripherals_title(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/")

        expect (page.get_by_role("heading", name="Browse by Peripherals/ Accessories Type")).to_be_visible()

    def test_browse_peripherals_list(self, page: Page):
         page.goto("https://ecommerce.datablitz.com.ph/")

         peripheral_picks = page.locator("#shopify-section-collection_list_r7K9Gm .collection-item").count()

         for i in range(peripheral_picks):
               list = page.locator("#shopify-section-collection_list_r7K9Gm .collection-item").nth(i)
               expect (list.locator('.collection-item__image-wrapper ')).to_be_visible()
               list.hover()
               page.wait_for_timeout(500)
               list.click()
               expect (page).to_have_url(re.compile(r"/collections/"))
               page.go_back()
               print(f"Product peripherals {i+1} tested")

    def test_browse_peripherals_buttons(self, page: Page):
            page.goto("https://ecommerce.datablitz.com.ph/")

            next_button = page.locator("#shopify-section-collection_list_r7K9Gm").get_by_role("button", name="Next")
            expect(next_button).to_be_visible()
            next_button.click()

            previous_button = page.locator("#shopify-section-collection_list_r7K9Gm").get_by_role("button", name="Previous")
            expect(previous_button).to_be_visible()
            previous_button.click()
