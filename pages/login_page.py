from automation_exercise_pom.pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self,page):
        super().__init__(page)
        self.login_url='https://automationexercise.com/login'
        self.login_email=page.get_by_test_id('login-email') #locator(['data-qa="login-password"]')
        self.login_password=page.get_by_test_id('login-password')
        self.login_btn = page.get_by_test_id('login-button')
        self.logout_btn=page.locator('a[href="/logout"]')

        self.error_msg=page.get_by_text('incorrect')


    def open_login(self,page):
        self.open_page(self.login_url)



    def login(self,email='test@example.com',password='Psd1234#'):
        self.login_email.fill(email)
        self.login_password.fill(password)
        self.login_btn.click()

    def logout(self):
        self.logout_btn.click()


