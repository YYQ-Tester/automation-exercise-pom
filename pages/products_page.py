import re
from automation_exercise_pom.pages.base_page import BasePage


class ProductsPage(BasePage):

    def __init__(self,page):
        super().__init__(page) #here should always be page
        self.products_url='https://automationexercise.com/products'
        self.search_bar=page.get_by_placeholder('Search Product')
        self.search_btn=page.locator('#submit_search')
        self.products_list=page.locator('.productinfo') # Locate the individual product instead of the container
        self.modal=page.locator('.modal-confirm')
        self.modal_text=page.locator('.modal-confirm .modal-body')
        self.view_cart=self.modal.locator('a[href="/view_cart"]')

        self.continue_btn=page.get_by_role('button',name='Continue Shopping')


    def open_products(self):
        self.open_page(self.products_url)

    def search_products(self,item):
        self.search_bar.fill(item)
        self.search_btn.click()

    def search_results(self,item):
        result=self.products_list.filter(
            has_text=re.compile(item,re.IGNORECASE)
        )# Use a regex to ignore case
        return result

    def add_to_cart(self,item):
        search_items=self.search_results(item)
        add_btn=search_items.nth(0).locator('.add-to-cart')# Locate the button inside the product
        add_btn.click()


    def search_view_cart(self,item):
        self.add_to_cart(item)
        self.view_cart.click()







