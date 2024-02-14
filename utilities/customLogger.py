import logging


class LogGen:
    @staticmethod
    def loggen():
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        log_file_path = "./logs/automation.log"
        file_handler = logging.FileHandler(log_file_path)
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', datefmt='%m%d%Y %I:%M:%S %p')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        return logger
