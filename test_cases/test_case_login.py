import time

import allure
from playwright.sync_api import Page
from PageObjectModel.login_page_POM import LoginPage
from Configuration.conftest import *
import sys, os
print("************* sys.path: ", sys.path)
print("************* os.getcwd: ", os.getcwd())

@allure.title("Valid Login -Encrypted Password")
def test_valid_login(page_with_ss: Page, config, logger_step):
    obj_login = LoginPage(page_with_ss, logger_step)
    logger_step("Starting valid login test", level="INFO")
    obj_login.login_method(config["username"], config["encrypted_password"])
    logger_step("Valid login completed, checking dashboard URL", level="WARNING")
    time.sleep(2)
    assert "/dashboard2" in page_with_ss.url

@allure.title("Invalid Login -Failure Screenshot Auto Attach")
def test_invalid_login(page_with_ss: Page, logger_step):
    obj_login = LoginPage(page_with_ss, logger_step)
    logger_step("Starting Invalid login test", level="INFO")
    obj_login.login_method("wrong", "wrong")
    logger_step("Invalid login completed, checking dashboard URL", level="WARNING")
    time.sleep(2)
    assert obj_login.error_message.is_visible()
