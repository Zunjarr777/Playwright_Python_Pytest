import pytest, yaml
from datetime import datetime
from playwright.sync_api import sync_playwright
from Utility.encrypt_util import decrypt_password
from Utility.log_util import LogGen
from Utility.artifacts import allure_attach_ss_log


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    setattr(item, f"rep_{outcome.get_result().when}", outcome.get_result())


@pytest.fixture(scope="session")
def config():
    with open("config_yaml.yaml") as f:
        data = yaml.safe_load(f)
        data["time_cur"] = datetime.now().strftime("%d%m%Y_%H%M%S")
        data["log_path"] = f"Logs/log_{data['time_cur']}.log"
        data["password"] = decrypt_password(data["encrypted_password"])
        return data


@pytest.fixture(scope="session")
def browser(config):
    pw = sync_playwright().start()
    if config["browser"] == "chromium":
        browser = pw.chromium.launch(headless=config["headless"])
    elif config["browser"] == "firefox":
        browser = pw.firefox.launch(headless=config["headless"])
    else:
        raise ValueError("Unsupported browser")
    yield browser
    browser.close()
    pw.stop()


@pytest.fixture()
def page_with_ss2(browser, config, request):
    context = browser.new_context()
    page = context.new_page()
    page.goto(config["base_url"])
    yield page

    if getattr(request.node, "rep_call", None) and request.node.rep_call.failed:
        allure_attach_ss_log(page, request.node.name, config["ss_path"], config["log_path"])
    context.close()


@pytest.fixture(scope="session")
def logger(config):
    return LogGen.log_creation(config["log_path"])

########################################################################################################################
# (venv) PS C:\Users\lenovo\PycharmProjects\Playwright_Framework_July> pytest -s -v .\test_cases\test_case_login.py --browser webkit
# allure serve Reports/allure_report
########################################################################################################################
