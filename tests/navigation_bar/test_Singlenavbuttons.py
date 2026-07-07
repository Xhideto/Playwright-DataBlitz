from playwright.sync_api import Page, expect
import re

class TestNavBarSingleMenus:
    def test_pre_orders(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/")

        order = page.locator(".tmenu_navbar")

        order.get_by_role('link', name="Pre-Orders").hover()
        page.wait_for_timeout(500)
        order.get_by_role("link", name='Pre-Orders', exact=True).click()
        expect (page).to_have_url("https://ecommerce.datablitz.com.ph/pages/pre-orders")
        page.wait_for_timeout(1000)
        print(f"Pre-Orders is working")

    def test_digital_store(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/")

        digital = page.locator(".tmenu_navbar")

        digital.get_by_role('link', name="Digital Store").hover()
        page.wait_for_timeout(500)
        with page.expect_popup() as digital_store:
            digital.get_by_role("link", name='Digital Store', exact=True).click()

        new_page = digital_store.value
        new_page.wait_for_load_state()

        expect (new_page).to_have_url(re.compile(r"https://digital.datablitz.com.ph/"))
        print(f"'{new_page.url}' is working")
        new_page.close()

    def test_promos(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/")

        promos = page.locator(".tmenu_navbar")

        promos.get_by_role('link', name="Promos").hover()
        page.wait_for_timeout(500)

        expect (promos.get_by_role('tab', name="HOT DEALS"))
        print(f"HOT DEALS badge is visible")

        promos.get_by_role("link", name='Promos').click()
        expect (page).to_have_url("https://ecommerce.datablitz.com.ph/pages/bundles-and-promos")
        page.wait_for_timeout(1000)
        print(f"Promos is working")

    def test_order_status(self, page: Page):
        page.goto("https://ecommerce.datablitz.com.ph/")

        status = page.locator(".tmenu_navbar")

        status.get_by_role('link', name="Order Status").hover()
        page.wait_for_timeout(500)
        status.get_by_role("link", name='Order Status', exact=True).click()
        expect (page).to_have_url("https://ecommerce.datablitz.com.ph/pages/order-status-lookup")
        page.wait_for_timeout(1000)
        print(f"Order Status is working")