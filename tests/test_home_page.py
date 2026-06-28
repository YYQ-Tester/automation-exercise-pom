
from playwright.sync_api import expect

def test_navigation(open_home_page,page):
    home=open_home_page

    home.goto_home()
    expect(page).to_have_url('https://automationexercise.com/')
    home.expect_slider_is_visible()

    home.goto_products()
    expect(page).to_have_url('https://automationexercise.com/products')

    home.goto_cart()
    expect(page).to_have_url('https://automationexercise.com/view_cart')

    home.goto_login()
    expect(page).to_have_url('https://automationexercise.com/login')

    home.goto_contact()
    expect(page).to_have_url('https://automationexercise.com/contact_us')


