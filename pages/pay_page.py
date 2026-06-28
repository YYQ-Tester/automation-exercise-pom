from automation_exercise_pom.pages.base_page import BasePage

class PayPage(BasePage):

    def __init__(self,page):
        super().__init__(page)
        self.card_name = page.get_by_test_id('name-on-card')
        self.card_num = page.get_by_test_id('card-number')
        self.cvc = page.get_by_test_id('cvc')
        self.expired_mon = page.get_by_test_id('expiry-month')
        self.expired_year = page.get_by_test_id('expiry-year')
        self.pay_btn = page.get_by_role('button', name = 'Pay and Confirm Order')

    def fill_payment(self, name, number, cvc, month, year):
        self.card_name.fill(name)
        self.card_num.fill(number)
        self.cvc.fill(cvc)
        self.expired_mon.fill(month)
        self.expired_year.fill(year)

    def confirm_payment(self):
        self.pay_btn.click()

