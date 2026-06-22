from playwright.sync_api import Page, expect
import re

class TestDatablitzHomepage:

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

    def test_hot_picks_buttons(self, page: Page):
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
              newa_img.click()
              expect (page).to_have_url(re.compile(r"/collections/new-arrivals/products/"))
              page.go_back()

              expect(newa_img.locator('.price')).to_be_visible

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

    def test_new_arrivals_buttons(self, page: Page):
            page.goto("https://ecommerce.datablitz.com.ph/")

            next_button = page.locator("#shopify-section-1590542985479").get_by_role("button", name="Next")
            expect(next_button).to_be_visible()
            next_button.click()

            previous_button = page.locator("#shopify-section-1590542985479").get_by_role("button", name="Previous")
            expect(previous_button).to_be_visible()
            previous_button.click()

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

    def test_game_promos(self, page: Page):
          page.goto("https://ecommerce.datablitz.com.ph/")
          
          promo_games = page.locator("#shopify-section-1587182738805 .promo-block").count()

          for i in range(promo_games):
                product = page.locator("#shopify-section-1587182738805 .promo-block").nth(i)
                expect (product.locator('.promo-block__heading')).to_be_visible()

                expect (product.locator('.promo-block__image-wrapper')).to_be_visible()
                product.locator('.promo-block__image-wrapper').click()
                expect (page).to_have_url(re.compile(r"/collections/"))
                page.go_back()

                expect (product.locator('.promo-block__cta')).to_be_visible()
                product.locator('.promo-block__cta').click()
                expect (page).to_have_url(re.compile(r"/collections/"))
                page.go_back()
                print(f"Game promo product {i+1} been tested")
