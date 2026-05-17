import logging
import os


class LogGen():
    @staticmethod
    def loggen():
        path = os.path.abspath(os.curdir) + '\\logs\\automation.log'
        os.makedirs(os.path.dirname(path), exist_ok=True)
        logging.basicConfig(filename=path,
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',force=True)

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
