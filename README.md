# Automation Exercise POM

This is my first Playwright automation project using Page Object Model.  
Target site: https://automationexercise.com

## Tech Stack
- Python / Playwright / pytest
- Faker / uuid
- Page Object Model (POM)

## Project Structure
```
automation_exercise_pom/
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── signup_page.py
│   ├── home_page.py
│   ├── products_page.py
│   ├── cart_page.py
│   ├── contact_page.py
│   └── pay_page.py
│
├── tests/
│   ├── test_signup_login.py
│   ├── test_home_page.py
│   ├── test_products_page.py
│   ├── test_cart_page.py
│   └── test_contact.py
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── .gitignore
```

## Test Coverage
- Register / Login / Login failure
- Navigation bar jumping
- Product search / Add to cart
- Delete from cart / Place order / Complete payment
- Submit contact form / File upload

## Design Decisions

**Navigation bar lives in BasePage**  
The nav bar is shared across all pages, so it belongs in `BasePage` (parent class).  
Each subclass only defines its own unique elements — keeps the structure clean and logical.

**Navigation tests are isolated from page tests**  
Navigation tests verify jumping by clicking links, simulating real user behavior.  
Other page tests open URLs directly — so if the nav bar breaks, page tests still run independently.

**Delete Account as teardown**  
After signup tests, the test account is deleted via the site's own delete function.  
This keeps the test environment clean without needing database access.

**Avoid invalid dates**  
Faking day, month, and year separately risks illegal combinations like February 31st.  
Instead, `fake.date_of_birth()` generates a valid date, then day/month/year are read individually.

## Key Implementation Notes
- Cookie consent dialog is handled in `BasePage.goto()` — applied automatically on every page
- Signup form uses a dictionary to fill multiple fields in one loop
- Cart list uses CSS prefix selector `tr[id^="product-"]` to match all product rows
- Product ID is stored before deletion, then used to verify the element is no longer visible
- `uuid` generates unique fake emails; `Faker` provides other signup data
- Temporary file is created at runtime and passed to the file input — no real file stored in project
- Dialog event listener is registered with a lambda before the triggering action

## How to Run
pip install -r requirements.txt
pytest tests/
pytest tests/ --headed        # run with browser visible
pytest tests/ -v              # verbose output

## Author
Emily