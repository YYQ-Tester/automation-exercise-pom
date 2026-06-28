
from pytest_playwright.pytest_playwright import page
from automation_exercise_pom.pages.base_page import BasePage


class CartPage(BasePage):

    def __init__(self,page):
        super().__init__(page)
        self.cart_url='https://automationexercise.com/view_cart'
        self.cart_list=page.locator('tr[id^="product-"]')#属性选择器 ^=表示以什么开头 tr是table，属性
        self.check_out_btn=page.locator('.check_out')
        self.order_btn=page.get_by_role('link',name='Place Order')
        self.modal = page.locator('.modal-confirm')


    def delete_first_from_cart(self):
        delete=self.cart_list.first.locator('.cart_quantity_delete')#only delete first one
        delete.click()

    def goto_check_out(self):
        self.check_out_btn.click()

    def place_order(self):
        self.order_btn.click()













