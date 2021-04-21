#!/usr/bin/env python

__author__ = "Vinícius Pereira"
__copyright__ = "Copyright 2021, Vinícius Pereira"
__credits__ = "Vinícius Pereira"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Vinícius Pereira"
__email__ = "viniciuspsb@gmail.com"
__status__ = "Development"

import sys, os
from enum import Enum, auto


class BuildMode(Enum):
    onedir = auto(),
    onefile = auto()

class ApplicationMode(Enum):
    console = auto(),
    windowed = auto()


if __name__ == "__main__":
    pass
