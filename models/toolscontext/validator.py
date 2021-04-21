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

import sys, os; sys.path.insert(0,os.getcwd())
import re
import unicodedata
import PyQt5.QtWidgets as qtw
import models.toolscontext.enums.strenums as stre


def check_string(text: str,
                 isempty: bool = False,
                 isspace: bool = False,
                 lowercase: bool = False,
                 uppercase: bool = False,
                 numbers: bool = False,
                 accented_letters: bool = False,
                 cedilla: bool = False,
                 isolated_accents: bool = False,
                 punctuations: bool = False,
                 special_chars: bool = False,
                 white_spaces: bool = False,
                 break_lines: bool = False,
                 non_unicode: bool = False,
                 print_cmd: bool = False) -> bool:
    """
    Checks a string based on the parameters chosen by the user.

    Args:
        text (str): The string to be checked.
        isempty (bool): Checks if the string is empty. Defaults to False.
        isspace (bool): Checks if the string is only white spaces. Defaults to False.
        lowercase (bool): Checks if the string contains lowercases. Defaults to False.
        uppercase (bool): Checks if the string contains uppercases. Defaults to False.
        numbers (bool): Checks if the string contains numbers. Defaults to False.
        accented_letters (bool): Checks if the string contains accented letters. Defaults to False.
        cedilla (bool): Checks if the string contains cedilla. Defaults to False.
        isolated_accents (bool): Checks if the string contains isolated accents. Defaults to False.
            "`´^~¨"
        punctuations (bool): Checks if the string contains punctuations. Defaults to False.
            ".:,;\-_<>=+*!?)(}{|''""\][\\/"
        special_chars (bool): Checks if the string contains special characters. Defaults to False.
            "@#$%&"
        white_spaces (bool): Checks if the string contains white spaces. Defaults to False.
        break_lines (bool): Checks if the string contains break lines. Defaults to False.
        non_unicode (bool): Checks if the string contains non-unicode characters. Defaults to False.
        print_cmd (bool): Prints the alerts to the console. Defaults to False.

    Returns:
        True if the string passes all the tests, False if it fails at any.
    """
    if isinstance(text, str):
        ## Is Empty
        if isempty and not text:
            if print_cmd:
                print("Validator Error: The string is empty!")
            elif qt_window:
                qtw.QMessageBox.critical(
                    qt_window, "Erro", "O texto está em branco!")
            return False
        ## Is Space
        if isspace and text.isspace():
            if print_cmd:
                print("Validator Error: The string only contains white spaces!")
            elif qt_window:
                qtw.QMessageBox.critical(
                    qt_window, "Erro", "O texto contém apenas espaços!")
            return False
        ## Lowercase
        if lowercase and re.search('[a-z]', text):
            if print_cmd:
                print("Validator Error: The string contains lowercase letters!")
            elif qt_window:
                qtw.QMessageBox.critical(
                    qt_window, "Erro", "O texto contém letras minúsculas!")
            return False
        ## Uppercase
        if uppercase and re.search('[A-Z]', text):
            if print_cmd:
                print("Validator Error: The string contains uppercase letters!")
            elif qt_window:
                qtw.QMessageBox.critical(
                    qt_window, "Erro", "O texto contém letras maiúsculas!")
            return False
        ## Numbers
        if numbers and re.search('[\d]', text):
            if print_cmd:
                print("Validator Error: The string contains numbers!")
            elif qt_window:
                qtw.QMessageBox.critical(
                    qt_window, "Erro", "O texto contém números!")
            return False
        ## Accented letters
        if accented_letters and re.search('[àèìòùáéíóúâêîôûäëïöüãõ]', text):
            if print_cmd:
                print("Validator Error: The string contains accented letters!")
            elif qt_window:
                qtw.QMessageBox.critical(
                    qt_window, "Erro", "O texto contém letras acentuadas!")
            return False
        ## Cedilla
        if cedilla and re.search('[ç]', text):
            if print_cmd:
                print("Validator Error: The string contains cedilla!")
            elif qt_window:
                qtw.QMessageBox.critical(
                    qt_window, "Erro", "O texto contém cedilha!")
            return False
        ## Isolated Accents
        if isolated_accents and re.search('[`´^~¨]', text):
            if print_cmd:
                print("Validator Error: The string contains isolated accents!")
            elif qt_window:
                qtw.QMessageBox.critical(
                    qt_window, "Erro", "O texto contém acentos isolados!")
            return False
        ## Punctuations
        if punctuations and re.search('[.:,;\-_<>=+*!?)(}{|''""\][\\/]', text):
            if print_cmd:
                print("Validator Error: The string contains punctuations!")
            elif qt_window:
                qtw.QMessageBox.critical(
                    qt_window, "Erro", "O texto contém pontuações!")
            return False
        ## Special Characters
        if special_chars and re.search('[@#$%&]', text):
            if print_cmd:
                print("Validator Error: The string contains special characters!")
            elif qt_window:
                qtw.QMessageBox.critical(
                    qt_window, "Erro", "O texto contém caracteres especiais!")
            return False
        ## Non-unicode
        if non_unicode and re.search('(?![ -~ç´¨àèìòùáéíóúâêîôûäëïöüãõ\n]).', text):
            if print_cmd:
                print("Validator Error: The string contains invalid characters!")
            elif qt_window:
                qtw.QMessageBox.critical(
                    qt_window, "Erro", "O texto contém caracteres especiais!")
            return False
        ## White Spaces
        if white_spaces and re.search('[\s]', text):
            if print_cmd:
                print("Validator Error: The string contains white spaces!")
            elif qt_window:
                qtw.QMessageBox.critical(
                    qt_window, "Erro", "O texto contém espaços!")
            return False
        ## Break Lines
        if break_lines and re.search('[\n]', text):
            if print_cmd:
                print("Validator Error: The string contains break lines!")
            elif qt_window:
                qtw.QMessageBox.critical(
                    qt_window, "Erro", "O texto contém quebras de linha!")
            return False
        ## Consider "¡" and "¿"
        
        return True
    else:
        print("Validator Error: Text must be an string.")
        return False


def format_string(text: str,
                  trim: bool = False, 
                  normalize: bool = False, 
                  case: stre.StrCase = None) -> tuple[str,bool]:
    """
    Formats a string based on the parameters chosen by the user.

    Args:
        text (str): The string to be formatted.
        trim (bool): Trims the string. Defaults to False.
        normalize (bool): Removes all accents from the string. Defaults to False.
        case (stre.StrCase): Cases the string based on enum, which can be capitalize, title, uppercase or
            lowercase. Defaults to None.

    Returns:
        text (str): The formatted string.
        False if text isn't a string.
    """
    if isinstance(text, str):
        ## Trims the string
        if trim:
            # text = " ".join(text.split())
            text = text.strip()

        ## Normalizes the string
        if normalize:
            text = unicodedata.normalize('NFD', text).encode(
            'ascii', 'ignore').decode("utf-8")

        ## Cases the string
        if case == stre.StrCase.Capitalize:
            text = text.capitalize()
        elif case == stre.StrCase.Title:
            text = text.title()
        elif case == stre.StrCase.Upper:
            text = text.upper()
        elif case == stre.StrCase.Lower:
            text = text.lower()

        return text

    else:
        print("Validator Error: Text must be an string.")
        return False

def check_email() -> None:
    pass


def check_int() -> None:
    pass

def format_int() -> None:
    pass


def check_float() -> None:
    pass

def format_float() -> None:
    pass


def check_binary() -> None:
    pass

def format_binary() -> None:
    pass


def check_date() -> None:
    pass

def format_date() -> None:
    pass


def check_currency() -> None:
    pass

def format_currency() -> None:
    pass


if __name__ == "__main__":
    pass