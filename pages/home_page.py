from playwright.sync_api import expect
from automation_exercise_pom.pages.base_page import BasePage

class HomePage(BasePage):

    def __init__(self,page):
        super().__init__(page)
        self.home_url='https://automationexercise.com/'
        self.slider = page.locator('#slider-carousel')



    def open_home(self):
       self.open_page(self.home_url)

    def expect_slider_is_visible(self):
        expect(self.slider).to_be_visible()





