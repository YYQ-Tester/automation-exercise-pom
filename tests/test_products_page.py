
from playwright.sync_api import expect


def test_search_item(open_products_page):
    pp=open_products_page
    item='blue top'
    search_items =pp.search_products(item)
    expect(search_items).not_to_have_count(0)
    expect(search_items.first).to_be_visible()
    expect(search_items.nth(0)).to_contain_text(item,ignore_case=True )


def test_add_first_to_cart(open_products_page):
    pp = open_products_page
    item = 'top'
    pp.add_to_cart(item)
    expect(pp.modal).to_be_visible()
    expect(pp.modal_text).to_contain_text('added')

def test_view_cart(open_products_page,cart_page):
    pp = open_products_page
    cp = cart_page   #cp=CartPage(page)
    item = 'shirt'
    pp.search_view_cart(item)
    expect(pp.page).to_have_url(cp.cart_url)
    expect(cp.cart_items).to_have_count(1)
    item_info=cp.cart_list.locator('.cart_description')
    expect(item_info).to_contain_text(item,ignore_case = True)
