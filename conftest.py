# 在项目的全局配置或 conftest.py 中配置一次即可
import playwright
import pytest

from automation_exercise_pom.pages.cart_page import CartPage
from automation_exercise_pom.pages.home_page import HomePage
from automation_exercise_pom.pages.login_page import LoginPage
from automation_exercise_pom.pages.products_page import ProductsPage
from automation_exercise_pom.pages.signup_page import SignupPage


@pytest.fixture(scope="session", autouse=True) #可复用
def set_test_id(playwright):
    playwright.selectors.set_test_id_attribute("data-qa")


@pytest.fixture
def open_home_page(page):
    hp=HomePage(page)
    hp.open_home()
    return hp

@pytest.fixture()
def signup_page_and_delete(page):
    sp=SignupPage(page)
    yield sp
    if sp.delete.is_visible():
        sp.delete_account()


@pytest.fixture()
def open_login_page(page):
    lp=LoginPage(page)
    lp.open_login(page)
    return lp

@pytest.fixture()
def logged_in_user(open_login_page):
    lgd=open_login_page
    lgd.login()
    yield lgd
    lgd.logout()



@pytest.fixture()
def open_products_page(page):
    pp=ProductsPage(page)
    pp.open_products()
    return pp



@pytest.fixture()
def cart_page(page):
    cp=CartPage(page)
    return cp
#等同于在函数内部赋值cp
# def test_view_cart(open_products_page,page):
#     pp = open_products_page
#     cp = CartPage(page)

@pytest.fixture()
def products_page(page):
    pp=ProductsPage(page)
    return pp