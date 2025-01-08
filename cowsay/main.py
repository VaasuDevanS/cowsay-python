from __future__ import annotations
import re
import string

from .characters import CHARS

__version__ = '6.1'

CHARS: dict[str, str] = dict(sorted(CHARS.items()))
char_names: list[str] = list(CHARS.keys())


class CowsayError(LookupError):
    pass


def wrap_lines(lines: list, max_width: int = 49) -> list:

    # Buffers that will be used in the last.
    new_lines = []
    new_lines_width = []

    for line in lines:

        # Check whether the line width is overflow (greater than
        # max_width) because of half-width and full-width characters.
        line_buffer = ""
        line_width = 0

        # Loop over the characters in the line.
        for i, character in enumerate(line):

            if character in list(string.printable):
                # Half width characters.
                char_width = 1
            else:
                # Full width characters.
                char_width = 2

            # Check whether the `line_buffer` is overflowed.
            overflow = (line_width + char_width > max_width)

            if overflow:
                # Add `line_buffer` and `line_width`.
                new_lines.append(line_buffer)
                new_lines_width.append(line_width)

                # Reinitialize the `line_buffer` and `line_width`.
                line_buffer = character
                line_width = char_width
            else:
                # Add this character to `line_buffer` if not overflowed.
                line_buffer += character
                line_width += char_width

            if (i == (len(line) - 1)):
                # Last character.
                new_lines.append(line_buffer)
                new_lines_width.append(line_width)

    return new_lines, new_lines_width


def generate_bubble(text: str, max_width: int = 49) -> list:

    lines = [line.strip() for line in text.split('\n')]
    lines, lines_width = wrap_lines(
        lines=[line for line in lines if line], max_width=max_width)
    text_width = max(lines_width)

    output = ["  " + "_" * text_width]
    if len(lines) > 1:
        output.append(" /" + " " * text_width + "\\")
    for line, line_width in zip(lines, lines_width):
        output.append("| " + line + " " * (text_width - line_width + 1) + "|")
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


def draw(text: str, char_lines: str, to_console: bool = True,
         max_width: int = 49) -> None | str:

    if len(re.sub(r'\s', '', text)) == 0:
        raise CowsayError('Pass something meaningful to cowsay')

    output = generate_bubble(text, max_width=max_width)
    text_width = max([len(line) for line in output]) - 4  # 4 is the frame
    output += generate_char(char_lines, text_width)
    if to_console:
        for line in output:
            print(line)
    else:
        return '\n'.join(output)


def get_output_string(char: str, text: str, max_width: int = 49) -> str:

    if char in CHARS:
        return draw(text, CHARS[char], to_console=False, max_width=max_width)
    else:
        raise CowsayError(f'Available Characters: {char_names}')
