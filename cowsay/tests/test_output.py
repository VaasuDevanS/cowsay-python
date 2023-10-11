import pytest

from cowsay import char_funcs, char_names
from . import solutions


@pytest.mark.parametrize('char', char_names, ids=char_names)
def test_char_solution(char, capsys):

    lorem: str = (
        'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam'
        'nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat,'
        'sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum.'
    )

    char_funcs[char](lorem)
    out, _ = capsys.readouterr()
    assert out == solutions.CHARS_SOLUTIONS[char].lstrip('\n')
