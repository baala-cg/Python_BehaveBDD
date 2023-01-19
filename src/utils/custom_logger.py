import inspect
import logging

import allure


def custom_logger():
    # This is used to get the class/method name from where this customlogger method is called
    log_name = inspect.stack()[1][3]

    # Create the logging object and pass the log_name in it
    logger = logging.getLogger(log_name)

    # Set the log level
    logger.setLevel(logging.DEBUG)

    # Create the file_handler to save the logs in the file
    file_handler = logging.FileHandler("./logs/my_log.log", mode='a')

    # Set the logLevel for file_handler
    file_handler.setLevel(logging.DEBUG)

    # Create the formatter in which format do you like to save the logs
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s : %(message)s',
                                  datefmt='%d/%m/%y %I:%M:%S %p %A')

    # Set the formatter to file_handler
    file_handler.setFormatter(formatter)

    # Add file_handler to logging
    logger.addHandler(file_handler)

    # Finally return the logging object
    return logger


logger = custom_logger()


def allure_logs(text):
    with allure.step(text):
        pass


def allure_fail_logs(text):
    allure.step(text)


def info_log(text):
    allure_logs(text)
    logger.info(text)
    return text


def error_log(text):
    logger.error(text)
    allure_fail_logs(text)
    return text
