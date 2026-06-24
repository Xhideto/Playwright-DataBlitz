from playwright.sync_api import Page, expect
import re

class TestDatablitzPCParts:

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

              monitors_product.locator('.product-item__image-wrapper').click()
              expect (page).to_have_url(re.compile(r"/products/"))
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
              expect (page).to_have_url(re.compile(r"/products/"))
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

    def test_featured_laptops_buttons(self, page: Page):
            page.goto("https://ecommerce.datablitz.com.ph/")

            next_button = page.locator("#shopify-section-16167331070cdccb23").get_by_role("button", name="Next")
            expect(next_button).to_be_visible()
            next_button.click()

            previous_button = page.locator("#shopify-section-16167331070cdccb23").get_by_role("button", name="Previous")
            expect(previous_button).to_be_visible()
            previous_button.click()

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

    def test_featured_pc_parts_buttons(self, page: Page):
            page.goto("https://ecommerce.datablitz.com.ph/")

            next_button = page.locator("#shopify-section-16643318579a4c7d0a").get_by_role("button", name="Next")
            expect(next_button).to_be_visible()
            next_button.click()

            previous_button = page.locator("#shopify-section-16643318579a4c7d0a").get_by_role("button", name="Previous")
            expect(previous_button).to_be_visible()
            previous_button.click()

    def test_pc_parts_collections_extend(self, page: Page):
         page.goto("https://ecommerce.datablitz.com.ph/")

         pc_parts = page.locator("#shopify-section-collection_list_KfYbE8 .collection-item").count()

         for i in range(pc_parts):
               product = page.locator("#shopify-section-collection_list_KfYbE8 .collection-item").nth(i)
               expect (product.locator('.collection-item__image-wrapper ')).to_be_visible()
               product.hover()
               page.wait_for_timeout(500)
               product.click()

               expect (page).to_have_url(re.compile(r"/collections/"))
               page.go_back()
               print(f"Extended pc parts collections {i+1} tested")

    def test_pc_parts_collections_buttons(self, page: Page):
            page.goto("https://ecommerce.datablitz.com.ph/")

            next_button = page.locator("#shopify-section-collection_list_KfYbE8").get_by_role("button", name="Next")
            expect(next_button).to_be_visible()
            next_button.click()

            previous_button = page.locator("#shopify-section-collection_list_KfYbE8").get_by_role("button", name="Previous")
            expect(previous_button).to_be_visible()
            previous_button.click()

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

    def test_browse_parts_buttons(self, page: Page):
            page.goto("https://ecommerce.datablitz.com.ph/")

            next_button = page.locator("#shopify-section-1664331953e91cbf5a").get_by_role("button", name="Next")
            expect(next_button).to_be_visible()
            next_button.click()

            previous_button = page.locator("#shopify-section-1664331953e91cbf5a").get_by_role("button", name="Previous")
            expect(previous_button).to_be_visible()
            previous_button.click()
