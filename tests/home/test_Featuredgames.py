from playwright.sync_api import Page, expect
import re

class TestDatablitzFeaturedConsoleGames:

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

    def test_switch_buttons(self, page: Page):
            page.goto("https://ecommerce.datablitz.com.ph/")

            next_button = page.locator("#shopify-section-1616581165983c351d").get_by_role("button", name="Next")
            expect(next_button).to_be_visible()
            next_button.click()

            previous_button = page.locator("#shopify-section-1616581165983c351d").get_by_role("button", name="Previous")
            expect(previous_button).to_be_visible()
            previous_button.click()

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

    def test_playstation_buttons(self, page: Page):
            page.goto("https://ecommerce.datablitz.com.ph/")

            next_button = page.locator("#shopify-section-1616582529b9e27459").get_by_role("button", name="Next")
            expect(next_button).to_be_visible()
            next_button.click()

            previous_button = page.locator("#shopify-section-1616582529b9e27459").get_by_role("button", name="Previous")
            expect(previous_button).to_be_visible()
            previous_button.click()

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

    def test_xbox_buttons(self, page: Page):
            page.goto("https://ecommerce.datablitz.com.ph/")

            next_button = page.locator("#shopify-section-1616585015028b7de4").get_by_role("button", name="Next")
            expect(next_button).to_be_visible()
            next_button.click()

            previous_button = page.locator("#shopify-section-1616585015028b7de4").get_by_role("button", name="Previous")
            expect(previous_button).to_be_visible()
            previous_button.click()
