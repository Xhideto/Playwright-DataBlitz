from playwright.sync_api import Page, expect

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