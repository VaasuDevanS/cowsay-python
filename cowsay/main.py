from __future__ import print_function # for backwards compatibility

import sys
from .characters import CHARS

__version__ = '5.0'

char_names = list(CHARS.keys())

def wrap_lines(
    lines: list,
    max_width: int = 49
    ) -> list[str]:
    """
    wrap_lines(lines, max width) -> wrapped lines

    Wraps all lines in a box, so it doesn't overflow

    :param lines list: List of lines
    :param max_width int: Max width
    :returns list[str]: Wrapped lines
    """

    new_lines = []

    for line in lines:
        for line_part in [
            line[i:i+max_width] for i in range(0, len(line), max_width)
            ]:
            new_lines.append(line_part)

    return new_lines

def generate_bubble(
    text: str
    ) -> list[str]:
    """
    generate_bubble(text) -> bubble

    Creates a chat bubble around the text

    :param text str: Text to put in the bubble
    :returns list[str]: The bubble
    """

    lines = [
        line.strip()
        for line in str(text).split("\n")
        if line
    ]

    lines = wrap_lines([
        line
        for line in lines
    ])

    text_width = max([
        len(line)
        for line in lines
    ])

    output = []
    output.append("  " + "_" * text_width)

    if len(lines) > 1:
        output.append(
            " /"
            + (" " * text_width)
            + "\\"
        )

    for line in lines:
        output.append((
            "| "
            + line
            + " " * (text_width - len(line) + 1)
            + "|"
        ))

    if len(lines) > 1:
        output.append((
            " \\"
            + (" " * text_width)
            + "/"
        ))

    output.append((
        "  "
        + ("=" * text_width)
    ))

    return output

def generate_char(
    char: str,
    text_width: int
    ) -> list[str]:
    """
    generate_char(character, text width) -> properly aligned character

    Aligns the character to match the text length

    :param char str: Character art
    :param text_width int: Width of the text
    :returns list[str]: Characters with proper alignment
    """

    output = []

    char_lines = char.split('\n')
    char_lines = [
        i
        for i in char_lines
        if len(i) != 0
    ]

    for line in char_lines:
        output.append(' ' * text_width + line)

    return output

def draw(
    char: str,
    text: str,
    to_console: bool = True
    ) -> str:
    """
    draw(character, text, print to console) -> character with text bubble

    Adds the text bubble and aligns the character

    :param char str: Character art
    :param text str: Text to display in the bubble
    :param to_console bool: Print to console
    :returns str: Character with the text bubble
    """

    if len(text) == 0:
        raise Exception('Pass something meaningful to cowsay')

    output = generate_bubble(text)

    text_width = max([
        len(line)
        for line in output
    ]) - 4  # 4 is the frame

    output += generate_char(char, text_width)

    if to_console:
        for line in output:
            print(line)

    return '\n'.join(output)

# We are doing some magic here: Creating the functions dynamically.
# In .characters is a dict (CHARS) which holds all the lines for the characters.
# For each entry there we create a function.
# Wo do this to not break the old API.

chars = {}
for char_name, char_lines in CHARS.items():

    def func(text, char_lines=char_lines):
        draw(char_lines, text)

    func.__name__ = char_name
    globals()[char_name] = func
    chars[char_name] = func

def get_output_string(
    char: str,
    text: str
    ) -> str:
    """
    get_output_string(character, text) -> character with the text bubble

    Gets the character and text bubble

    :param char str: Character to use
    :param text str: text to put in the text bubble
    :returns str: Character with the text bubble
    """

    if char in CHARS:
        char = CHARS[char]

    return draw(
        char,
        text,
        to_console = False
    )

def cli() -> None:
    """
    cli() -> nothing

    Parses arguments from the Command Line Interface

    :returns None: Nothing
    """

    if '--version' in sys.argv[1:]:
        print(__version__)
        exit(0)

    if '--character' in sys.argv[1:]:
        character_index = sys.argv.index('--character')

        try:
            character = globals()[sys.argv[character_index + 1]]
            del sys.argv[character_index: character_index + 2]

        except (KeyError, IndexError):
            options = ', '.join(char_names)
            raise LookupError(
                'Invalid character selection passed. Available options: ' + options
            )
    else:
        character = cow

    character(' '.join(sys.argv[1:]))
