from playwright.sync_api import Page, expect
import re

class TestDatablitzHomeBeginContent:

    def test_home_title(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/")
        expect (page).to_have_title("DataBlitz - Your Total Gaming and Multimedia Store")

    def test_home_slideshow_dot_visible(self, page: Page):
          page.goto("https://ecommerce.datablitz.com.ph/")

          dots = page.locator('#shopify-section-slideshow .dot').count()
          assert dots > 0, "No dots found"
          print(f"{dots} slideshow dots found")
          expect (page.locator('.dot').first).to_be_visible()

    def test_home_slideshow_dot_click(self, page: Page):
          page.goto("https://ecommerce.datablitz.com.ph/")

          dots = page.locator('#shopify-section-slideshow .dot').count()
        
          for i in range(dots):
                dot = page.locator('#shopify-section-slideshow .dot').nth(i)
                dot.click()
                page.wait_for_timeout(500)

                expect (dot).to_have_class(re.compile(r"is-selected"))
                print(f"Slideshow dot {i+1} is selected")

    def test_home_slideshow_banners(self, page: Page):
          page.goto("https://ecommerce.datablitz.com.ph/")

          slides = page.locator('#shopify-section-slideshow .slideshow__slide').count()

          for i in range(slides):
                page.goto("https://ecommerce.datablitz.com.ph/")

                dot = page.locator('#shopify-section-slideshow .dot').nth(i)
                dot.click()
                page.wait_for_timeout(500)

                slide = page.locator('#shopify-section-slideshow .slideshow__slide').nth(i)
                expect (slide).to_be_visible()

                slide.hover()
                slide.click()
                page.wait_for_timeout(500)

                url = page.url

                if "/pages/" in url:
                      print(f"{url} {i+1} checked")

                elif "/collections/" in url:
                      print(f"{url} {i+1} checked")

                elif "/products/" in url:
                      page.go_back()
                      print(f"{url} {i+1} checked")

                else:
                    print(f"⚠️ {i+1}: UNKNOWN URL!")

                page.go_back()

    def test_device_promos(self, page: Page):
          page.goto("https://ecommerce.datablitz.com.ph/")
          
          promo_devices = page.locator("#shopify-section-1584758974956 .promo-block").count()

          for i in range(promo_devices):
                product = page.locator("#shopify-section-1584758974956 .promo-block").nth(i)

                expect (product.locator('.promo-block__image-wrapper')).to_be_visible()
                product.locator('.promo-block__image-wrapper').click()
                expect (page).to_have_url(re.compile(r"/collections/"))
                page.go_back()

                expect (product.locator('.promo-block__cta')).to_be_visible()
                product.locator('.promo-block__cta').click()
                expect (page).to_have_url(re.compile(r"/collections/"))
                page.go_back()
                print(f"Game promo product {i+1} been tested")

    def test_home_scnd_slideshow_dot_visible(self, page: Page):
          page.goto("https://ecommerce.datablitz.com.ph/")

          dots = page.locator('#shopify-section-16643330685e2168b4 .dot').count()
          assert dots > 0, "No dots found"
          print(f"{dots} slideshow dots found")
          expect (page.locator('.dot').first).to_be_visible()

    def test_home_scnd_slideshow_dot_click(self, page: Page):
          page.goto("https://ecommerce.datablitz.com.ph/")

          dots = page.locator('#shopify-section-16643330685e2168b4 .dot').count()
        
          for i in range(dots):
                dot = page.locator('#shopify-section-16643330685e2168b4 .dot').nth(i)
                dot.click()
                page.wait_for_timeout(500)

                expect (dot).to_have_class(re.compile(r"is-selected"))
                print(f"Slideshow dot {i+1} is selected")

    def test_home_scnd_slideshow_banners(self, page: Page):
          page.goto("https://ecommerce.datablitz.com.ph/")

          slides = page.locator('#shopify-section-16643330685e2168b4 .slideshow__slide').count()

          for i in range(slides):
                page.goto("https://ecommerce.datablitz.com.ph/")

                dot = page.locator('#shopify-section-16643330685e2168b4 .dot').nth(i)
                dot.click()
                page.wait_for_timeout(500)

                slide = page.locator('#shopify-section-16643330685e2168b4 .slideshow__slide').nth(i)
                expect (slide).to_be_visible()

                slide.hover()
                slide.click()
                page.wait_for_timeout(500)

                url = page.url

                if "/pages/" in url:
                      print(f"{url} {i+1} checked")

                elif "/collections/" in url:
                      print(f"{url} {i+1} checked")

                elif "/products/" in url:
                      page.go_back()
                      print(f"{url} {i+1} checked")

                else:
                    print(f"⚠️ {i+1}: UNKNOWN URL!")

                page.go_back()

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
