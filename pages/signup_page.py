from automation_exercise_pom.pages.base_page import BasePage


class SignupPage(BasePage):

    def __init__(self,page):
        super().__init__(page)
        self.signup_url='https://automationexercise.com/signup'
        self.signup_name = page.get_by_test_id('signup-name')
        self.signup_email=page.get_by_test_id('signup-email')
        self.signup_btn = page.get_by_test_id('signup-button')

        # account information
        self.title_mr = page.locator('#id_gender1')
        self.title_mrs = page.locator('#id_gender2')
        self.name = page.get_by_test_id('name')
        self.email = page.get_by_test_id('email')  # disabled，read only
        self.password = page.get_by_test_id('password')
        self.days = page.get_by_test_id('days')
        self.months = page.get_by_test_id('months')
        self.years = page.get_by_test_id('years')
        self.newsletter_checkbox = page.locator('#newsletter')
        self.offers_checkbox = page.locator('#optin')

        # address information
        self.first_name = page.get_by_test_id('first_name')
        self.last_name = page.get_by_test_id('last_name')
        self.company = page.get_by_test_id('company')
        self.address = page.get_by_test_id('address')
        self.address2 = page.get_by_test_id('address2')
        self.country = page.get_by_test_id('country')
        self.state = page.get_by_test_id('state')
        self.city = page.get_by_test_id('city')
        self.zipcode = page.get_by_test_id('zipcode')
        self.mobile = page.get_by_test_id('mobile_number')

        # submit
        self.create_account_btn = page.get_by_test_id('create-account')
        self.continue_btn = page.get_by_test_id('continue-button')
        self.logged_in_user=page.locator('.fa-user')
        self.delete=page.locator('a[href="/delete_account"]')



    def open_signup(self):
        self.open_page(self.signup_url)

    def signup(self, name, email):
        self.open_signup()
        self.signup_name.fill(name)
        self.signup_email.fill(email)
        self.signup_btn.click()


    def fill_account_info(self, name, password, day, month, year):
        self.title_mrs.click()
        self.name.fill(name)
        self.password.fill(password)
        self.days.select_option(day)
        self.months.select_option(month)
        self.years.select_option(year)
        self.newsletter_checkbox.check()
        self.offers_checkbox.check()

    def fill_address_info(self, first, last, company, address, country, state, city, zip, mobile):
        self.first_name.fill(first)
        self.last_name.fill(last)
        self.company.fill(company)
        self.address.fill(address)
        self.country.select_option(country)
        self.state.fill(state)
        self.city.fill(city)
        self.zipcode.fill(zip)
        self.mobile.fill(mobile)

    def create_account(self):
        self.create_account_btn.click()

    def delete_account(self):
        self.delete.click()








