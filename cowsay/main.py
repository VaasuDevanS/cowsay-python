from __future__ import print_function
import sys
import re
import argparse

from .characters import CHARS

__version__ = '4.0'
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

def draw(char, text, to_console=True):
    if len(re.sub('\s', '', text)) == 0:
        raise Exception('Pass something meaningful to cowsay')
    output = generate_bubble(text)
    text_width = max([len(line) for line in output]) - 4  # 4 is the frame
    output += generate_char(char, text_width)
    if to_console:
        for line in output:
            print(line)
    return '\n'.join(output)


chars = {}
for char_name, char_lines in CHARS.items():
    def func(text, char_lines=char_lines):
        draw(char_lines, text)
    func.__name__ = char_name
    globals()[char_name] = func
    chars[char_name] = func
    

def get_output_string(char_name, text):
    if char_name in CHARS:
        return draw(CHARS[char_name], text, to_console=False)
    else:
        raise Exception('Available Characters: ', list(CHARS.keys()))


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument('echo', help='say something',nargs='?',default='Oops')
    parser.add_argument('-l', '--list', action='store_true',
                    help='show characters')
    parser.add_argument('-v', '--version', action='store_true',
                    help='show the version')
    parser.add_argument('-f',  '--character',
                    help='use specific character')
    args = parser.parse_args()

    if args.version:
        print(__version__)
        exit(0)
    
    if args.list:
        print('Available Characters:' + ' '.join(CHARS.keys()))
        exit(0)
    
    if args.character is None:
        cow(args.echo)
        exit(0)
    
    if (args.character in chars):
        print(get_output_string(args.character, args.echo))
    else:
        cow(args.echo)