from playwright.sync_api import expect

from automation_exercise_pom.pages.contact_page import ContactPage

def test_contact_us(page,tmp_path):
    cp=ContactPage(page)
    test_file = tmp_path / "upload.txt"
    test_file.write_text("test content")

    cp.fill_contact_form(
        'Test_name',
        'Test@test.com',
        'bug',
        'test message'
    )
    cp.upload(test_file)
    cp.submit()
    expect(cp.success_msg).to_be_visible()
