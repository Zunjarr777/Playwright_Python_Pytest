# --- Standard library ---
import os
from datetime import datetime
# --- Third-party libraries ---
import pytest, allure, yaml
from playwright.sync_api import sync_playwright
# --- Local project imports ---
from Utility.encrypt_util import decrypt_password
from Utility.log_util import LogGen
# from Utility.log_util import log_step


@pytest.fixture(scope="session")
def config():
    with open("config_yaml.yaml") as f:
        data = yaml.safe_load(f)
        data["password"] = decrypt_password(data["encrypted_password"])
        # data["time_current"] = datetime.now().strftime("%d%m%Y_%H%M%S")
        timestamp = datetime.now().strftime("%d%m%Y_%H%M%S")
        data["time_current"] = timestamp
        data["log_path"] = f"Logs/test_{timestamp}.log"
        # os.makedirs(data["screenshot_path"], exist_ok=True)
        return data

@pytest.fixture(scope="session")
def browser(config):
    playwright = sync_playwright().start()
    browser = getattr(playwright, config["browser"]).launch(headless=config["headless"])
    yield browser
    browser.close()
    playwright.stop()

@pytest.fixture()
def page_with_ss(browser, config, request):
    context = browser.new_context()
    page = context.new_page()
    page.goto(config["base_url"])
    yield page
    if request.node.rep_call.failed:
        test_name = request.node.name
        allure.attach(page.screenshot(path=f"{config['screenshot_path']}{test_name}_{config['time_current']}.png"),
                                      attachment_type=allure.attachment_type.PNG)
    context.close()

# @pytest.fixture()
# def logger_step():
#     return log_step

@pytest.fixture()
def logger(config):
    return LogGen.log_creation(config["log_path"])
# --------------------------------------------------------------------------------------------------------
# (venv) PS C:\Users\lenovo\PycharmProjects\Playwright_Framework_July> pytest .\test_cases\test_case_login.py -s -v --browser=chromium
# allure serve Reports/allure_report
# allure generate Reports/allure_report

# pip install -r requirements.txt
# --------------------------------------------------------------------------------------------------------
