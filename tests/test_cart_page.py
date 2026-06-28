import re
from playwright.sync_api import expect
from automation_exercise_pom.pages.pay_page import PayPage


def test_delete_item(open_products_page,cart_page):
    pp=open_products_page
    cp=cart_page
    pp.search_view_cart('top')
    first_item_id=cp.cart_list.first.get_attribute('id')
    cp.delete_first_from_cart()
    first_item=cp.page.locator(f'#{first_item_id}')#f-string
    expect(first_item).not_to_be_visible()

def test_order_required_login(open_products_page,cart_page):
    pp = open_products_page
    cp = cart_page
    pp.search_view_cart('top')
    cp.goto_check_out()
    expect(cp.modal).to_be_visible()
    expect(cp.page).to_have_url(cp.cart_url)

def test_order_success(logged_in_user,products_page,cart_page,page):
    lp=logged_in_user
    pp=products_page
    cp=cart_page
    pyp = PayPage(page)

    lp.goto_products()
    pp.search_view_cart('top')
    cp.goto_check_out()
    cp.place_order()
    pyp.fill_payment('Test', '1234567890', '123', '12', '2029')
    pyp.confirm_payment()

    expect(cp.page).to_have_url(re.compile('/.*payment_done/\\d+'))
    expect(cp.page.get_by_test_id('order-placed')).to_be_visible()

