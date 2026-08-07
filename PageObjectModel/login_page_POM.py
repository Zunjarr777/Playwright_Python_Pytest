from Configuration.conftest import logger

class LoginPage:
    def __init__(self, page, logger):
        self.page = page
        self.logger = logger
        self.username_input = page.locator("input[name='username']")
        self.password_input = page.locator("input[name='password']")
        self.login_button = page.locator("button[type='submit']")
        self.error_message = page.locator(".oxd-alert-content-text")

    def login_method(self, username, password):
        self.logger.debug(f"Filling username: {username}")
        self.username_input.fill(username)
        self.logger.debug(f"Filling password: {password}")
        self.password_input.fill(password)
        self.logger.info("Clicking login button")
        self.login_button.click()
