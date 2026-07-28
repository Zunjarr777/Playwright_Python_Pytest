import allure
import logging
from datetime import datetime
from Configuration.config_file import config

logging.basicConfig(filename=config["log_path"],
                    level=logging.DEBUG,  # capture all levels
                    datefmt=config["date_format"])


def log_step(message, level: str = "INFO"):
    level = level.upper()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if level == "DEBUG":
        logging.debug(f"{timestamp} {message}_ ")
    elif level == "ERROR":
        logging.error(f"{timestamp} {message}_ ")
    elif level == "WARNING":
        logging.warning(f"{timestamp} {message}_ ")
    else:
        logging.info(f"{timestamp} {message}_ ")

    with allure.step(f"{timestamp} [{level}] {message}_ "):  # Allure step always shows the message, regardless of level
        pass
