from automation_exercise_pom.pages.base_page import BasePage


class ContactPage(BasePage):

    def __init__(self,page):
        super().__init__(page)
        self.contact_url='https://automationexercise.com/contact_us'
        self.name=page.get_by_test_id('name')
        self.email = page.get_by_test_id('email')
        self.subject = page.get_by_test_id('subject')
        self.message = page.get_by_test_id('message')
        self.submit_button = page.get_by_test_id('submit-button')
        self.choose_file = page.locator('input[name="upload_file"]')
        self.success_msg=page.locator('.status.alert-success')



    def open_contact(self):
        self.open_page(self.contact_url)

    def fill_contact_form(self,name,email,subject,message):
        self.open_contact()
        self.name.fill(name)
        self.email.fill(email)
        self.subject.fill(subject)
        self.message.fill(message)

    def upload(self,file):
        self.choose_file.set_input_files(file)

    def submit(self):
        self.page.on('dialog', lambda dialog: dialog.accept()) #register an event listener before triggering
        self.submit_button.click()




