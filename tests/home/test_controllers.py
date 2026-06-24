from playwright.sync_api import Page, expect
import re

class TestDatablitzControllers:

    def test_device_promos(self, page: Page):
          page.goto("https://ecommerce.datablitz.com.ph/")
          
          promo_devices = page.locator("#shopify-section-1595996575693 .promo-block").count()

          for i in range(promo_devices):
                product = page.locator("#shopify-section-1595996575693 .promo-block").nth(i)

                expect (product.locator('.promo-block__image-wrapper')).to_be_visible()
                product.locator('.promo-block__image-wrapper').click()

                url = page.url

                if "/pages/" in url:
                     print(f"Pages URL {i+1} found")

                elif "/collections/" in url:
                     print(f"Collections URL {i+1} found")

                else:
                    print(f"⚠️ {i+1}: UNKNOWN URL!")

                page.go_back()

                expect (product.locator('.promo-block__cta')).to_be_visible()
                product.locator('.promo-block__cta').click()
                
                if "/pages/" in url:
                     print(f"Pages URL {i+1} found(Button)")

                elif "/collections/" in url:
                     print(f"Collections URL {i+1} found(Button)")

                else:
                    print(f"⚠️ {i+1}: UNKNOWN URL!")

                page.go_back()
                print(f"Game promo product {i+1} been tested")

    def test_device_promos_extend(self, page: Page):
         page.goto("https://ecommerce.datablitz.com.ph/")

         promo_devices = page.locator("#shopify-section-collection_list_rhNkPm .collection-item").count()

         for i in range(promo_devices):
               product = page.locator("#shopify-section-collection_list_rhNkPm .collection-item").nth(i)
               expect (product.locator('.collection-item__image-wrapper ')).to_be_visible()
               product.hover()
               page.wait_for_timeout(500)
               product.click()

               expect (page).to_have_url(re.compile(r"/collections/"))
               page.go_back()
               print(f"Extended device promo product {i+1} tested")
