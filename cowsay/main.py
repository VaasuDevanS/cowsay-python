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

def generate_bubble(text):
    lines = [line.strip() for line in str(text).split("\n")]
    lines = wrap_lines([line for line in lines if line])
    text_width = max([len(line) for line in lines])
    output = []
    output.append("  " + "_" * text_width)
    if len(lines) > 1:
        output.append(" /" + " " * text_width + "\\")
    for line in lines:
        output.append("| " + line + " " * (text_width - len(line) + 1) + "|")
    if len(lines) > 1:
        output.append(" \\" + " " * text_width + "/")
    output.append("  " + "=" * text_width)                 
    return output

def generate_char(char, text_width):
    output = []
    char_lines = char.split('\n')
    char_lines = [i for i in char_lines if len(i) != 0]
    for line in char_lines:
        output.append(' ' * text_width + line)
    return output


# we are doing some magic here: Creating the functions dynamically.
# in .characters is a dict CHARS which holds the lines for the characters.
# For each entry there, we create a function.
# Wo do this, to not break the old API.

def draw(char, text):
    output = generate_bubble(text)
    text_width = max([len(line) for line in output]) - 4  # 4 is the frame
    output += generate_char(char, text_width)
    for line in output:
        print(line)

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

