#!/usr/bin/env python

__author__ = "Vinícius Pereira"
__copyright__ = "Copyright 2021, Vinícius Pereira"
__credits__ = "Vinícius Pereira"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Vinícius Pereira"
__email__ = "viniciuspsb@gmail.com"
__status__ = "Development"

import sys
import os
import inspect as ins
from enum import Enum, auto


class StrCase(Enum):
    Title = auto(),
    Capitalize = auto(),
    Upper = auto(),
    Lower = auto()


class StrPattern(Enum):
    UppercaseLetters = auto(),
    LowercaseLetters = auto(),
    UpperLowerLetters = auto(),
    AccLettersCedilla = auto(),
    AccLettersCedillaHyphen = auto(),

    UppercaseLettersPunct = auto(),
    LowercaseLettersPunct = auto(),
    UpperLowerLettersPunct = auto(),
    AccLettersCedillaPunct = auto(),

    UppercaseLettersSpecial = auto(),
    LowercaseLettersSpecial = auto(),
    UpperLowerLettersSpecial = auto(),
    AccLettersCedillaSpecial = auto(),

    UppercaseLettersSpaces = auto(),
    LowercaseLettersSpaces = auto(),
    UpperLowerLettersSpaces = auto(),
    AccLettersCedillaSpaces = auto(),
    AccLettersCedillaSpacesHyphen = auto(),

    UppercaseLettersPunctSpecialSpaces = auto(),
    LowercaseLettersPunctSpecialSpaces = auto(),
    UpperLowerLettersPunctSpecialSpaces = auto(),
    AccLettersCedillaPunctSpecialSpaces = auto(),

    Numbers = auto(),
    NumbersPunct = auto(),
    NumbersSpecial = auto(),
    NumbersSpaces = auto(),
    NumbersPunctSpaces = auto(),
    NumbersSpecialSpaces = auto(),
    NumbersPunctSpecialSpaces = auto(),

    UppercaseLettersNumbersPunctSpecialSpaces = auto(),
    LowercaseLettersNumbersPunctSpecialSpaces = auto(),
    UpperLowerLettersNumbersPunctSpecialSpaces = auto(),
    AccLettersCedillaNumbersPunctSpecialSpaces = auto(),

    AccLettersCedillaNumbersSpacesHyphen = auto(),  # Standard

    NonUnicode = auto(),
    AnyCharacter = auto(),


if __name__ == "__main__":
    pass
