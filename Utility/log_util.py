import logging

class LogGen:
    @staticmethod
    def log_creation(log_path):
        logging.basicConfig(filename=log_path,
                            level=logging.DEBUG,
                            format="%(asctime)s [%(levelname)s] %(message)s",
                            datefmt="%Y-%m-%d %H:%M:%S",
                            force=True)
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        return logger

    # @staticmethod
    # def attach_log(log_path):
    #     allure.attach.file(log_path, name=f"{datetime.now().strftime('%H:%M:%S')}",
    #                         attachment_type=allure.attachment_type.TEXT)
