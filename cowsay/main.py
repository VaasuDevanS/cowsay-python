import re
import textwrap

from .characters import CHARS

__version__ = '6.0'

CHARS = dict(sorted(CHARS.items()))
char_names = list(CHARS.keys())


class CowsayError(LookupError):
    pass


def generate_bubble(text: str) -> list:

    text = textwrap.fill(text, width=49)
    lines = [line.strip() for line in text.splitlines()]
    text_width = max([len(line) for line in lines])

    output = ["  " + "_" * text_width]
    if len(lines) > 1:
        output.append(" /" + " " * text_width + "\\")
    for line in lines:
        output.append("| " + line + " " * (text_width - len(line) + 1) + "|")
    if len(lines) > 1:
        output.append(" \\" + " " * text_width + "/")
    output.append("  " + "=" * text_width)

    return output


def generate_char(char_lines: str, text_width: int) -> list:

    output = []
    char_lines = char_lines.split('\n')
    char_lines = [i for i in char_lines if len(i) != 0]
    for line in char_lines:
        output.append(' ' * text_width + line)
    return output


def draw(text: str, char_lines: str, to_console: bool = True) -> str:

    if len(re.sub(r'\s', '', text)) == 0:
        raise CowsayError('Pass something meaningful to cowsay')

    output = generate_bubble(text)
    text_width = max([len(line) for line in output]) - 4  # 4 is the frame
    output += generate_char(char_lines, text_width)
    if to_console:
        for line in output:
            print(line)
    else:
        return '\n'.join(output)


def get_output_string(char: str, text: str) -> str:

    if char in CHARS:
        return draw(text, CHARS[char], to_console=False)
    else:
        raise CowsayError(f'Available Characters: {char_names}')
