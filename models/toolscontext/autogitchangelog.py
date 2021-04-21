#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Module short description.

   Module long description...
"""

__author__ = "Vinícius Pereira"
__copyright__ = "Copyright YYYY, My Project"
__credits__ = ["Vinícius Pereira","etc."]
__date__ = "YYYY/MM/DD"
__license__ = "GPL"
__version__ = "1.0.0"
__pythonversion__ = "3.9.1"
__maintainer__ = "Vinícius Pereira"
__contact__ = "viniciuspsb@gmail.com"
__status__ = "Development"
__deprecated__ = "False"

import os


def generate_gitchangelog() -> None:
    """
    Short description.

    Args:
        ...

    Returns:
        None.
    """
    os.system("git-changelog . -o CHANGELOG.MD -s angular -t angular")

    with open("CHANGELOG.MD","r+") as file:
        lines = file.readlines()

        part1 = lines[:+1]
        part1 = ''.join(part1)
        
        part2 = lines[+1:]
        part2 = ''.join(part2)
        part2 = part2.replace("<a name=", "#\n<a name=")

        content = part1 + part2
        
        file.seek(0)
        file.write("# Changelog\n" + content)
        

if __name__ == "__main__":
    generate_gitchangelog()