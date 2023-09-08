from .main import (

    __version__,

    # Variables
    char_names,
    CHARS,

    # Methods
    get_output_string,
    draw,

    CowsayError,

)

# This is where we create functions for each character dynamically

char_funcs = {}

for ch_name, ch_lines in CHARS.items():

    def func(text: str, char_lines=ch_lines):
        draw(str(text), char_lines)

    func.__name__ = ch_name
    globals()[ch_name] = func
    char_funcs[ch_name] = func
