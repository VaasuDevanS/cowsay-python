import pytest

import cowsay


def test_char_names():

    characters = ['beavis', 'cheese', 'daemon', 'cow', 'dragon',
                  'ghostbusters', 'kitty', 'kitten', 'meow', 'milk', 'stegosaurus',
                  'stimpy', 'turkey', 'turtle', 'tux',
                  'pig', 'trex', 'miki', 'fox', 'octopus']

    assert len(cowsay.char_names) == len(characters)
    assert cowsay.char_names == sorted(characters)


def test_draw_error():
    with pytest.raises(cowsay.CowsayError) as e:
        cowsay.draw('', '')
    assert e.value.args[0] == 'Pass something meaningful to cowsay'


def test_get_output_string():
    assert isinstance(cowsay.get_output_string(char='cow', text='Hello'), str)


def test_get_output_string_error():
    with pytest.raises(cowsay.CowsayError) as e:
        cowsay.get_output_string('random', 'random text')
    assert e.value.args[0] == f'Available Characters: {cowsay.char_names}'
