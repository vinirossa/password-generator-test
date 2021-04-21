#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Password Generator

    Generates safe and easy to remember passwords based on keywords...

"""

__author__ = "Vinícius Pereira"
__copyright__ = "Copyright 2021, Vinícius Pereira"
__credits__ = ["Vinícius Pereira","etc."]
__date__ = "2021/04/12"
__license__ = "GPL"
__version__ = "1.2.21"
__pythonversion__ = "3.9.1"
__maintainer__ = "Vinícius Pereira"
__contact__ = "viniciuspsb@gmail.com"
__status__ = "Development"

import sys, os


PROJECT_NAME = "Password Generator"
EXE_NAME = "generator"
URL = os.environ["SETUP_URL"] = os.popen("git config --get remote.origin.url").read().strip()
os.environ["SETUP_VERSION"] = os.environ["VERSION"] = __version__
CLASSIFIERS = os.environ["SETUP_CLASSIFIERS"] = ""
DESCRIPTION = os.environ["SETUP_DESCRIPTION"] = "" 
KEYWORDS = os.environ["SETUP_KEYWORDS"] = ""
PACKAGES = os.environ["SETUP_PACKAGES"] = ""
PY_MODULES = os.environ["SETUP_PY_MODULES"] = ""
SCRIPTS =os.environ["SETUP_SCRIPTS"] = ""
ICON_FILE = "assets/lock-48.ico"
VERSION_FILE = "version_info.txt"
RESOURCE_FILE = ""
METADATA_DICT = {"Version" : __version__,
                 "CompanyName" : __author__, 
                 "FileDescription": PROJECT_NAME,
                 "InternalName": PROJECT_NAME, 
                 "LegalCopyright": __copyright__,
                 "OriginalFilename": EXE_NAME + ".exe",
                 "ProductName": PROJECT_NAME}


def main():
    try:
        import controllers.generate_password_controller
    except Exception as e:
        print("--- Execution Error on Main ---")


if __name__ == "__main__":
    main()