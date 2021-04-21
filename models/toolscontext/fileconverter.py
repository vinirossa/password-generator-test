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

import sys, os, shutil


def ui_to_py(filename: str,
             filepath: str = os.path.dirname(__file__),
             outputpath: str = os.path.dirname(__file__)) -> None:
    """
    Converts a .ui file from Qt Designer to a python script.

    Args:
        filename (str): The .ui file name to be converted.
        filepath (str): The .ui file path to be converted.
        outputpath (str): The output directory to the python script.

    Returns:
        None.
    """
    if isinstance(filename,str) and isinstance(filepath,str):
        if not ' ' in filename:
            if os.path.isfile("{}\{}.ui".format(filepath,filename)):
                filepath = filepath
                filename = filename
                chk_py = os.path.isfile("{}\{}.py".format(filepath,filename))
                os.system("cd {0} & pyuic5 -x {1}.ui -o {1}.py".format(filepath,filename))
                shutil.move("{}\{}.py".format(filepath,filename),"{}\{}.py".format(outputpath,filename))

                if chk_py:
                    print("File Converter Info: {}.py file updated.".format(filename))
                else:
                    print("File Converter Info: {}.py file created.".format(filename))
            else:
                print("File Converter Alert: The {}.ui file doesn't exist.".format(filename))
        else:
            print("File Converter Error: The filename contains spaces.")
    else:
        print("File Converter Error: Arguments are not string.")


def qrc_to_py(filename: str,
              filepath: str = os.path.dirname(__file__),
              outputpath: str = os.path.dirname(__file__)) -> None:
    """
    Converts a .qrc file from Qt Designer to a python script.

    Args:
        filename (str): The .qrc file name to be converted.
        filepath (str): The .qrc file path to be converted.
        outputpath (str): The output directory to the python script.

    Returns:
        None.
    """
    if isinstance(filename,str) and isinstance(filepath,str):
        if not ' ' in filename:
            if os.path.isfile("{}\{}.qrc".format(filepath,filename)):
                filepath = filepath
                filename = filename
                chk_py = os.path.isfile("{}\{}.py".format(filepath,filename))
                os.system("cd {0} & pyrcc5 {1}.qrc -o {1}.py".format(filepath,filename))
                shutil.move("{}\{}.py".format(filepath,filename),"{}\{}.py".format(outputpath,filename))

                if chk_py:
                    print("File Converter Info: {}.py file updated.".format(filename))
                else:
                    print("File Converter Info: {}.py file created.".format(filename))
            else:
                print("File Converter Alert: The {}.qrc file doesn't exist.".format(filename))
        else:
            print("File Converter Error: The filename contains spaces.")
    else:
        print("File Converter Error: Arguments are not string.")

