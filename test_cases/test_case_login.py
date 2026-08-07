import allure, sys, os
from playwright.sync_api import Page
from PageObjectModel.login_page_POM import LoginPage
from Configuration.conftest import config, logger, page_with_ss2

print("************* sys.path: ", sys.path)
print("************* os.getcwd: ", os.getcwd())


@allure.title("Valid Login -Encrypted Password")
def test_valid_login(page_with_ss2: Page, config, logger):
    obj_login = LoginPage(page_with_ss2, logger)
    logger.info("Executing valid login test")
    obj_login.login_method(config["username"], config["encrypted_password"])
    logger.warning("Valid login completed, checking dashboard URL")
    assert "/dashboard2" in page_with_ss2.url


@allure.title("Invalid Login -Failure Screenshot Auto Attach")
def test_invalid_login(page_with_ss2: Page, logger):
    obj_login = LoginPage(page_with_ss2, logger)
    logger.info("Executing Invalid login test")
    obj_login.login_method("wrong", "wrong")
    logger.warning("Invalid login completed, checking dashboard URL")
    assert obj_login.error_message.is_visible()
