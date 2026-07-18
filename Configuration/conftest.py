import pytest
import yaml
import allure
from datetime import datetime
from playwright.sync_api import sync_playwright
from Utility.util import decrypt_password


@pytest.fixture(scope="session")
def config():
    with open("config.yaml") as f:
        data = yaml.safe_load(f)
        data["password"] = decrypt_password(data["encrypted_password"])
        return data


@pytest.fixture(scope="session")
def browser(config):
    playwright = sync_playwright().start()
    browser = getattr(playwright, config["browser"]).launch(headless=config["headless"])
    yield browser
    browser.close()
    playwright.stop()


@pytest.fixture(scope="function")
def page_with_screenshot(browser, config, request):
    context = browser.new_context()
    page = context.new_page()
    page.goto(config["base_url"])
    yield page

    if request.node.rep_call.failed:
        timing = datetime.now().strftime("%d%m%Y_%H%M%S")
        test_name = request.node.name
        allure.attach(page.screenshot(path=f"{config['screenshot_path']}{test_name}_{timing}.png"), name="failure_screenshot", attachment_type=allure.attachment_type.PNG)
        # screenshot_path = f"{config['screenshot_path']}{test_name}_{timing}.png"
        # screenshot = page.screenshot(path=screenshot_path)
        # allure.attach(screenshot, name="failure_screenshot", attachment_type=allure.attachment_type.PNG)
    context.close()
# --------------------------------------------------------------------------------------------------------
# (venv) PS C:\Users\lenovo\PycharmProjects\Playwright_Framework_July> pytest .\test_cases\test_case_login.py -s -v --browser=chromium
# allure serve Reports/allure_report
# allure generate Reports/allure_report
# --------------------------------------------------------------------------------------------------------


# @pytest.fixture(scope="function")
# def setup_page(page: pytest.FixtureRequest, config):
#     page.goto(config["base_url"])               # Navigate to base URL before each test
#     return page


# @pytest.fixture(scope="function")
# def page(browser, config, request):
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto(config["base_url"])
#     yield page
#
#     # Attach screenshot automatically if test failed
#     rep = getattr(request.node, "rep_call", None)
#     if rep and rep.failed:
#         screenshot = page.screenshot(path=f"{config['screenshot_path']}failure.png")
#         allure.attach(screenshot, name="failure_screenshot", attachment_type=allure.attachment_type.PNG)
#
#     if not page.is_closed():
#         page.close()
#     context.close()

# Hook to capture test outcome and store it on the node
# def pytest_runtest_makereport(item, call):
#     if "page" in item.fixturenames and call.when == "call":
#         # call is a CallInfo, but pytest makes a Report object here
#         outcome = pytest.TestReport.from_item_and_call(item, call)
#         item.rep_call = outcome
# ----------------------------------------------------


# @pytest.fixture(scope="function")
# def page(browser, config):
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto(config["base_url"])
#     try:
#         yield page
#     except Exception:
#         screenshot = page.screenshot(path=f"{config['screenshot_path']}failure.png")
#         allure.attach(screenshot, name="failure_screenshot", attachment_type=allure.attachment_type.PNG)
#         raise
#     finally:
#         context.close()
# --------------------------------------------------------------------------------------------------------