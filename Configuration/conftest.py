import pytest
import yaml
import allure
from datetime import datetime
from playwright.sync_api import sync_playwright
from Utility.encrypt_util import decrypt_password
from Utility.log_util import log_step


@pytest.fixture(scope="session")
def config():
    with open("config_yaml.yaml") as f:
        data = yaml.safe_load(f)
        data["password"] = decrypt_password(data["encrypted_password"])
        return data


# @pytest.fixture(scope="session")
# def app_config():
#     data = {
#         "username": config_file.config["username"],
#         "encrypted_password": config_file.config["encrypted_password"],
#         "base_url": config_file.config["base_url"],
#         "browser": config_file.config["browser"],  # Add default browser
#         "headless": config_file.config["headless"]}  # Add default headless mode
#
#     if data["encrypted_password"]:
#         data["password"] = decrypt_password(data["encrypted_password"])
#
#     return data

@pytest.fixture(scope="session")
def browser(config):
    playwright = sync_playwright().start()
    browser = getattr(playwright, config["browser"]).launch(headless=config["headless"])
    yield browser
    browser.close()
    playwright.stop()


@pytest.fixture(scope="function")
def page_with_ss(browser, config, request):
    context = browser.new_context()
    page = context.new_page()
    page.goto(config["base_url"])
    yield page

    if request.node.rep_call.failed:
        test_name = request.node.name
        timing = datetime.now().strftime("%d%m%Y_%H%M%S")
        allure.attach(page.screenshot(path=f"{config['screenshot_path']}_{test_name}_{timing}.png"),
                      attachment_type=allure.attachment_type.PNG)
    context.close()


@pytest.fixture
def logger_step():
    return log_step
# --------------------------------------------------------------------------------------------------------
# (venv) PS C:\Users\lenovo\PycharmProjects\Playwright_Framework_July> pytest .\test_cases\test_case_login.py -s -v --browser=chromium
# allure serve Reports/allure_report
# allure generate Reports/allure_report
# --------------------------------------------------------------------------------------------------------
