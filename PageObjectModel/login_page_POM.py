class LoginPage:
    def __init__(self, page, logger_step):
        self.page = page
        self.logger_step = logger_step
        self.username_input = page.locator("input[name='username']")
        self.password_input = page.locator("input[name='password']")
        self.login_button = page.locator("button[type='submit']")
        self.error_message = page.locator(".oxd-alert-content-text")

    def login_method(self, username, password):
        self.logger_step("Filling username", level="DEBUG")
        self.username_input.fill(username)
        self.logger_step("Filling password", level="DEBUG")
        self.password_input.fill(password)
        self.logger_step("Clicking login button", level="INFO")
        self.login_button.click()
