import argparse
import sys

from . import CowsayError, char_names, char_funcs, __version__


def cli():

    parser = argparse.ArgumentParser(
        prog='Cowsay',
        description='CLI tool to display text in ASCII art. '
                    f'Available Characters: {char_names}'
    )

    parser.add_argument('-c', '--character',
                        default='cow')

    parser.add_argument('-t', '--text',
                        help='Text to display. If not provided, reads from stdin.')

    parser.add_argument('-v', '--version',
                        action='version', version=__version__)

    args = parser.parse_args()

    if args.character not in char_names:
        raise CowsayError(f'Available Characters: {char_names}')

    if args.text:
        text = args.text
    else:
        if sys.stdin.isatty():
            parser.error('Text argument is required if not piping input.')
        text = sys.stdin.read().strip()

    char_funcs[args.character](text)


if __name__ == "__main__":

    cli()
