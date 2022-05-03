import logging
import os
from datetime import datetime

from utilities.readProperties import ReadConfig


class LogGen:

    @staticmethod
    def loggen():
        logging.basicConfig(filename=".\\Logs\\automation.log",
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%y %I:%M:%S %p', filemode='w')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

    @staticmethod
    def logger():
        # getLogger() method takes the test case name as input
        logger = logging.getLogger(__name__)
        # FileHandler() method takes location and path of log file
        fileHandler = logging.FileHandler('.\\Logs\\automation.log')
        # Formatter() method takes care of the log file formatting
        formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(message)s")
        fileHandler.setFormatter(formatter)
        # addHandler() method takes fileHandler object as parameter
        logger.addHandler(fileHandler)
        # setting the logger level
        logger.setLevel(logging.INFO)
        return logger
