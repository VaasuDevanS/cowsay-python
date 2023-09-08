import argparse

from . import CowsayError, char_names, char_funcs


def cli():

    parser = argparse.ArgumentParser(
        prog='Cowsay',
        description='CLI tool to display text in ASCII art. '
                    f'Available Characters: {char_names}'
    )

    parser.add_argument('-c', '--character',
                        default='cow')

    parser.add_argument('-t', '--text',
                        required=True)

    args = parser.parse_args()

    if args.character not in char_names:
        raise CowsayError(f'Available Characters: {char_names}')

    char_funcs[args.character](args.text)


if __name__ == "__main__":

    cli()
