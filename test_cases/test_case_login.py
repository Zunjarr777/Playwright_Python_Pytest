import allure
from PageObjectModel.login_page_POM import LoginPage
from playwright.sync_api import sync_playwright, expect, Page
# from Configuration.conftest import config, setup_page
from Configuration.conftest import config, page_with_screenshot

import sys, os
print("************* sys.path: ", sys.path)
print("************* os.getcwd: ", os.getcwd())

@allure.title("Valid Login with Encrypted Password")
def test_valid_login(page_with_screenshot: Page, config):
    obj_login = LoginPage(page_with_screenshot)
    obj_login.login_method(config["username"], config["encrypted_password"])
    assert "/dashboard" in page_with_screenshot.url

@allure.title("Invalid Login -Failure Screenshot Auto Attach")
def test_invalid_login(page_with_screenshot: Page):
    obj_login = LoginPage(page_with_screenshot)
    obj_login.login_method("wrong", "wrong")
    assert obj_login.error_message.is_visible()        # No need to manually attach screenshot here — hook will do it if test fails
