import allure
from datetime import datetime

def allure_attach_ss_log(page, test_name, ss_path, log_path):
    timestamp = datetime.now().strftime("%d%m%Y_%H%M%S")
    page.screenshot(path=f"{ss_path}_{test_name}_{timestamp}.png")

    with allure.step(f"{test_name}"):
        allure.attach.file(f"{ss_path}_{test_name}_{timestamp}.png", attachment_type=allure.attachment_type.PNG)
        allure.attach.file(log_path, name=f"{timestamp}", attachment_type=allure.attachment_type.TEXT)

    # with allure.step(f"Failure - {test_name}"):
    #     allure.attach.file(f"{ss_path}_{test_name}_{timestamp}.png", name="Failed Screenshot", attachment_type=allure.attachment_type.PNG)
    #     LogGen.attach_log(log_path, name="Log File")
