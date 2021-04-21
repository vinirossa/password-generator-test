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
import random
import models.toolscontext.validator as validator


class PasswordGenerator():
    """
    A password generator based on keywords.

    Longer class information....
    Longer class information....

    Attributes:
        keywords (list): A boolean indicating if we like SPAM or not.
        total_keywords (int): An integer count of the eggs we have laid.
        max_separators (int): 
    """
    def __init__(self):
        """ 
        Inits PasswordGenerator
        
        Args:
            ...
        """
        self.keywords = []

    @property
    def total_keywords(self):
        self.__total_keywords = len(self.keywords)
        return self.__total_keywords

    @property
    def max_separators(self):
        self.__max_separators = self.total_keywords - 1
        return self.__max_separators

    def generate_password(self, keywords: list, print_cmd: bool = False) -> str:
        """
        Returns the generated password.
        
        Parameters:
            keywords (list): List of strings that will compose the password.
            print_cmd (bool): Print the generated password on console if true.

        Returns:
            generated_password (string): Generated password from keywords.

        """
        self.keywords = list(keywords)
        temp_keywords = []

        ## Shuffle list
        random.shuffle(self.keywords)

        ## Randomize letters and cases
        for keyword in self.keywords:
            i = 0
            normalized_keyword = validator.normalize_string(keyword)
            new_keyword = list(normalized_keyword)

            for letter in new_keyword:
                if letter == 'a':
                    new_keyword[i] = random.choice(letter + "4")
                elif letter == 'e':
                    new_keyword[i] = random.choice(letter + "3")
                elif letter == 'i':
                    new_keyword[i] = random.choice(letter + "1!")
                elif letter == 'o':
                    new_keyword[i] = random.choice(letter + "0")
                elif letter == 's':
                    new_keyword[i] = random.choice(letter + "5$")

                i += 1

            temp_keyword = ''.join(new_keyword)
            temp_keyword = ''.join(random.choice(
                (str.upper, str.lower))(char) for char in temp_keyword)

            temp_keywords.append(temp_keyword)

        self.reset_list_with_values(self.keywords, temp_keywords)

        ## Insert separators
        i = 0
        while (i < self.max_separators):
            self.keywords[i] += random.choice("@#_&")
            i += 1

        generated_password = ''.join(self.keywords)

        ## Print to console
        if print_cmd:
            print(generated_password,"({0})".format(len(generated_password)))

        return generated_password

    def reset_list_with_values(self, original_list: list, temporary_list: list) -> None:
        original_list.clear()
        original_list.extend(temporary_list)
        temporary_list.clear()


if __name__ == "__main__":
    pass