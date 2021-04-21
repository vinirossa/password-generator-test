#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Module Name

    Description...

"""

__author__ = "Vinícius Pereira"
__copyright__ = "Copyright 2021, Vinícius Pereira"
__credits__ = ["Vinícius Pereira","etc."]
__date__ = "2021/04/12"
__license__ = "GPL"
__version__ = "1.0.0"
__pythonversion__ = "3.9.1"
__maintainer__ = "Vinícius Pereira"
__contact__ = "viniciuspsb@gmail.com"
__status__ = "Development"

import sys, os
import logging
import inspect
import datetime


STD_LOG_FORMAT = ("%(asctime)s - %(levelname)s - %(name)s - %(filename)s - %(funcName)s() - ln.%(lineno)d"
                  " - %(message)s")

def file_logger(filename: str, 
                level:int = logging.DEBUG, 
                format: str = STD_LOG_FORMAT):

    logger = logging.getLogger(__name__)
    logger.setLevel(level)

    formatter = logging.Formatter(format)

    file_handler = logging.FileHandler(filename)
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger


def prompt_logger(error):

    caller = inspect.getframeinfo(inspect.stack()[1][0])

    error_log = {"error_type": error.__class__.__name__,
                 "error_info": error.__doc__,
                 "error_line": error.__traceback__.tb_lineno,
                 "error_file": os.path.basename(caller.filename),
                 "error_time": datetime.datetime.now(),
                 "error_details": str(error).capitalize()}
    
    print("----- ERROR -----")
    print("Type:",error_log["error_type"])
    print("Info:",error_log["error_info"])
    print("Line:",error_log["error_line"])
    print("File:",error_log["error_file"])
    print("Time:",error_log["error_time"])
    print("Details:",error_log["error_details"])

    return error_log


def error_box():
    pass

def sql_logger():
    pass


if __name__ == "__main__":
    pass