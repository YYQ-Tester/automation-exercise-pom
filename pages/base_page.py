class BasePage:
    def __init__(self,page):
        self.page=page
        self.nav_home = page.get_by_role('link',name='Home')
        self.nav_products = page.locator('#header a[href="/products"]')
        self.nav_cart = page.locator('#header a[href="/view_cart"]')
        self.nav_login = page.locator('#header a[href="/login"]')
        self.nav_contact = page.locator('#header a[href="/contact_us"]')

    def dismiss_cookie(self):
        cookie_banner = self.page.locator('.fc-choice-dialog')
        consent = self.page.locator('.fc-cta-consent')
        if cookie_banner.is_visible():
            consent.click()

    def open_page(self,url):
        self.page.goto(url)
        self.dismiss_cookie()

    def goto_home(self):
        self.nav_home.click()

    def goto_products(self):
        self.nav_products.click()

    def goto_cart(self):
        self.nav_cart.click()

    def goto_login(self):
        self.nav_login.click()

    def goto_contact(self):
        self.nav_contact.click()


