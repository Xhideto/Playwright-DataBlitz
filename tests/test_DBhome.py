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

         hot_picks = page.locator("#shopify-section-1584623859185 .collection-item").count()

         for i in range(hot_picks):
               list = page.locator("#shopify-section-1584623859185 .collection-item").nth(i)
               expect (list.locator('.collection-item__image-wrapper ')).to_be_visible()
               list.hover()
               page.wait_for_timeout(500)
               list.click()
               expect (page).to_have_url(re.compile(r"/collections/"))
               page.go_back()
               print(f"Hot picks product {i+1} tested")


      #    page.locator("#shopify-section-1584623859185 .collection-item").nth(0).click()
      #    page.go_back()
      #    page.locator("#shopify-section-1584623859185 .collection-item").nth(1).click()
      #    page.go_back()
      #    page.locator("#shopify-section-1584623859185 .collection-item").nth(2).click()
      #    page.go_back()
      #    page.locator("#shopify-section-1584623859185 .collection-item").nth(3).click()
      #    page.go_back()
      #    page.locator("#shopify-section-1584623859185 .collection-item").nth(4).click()
      #    page.go_back()
      #    page.locator("#shopify-section-1584623859185 .collection-item").nth(5).click()
      #    expect (page).to_have_url(re.compile(r"/collections/"))

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

    def test_featured_switch(self, page: Page):
            page.goto("https://ecommerce.datablitz.com.ph/")

            expect (page.get_by_role("heading", name="Featured Nintendo Switch Games")).to_be_visible()

            expect (page.locator("#shopify-section-1616581165983c351d").get_by_text("View all ")).to_be_visible()
            page.locator('#shopify-section-1616581165983c351d').get_by_text("View all ").click()
            expect (page).to_have_url("https://ecommerce.datablitz.com.ph/collections/featured-nintendo-switch-games")
            page.go_back()

    def test_featured_switch_products(self, page: Page):
            page.goto("https://ecommerce.datablitz.com.ph/")

            product = page.locator("#shopify-section-1616581165983c351d .product-item").count()

            for i in range(product):
              switch_product = page.locator("#shopify-section-1616581165983c351d .product-item").nth(i)
              expect(switch_product.locator('.product-item__primary-image')).to_be_visible()
              switch_product.hover()
              page.wait_for_timeout(500)
              expect(switch_product.locator('.product-item__secondary-image')).to_have_count(1)
              switch_product.click()
              expect (page).to_have_url(re.compile(r"/products/"))
              page.go_back()

              if switch_product.locator(".product-label").count() > 0:
                    expect (switch_product.locator('.product-label')).to_be_visible()
                    expect (switch_product.locator('.price--highlight')).to_be_visible()
                    expect (switch_product.locator('.price--compare')).to_be_visible()
                    print(f"Switch product {i+1} has a label")

              else:
                    expect(switch_product.locator('.price')).to_be_visible()
                    print(f"Switch product {i+1} has a price")

              expect(switch_product.locator('.product-item__title')).to_be_visible()
              switch_product.locator('.product-item__title').click()
              expect (page).to_have_url(re.compile(r"/products/"))
              page.go_back()
              print(f"Featured switch product {i+1} been tested")

    def test_featured_playstation(self, page: Page):
            page.goto("https://ecommerce.datablitz.com.ph/")

            expect (page.get_by_role("heading", name="Featured PlayStation Games")).to_be_visible()

            expect (page.locator("#shopify-section-1616582529b9e27459").get_by_text("View all ")).to_be_visible()
            page.locator('#shopify-section-1616582529b9e27459').get_by_text("View all ").click()
            expect (page).to_have_url("https://ecommerce.datablitz.com.ph/collections/featured-playstation-games")
            page.go_back()

    def test_featured_playstation_products(self, page: Page):
            page.goto("https://ecommerce.datablitz.com.ph/")

            product = page.locator("#shopify-section-1616582529b9e27459 .product-item").count()

            for i in range(product):
              playstation_product = page.locator("#shopify-section-1616582529b9e27459 .product-item").nth(i)
              expect(playstation_product.locator('.product-item__primary-image')).to_be_visible()
              playstation_product.hover()
              page.wait_for_timeout(500)
              expect(playstation_product.locator('.product-item__secondary-image')).to_have_count(1)
              playstation_product.click()
              expect (page).to_have_url(re.compile(r"/products/"))
              page.go_back()

              if playstation_product.locator(".product-label").count() > 0:
                    expect (playstation_product.locator('.product-label')).to_be_visible()
                    expect (playstation_product.locator('.price--highlight')).to_be_visible()
                    expect (playstation_product.locator('.price--compare')).to_be_visible()
                    print(f"Playstation product {i+1} has a label")

              else:
                    expect(playstation_product.locator('.price')).to_be_visible()
                    print(f"Playstation product {i+1} has a price")

              expect(playstation_product.locator('.product-item__title')).to_be_visible()
              playstation_product.locator('.product-item__title').click()
              expect (page).to_have_url(re.compile(r"/products/"))
              page.go_back()
              print(f"Featured playstation product {i+1} been tested")

    def test_featured_xbox(self, page: Page):
            page.goto("https://ecommerce.datablitz.com.ph/")

            expect (page.get_by_role("heading", name="Featured Xbox Games")).to_be_visible()

            expect (page.locator("#shopify-section-1616585015028b7de4").get_by_text("View all ")).to_be_visible()
            page.locator('#shopify-section-1616585015028b7de4').get_by_text("View all ").click()
            expect (page).to_have_url("https://ecommerce.datablitz.com.ph/collections/featured-xbox-games")
            page.go_back()

    def test_featured_xbox_products(self, page: Page):
            page.goto("https://ecommerce.datablitz.com.ph/")

            product = page.locator("#shopify-section-1616585015028b7de4 .product-item").count()

            for i in range(product):
              xbox_product = page.locator("#shopify-section-1616585015028b7de4 .product-item").nth(i)
              expect(xbox_product.locator('.product-item__primary-image')).to_be_visible()
              xbox_product.hover()
              page.wait_for_timeout(500)
              expect(xbox_product.locator('.product-item__secondary-image')).to_have_count(1)
              xbox_product.click()
              expect (page).to_have_url(re.compile(r"/products/"))
              page.go_back()

              if xbox_product.locator(".product-label").count() > 0:
                    expect (xbox_product.locator('.product-label')).to_be_visible()
                    expect (xbox_product.locator('.price--highlight')).to_be_visible()
                    expect (xbox_product.locator('.price--compare')).to_be_visible()
                    print(f"Xbox product {i+1} has a label")

              else:
                    expect(xbox_product.locator('.price')).to_be_visible()
                    print(f"Xbox product {i+1} has a price")

              expect(xbox_product.locator('.product-item__title')).to_be_visible()
              xbox_product.locator('.product-item__title').click()
              expect (page).to_have_url(re.compile(r"/products/"))
              page.go_back()
              print(f"Featured xbox product {i+1} been tested")

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
              accesories_product.click()
              expect (page).to_have_url(re.compile(r"/collections/"))
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
              expect (page).to_have_url(re.compile(r"/collections/"))
              page.go_back()
              print(f"Featured console accesories {i+1} been tested")

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
              peripherals_product.click()
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

    def test_peripherals_collections(self, page: Page):
          page.goto("https://ecommerce.datablitz.com.ph/")
          
          peripherals_accesories = page.locator("#shopify-section-1590416962605 .promo-block").count()

          for i in range(peripherals_accesories):
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
                print(f"Product peripherals & accesories {i+1} been tested")

    def test_peripherals_collections_extend(self, page: Page):
         page.goto("https://ecommerce.datablitz.com.ph/")

         peripherals_accesories = page.locator("#shopify-section-68a94125-6c7a-4f7d-bec8-e60f4da85b01 .collection-item").count()

         for i in range(peripherals_accesories):
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

    def test_featured_gaming_monitors(self, page: Page):
            page.goto("https://ecommerce.datablitz.com.ph/")

            expect (page.get_by_role("heading", name="Featured Gaming Monitors")).to_be_visible()

            expect (page.locator("#shopify-section-1616674842433edc70").get_by_text("View all ")).to_be_visible()
            page.locator('#shopify-section-1616674842433edc70').get_by_text("View all ").click()
            expect (page).to_have_url("https://ecommerce.datablitz.com.ph/collections/featured-gaming-monitors")
            page.go_back()

    def test_featured_gaming_monitors_products(self, page: Page):
            page.goto("https://ecommerce.datablitz.com.ph/")

            product = page.locator("#shopify-section-1616674842433edc70 .product-item").count()

            for i in range(product):
              monitors_product = page.locator("#shopify-section-1616674842433edc70 .product-item").nth(i)
              expect(monitors_product.locator('.product-item__primary-image')).to_be_visible()
              monitors_product.hover()
              page.wait_for_timeout(500)
              expect(monitors_product.locator('.product-item__secondary-image')).to_have_count(1)
              monitors_product.click()
              expect (page).to_have_url(re.compile(r"/collections/featured-gaming-monitors/products/"))
              page.go_back()

              if monitors_product.locator(".product-label").count() > 0:
                    expect (monitors_product.locator('.product-label')).to_be_visible()
                    expect (monitors_product.locator('.price--highlight')).to_be_visible()
                    expect (monitors_product.locator('.price--compare')).to_be_visible()
                    print(f"Product gaming monitor {i+1} has a label")

              else:
                    expect(monitors_product.locator('.price')).to_be_visible()
                    print(f"Product gaming monitor {i+1} has a price")

              expect(monitors_product.locator('.product-item__title')).to_be_visible()
              monitors_product.locator('.product-item__title').click()
              expect (page).to_have_url(re.compile(r"/collections/featured-gaming-monitors/products/"))
              page.go_back()
              print(f"Featured gaming monitor {i+1} been tested")

    def test_browse_gaming_monitors_buttons(self, page: Page):
            page.goto("https://ecommerce.datablitz.com.ph/")

            next_button = page.locator("#shopify-section-1616674842433edc70").get_by_role("button", name="Next")
            expect(next_button).to_be_visible()
            next_button.click()

            previous_button = page.locator("#shopify-section-1616674842433edc70").get_by_role("button", name="Previous")
            expect(previous_button).to_be_visible()
            previous_button.click()

    def test_home_slideshow_dot_visible(self, page: Page):
          page.goto("https://ecommerce.datablitz.com.ph/")

          dots = page.locator('#shopify-section-162729501951418af1 .dot').count()
          assert dots > 0, "No dots found"
          print(f"{dots} slideshow dots found")
          expect (page.locator('.dot').first).to_be_visible()

    def test_home_slideshow_dot_click(self, page: Page):
          page.goto("https://ecommerce.datablitz.com.ph/")

          dots = page.locator('#shopify-section-162729501951418af1 .dot').count()
        
          for i in range(dots):
                dot = page.locator('#shopify-section-162729501951418af1 .dot').nth(i)
                dot.click()
                page.wait_for_timeout(500)

                expect (dot).to_have_class(re.compile(r"is-selected"))
                print(f"Slideshow dot {i+1} is selected")

    def test_home_slideshow_banners(self, page: Page):
          page.goto("https://ecommerce.datablitz.com.ph/")

          slides = page.locator('#shopify-section-162729501951418af1 .slideshow__slide').count()

          for i in range(slides):
                page.goto("https://ecommerce.datablitz.com.ph/")

                dot = page.locator('#shopify-section-162729501951418af1 .dot').nth(i)
                dot.click()
                page.wait_for_timeout(500)

                slide = page.locator('#shopify-section-162729501951418af1 .slideshow__slide').nth(i)
                expect (slide).to_be_visible()

                slide.hover()
                page.wait_for_timeout(500)
                slide.click()
                expect (page).to_have_url(re.compile(r"/collections/"))

                page.go_back()

    def test_featured_laptops(self, page: Page):
            page.goto("https://ecommerce.datablitz.com.ph/")

            expect (page.get_by_role("heading", name="Featured Laptops")).to_be_visible()

            expect (page.locator("#shopify-section-16167331070cdccb23").get_by_text("View all ")).to_be_visible()
            page.locator('#shopify-section-16167331070cdccb23').get_by_text("View all ").click()
            expect (page).to_have_url("https://ecommerce.datablitz.com.ph/collections/featured-laptops")
            page.go_back()

    def test_featured_laptops_products(self, page: Page):
            page.goto("https://ecommerce.datablitz.com.ph/")

            product = page.locator("#shopify-section-16167331070cdccb23 .product-item").count()

            for i in range(product):
              laptops_product = page.locator("#shopify-section-16167331070cdccb23 .product-item").nth(i)
              expect(laptops_product.locator('.product-item__primary-image')).to_be_visible()
              laptops_product.hover()
              page.wait_for_timeout(500)
              expect(laptops_product.locator('.product-item__secondary-image')).to_have_count(1)
              laptops_product.click()
              expect (page).to_have_url(re.compile(r"/products/"))
              page.go_back()

              if laptops_product.locator(".product-label").count() > 0:
                    expect (laptops_product.locator('.product-label')).to_be_visible()
                    expect (laptops_product.locator('.price--highlight')).to_be_visible()
                    expect (laptops_product.locator('.price--compare')).to_be_visible()
                    print(f"Product laptop {i+1} has a label")

              else:
                    expect(laptops_product.locator('.price')).to_be_visible()
                    print(f"Product laptop {i+1} has a price")

              expect(laptops_product.locator('.product-item__title')).to_be_visible()
              laptops_product.locator('.product-item__title').click()
              expect (page).to_have_url(re.compile(r"/products/"))
              page.go_back()
              print(f"Featured laptop {i+1} been tested")

    def test_featured_pc_parts(self, page: Page):
            page.goto("https://ecommerce.datablitz.com.ph/")

            expect (page.get_by_role("heading", name="Featured PC Parts & Components")).to_be_visible()

            expect (page.locator("#shopify-section-16643318579a4c7d0a").get_by_text("View all ")).to_be_visible()
            page.locator('#shopify-section-16643318579a4c7d0a').get_by_text("View all ").click()
            expect (page).to_have_url("https://ecommerce.datablitz.com.ph/collections/featured-pc-parts-components")
            page.go_back()

    def test_featured_pc_parts_products(self, page: Page):
            page.goto("https://ecommerce.datablitz.com.ph/")

            product = page.locator("#shopify-section-16643318579a4c7d0a .product-item").count()

            for i in range(product):
              parts_product = page.locator("#shopify-section-16643318579a4c7d0a .product-item").nth(i)
              expect(parts_product.locator('.product-item__primary-image')).to_be_visible()
              parts_product.hover()
              page.wait_for_timeout(500)
              expect(parts_product.locator('.product-item__secondary-image')).to_have_count(1)
              parts_product.click()
              expect (page).to_have_url(re.compile(r"/products/"))
              page.go_back()

              if parts_product.locator(".product-label").count() > 0:
                    expect (parts_product.locator('.product-label')).to_be_visible()
                    expect (parts_product.locator('.price--highlight')).to_be_visible()
                    expect (parts_product.locator('.price--compare')).to_be_visible()
                    print(f"Product PC parts {i+1} has a label")

              else:
                    expect(parts_product.locator('.price')).to_be_visible()
                    print(f"Product PC parts {i+1} has a price")

              expect(parts_product.locator('.product-item__title')).to_be_visible()
              parts_product.locator('.product-item__title').click()
              expect (page).to_have_url(re.compile(r"/products/"))
              page.go_back()
              print(f"Featured PC parts {i+1} been tested")

    def test_browse_parts_title(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/")

        expect (page.get_by_role("heading", name="Browse by Parts/ Components Type")).to_be_visible()

    def test_browse_parts_list(self, page: Page):
         page.goto("https://ecommerce.datablitz.com.ph/")

         parts_picks = page.locator("#shopify-section-1664331953e91cbf5a .collection-item").count()

         for i in range(parts_picks):
               list = page.locator("#shopify-section-1664331953e91cbf5a .collection-item").nth(i)
               expect (list.locator('.collection-item__image-wrapper ')).to_be_visible()
               list.hover()
               page.wait_for_timeout(500)
               list.click()
               expect (page).to_have_url(re.compile(r"/collections/"))
               page.go_back()
               print(f"Product parts/components {i+1} tested")

    def test_home_end_content(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/")

        expect (page.locator("#shopify-section-static-text-with-icons").get_by_alt_text('Your Most Trusted DataBlitz Store')).to_be_visible()
        expect (page.locator("#shopify-section-static-text-with-icons").get_by_text('Your Most Trusted DataBlitz Store')).to_be_visible()
        expect (page.locator("#shopify-section-static-text-with-icons").get_by_text('100% All Brand New & Original. Shop with confidence!')).to_be_visible()

        expect (page.locator("#shopify-section-static-text-with-icons").get_by_text('Fast Shipping Nationwide')).to_be_visible()
        expect (page.locator("#shopify-section-static-text-with-icons").get_by_text('Ships in 24 hours! Express and Same-Day Delivery within Metro Manila!')).to_be_visible()

        expect (page.locator("#shopify-section-static-text-with-icons").get_by_text('Save on Loyalty Rewards')).to_be_visible()
        expect (page.locator("#shopify-section-static-text-with-icons").get_by_text('Sign in to start earning Loyalty Rewards Points!')).to_be_visible()

        expect (page.locator("#shopify-section-static-text-with-icons").get_by_text('100% Safe and Secure')).to_be_visible()
        expect (page.locator("#shopify-section-static-text-with-icons").get_by_text('All Transactions are Fully Encrypted with State of the Art Technology!')).to_be_visible()
