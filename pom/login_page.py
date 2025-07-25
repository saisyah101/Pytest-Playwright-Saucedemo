from playwright.sync_api import Page,expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

        #Locator
        self.username_field = page.locator("[data-test='username']")
        self.password_field = page.locator("[data-test='password']")
        self.login_button = page.locator("[data-test='login-button']")
        self.error_message = page.locator("[data-test='error']")
        self.products_title = page.locator("[data-test='title']")

    def login_flow(self, username, password):
        #Fill username field
        self.username_field.fill(username)
        # Fill password field
        self.password_field.fill(password)
        # Click login button
        self.login_button.click()
        return self

    def verify_login_success(self):
        expect(self.login_button).not_to_be_visible()
        expect(self.products_title).to_be_visible()
        return self

    def verify_login_failure(self, expected_error):
        expect(self.login_button).to_be_visible()
        expect(self.error_message).to_have_text(expected_error)
        expect(self.products_title).not_to_be_visible()
        return self

    def verify_invalid_credentials_error(self):
        expected_error = "Epic sadface: Username and password do not match any user in this service"
        return self.verify_login_failure(expected_error)

    def verify_invalid_empty_username(self):
        expected_error = "Epic sadface: Username is required"
        return self.verify_login_failure(expected_error)

    def verify_invalid_empty_password(self):
        expected_error = "Epic sadface: Password is required"
        return self.verify_login_failure(expected_error)