import uuid
from playwright.sync_api import expect
from faker import Faker

fake=Faker()


def test_login_success(open_login_page):
    lp = open_login_page
    lp.login()
    expect(lp.logout_btn).to_be_visible()

def test_login_wrong_info(open_login_page,page):
    lp = open_login_page
    lp.login('wrong@email','wrongpswd')
    expect(lp.error_msg).to_be_visible()
    expect(page).to_have_url(lp.login_url)

def test_signup_and_delete(signup_page_and_delete):
    sp=signup_page_and_delete
    name = fake.name()
    #email=fake.email()
    email=f'{uuid.uuid4().hex[:8]}@test.com'
    password='Test1234#'
    birthday=fake.date_of_birth(minimum_age = 18,maximum_age = 99)

    sp.signup(name, email)
    expect(sp.page).to_have_url(sp.signup_url)

    account_info={
        'name':name,
        'password':password,
        'day':str(birthday.day),
        'month':str(birthday.month),
        'year':str(birthday.year)
    }
    sp.fill_account_info(**account_info)
    # ** unpacks a dictionary, so each key becomes a parameter name

    address_info={
        'first':fake.first_name(),
        'last':fake.last_name(),
        'company':fake.company(),
        'address':fake.address(),
        'country':'Canada',
        'state':fake.state(),
        'city':fake.city(),
        'zip':fake.zipcode(),
        'mobile':fake.phone_number()
    }
    sp.fill_address_info(**address_info)
    # ** unpacks a dictionary, so each key becomes a parameter name

    sp.create_account()
    expect(sp.page.get_by_test_id('account-created')).to_be_visible()
    sp.continue_btn.click()
    expect(sp.page).to_have_url('https://automationexercise.com/')


