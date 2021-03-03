"""
Author: Vaasudevan Srinivasan
Author Email: vaasuceg.96@gmail.com
Created on: May 08, 2017
Last Modified on: Dec 08, 2020
Description: Python package - cowsay
"""


from __future__ import print_function
import sys

from .characters import CHARS

__version__ = '3.0'
__name__ = 'cowsay'


char_names = CHARS.keys()

def wrap_lines(lines, max_width=49):
    # TODO: Wrap a line only at whitespaces
    new_lines = []
    for line in lines:
        for line_part in [
            line[i:i+max_width] for i in range(0, len(line), max_width)
        ]:
            new_lines.append(line_part)
    return new_lines


def string_processing(text):
    text = str(text)
    lines = [line.strip() for line in str(text).split("\n")]
    lines = [line for line in lines if line]
    lines = wrap_lines(lines)
    text_width = max([len(line) for line in lines])
    print("  " + "_" * text_width)
    if len(lines) > 1:
        print(" /" + " " * text_width + "\\")
    for line in lines:
        print("| " + line + " " * (text_width - len(line) + 1) + "|")
    if len(lines) > 1:
        print(" \\" + " " * text_width + "/")
    print("  " + "=" * text_width)                 
    return text_width
                    
    
# we are doing some magic here: Creating the functions dynamically.
# in .characters is a dict CHARS which holds the lines for the characters.
# For each entry there, we create a function.
# Wo do this, to not break the old API.

def draw(char, text):
    text_width = string_processing(text)
    flag = text_width
    char_lines = char.split('\n')
    char_lines = [i for i in char_lines if len(i) != 0]
    for line in char_lines:
        print(' ' * (flag - 0) + line)

chars = []
for char_name, char_lines in CHARS.items():
    def func(text, char_lines=char_lines):
        draw(char_lines, text)
    func.__name__ = char_name
    globals()[char_name] = func
    chars.append(func)

def cli():

    if '--version' in sys.argv[1:]:
        print(__version__)
        exit(0)

    cow(' '.join(sys.argv[1:]))

