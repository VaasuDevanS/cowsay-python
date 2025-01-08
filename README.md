
[![cowsay](https://github.com/VaasuDevanS/cowsay-python/actions/workflows/cowsay.yaml/badge.svg?branch=main)](https://github.com/VaasuDevanS/cowsay-python/actions/workflows/cowsay.yaml)
[![codecov](https://codecov.io/gh/VaasuDevanS/cowsay-python/graph/badge.svg?token=GV4ntsCNtd)](https://codecov.io/gh/VaasuDevanS/cowsay-python)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/d5a358f5dd5c41d68db8c331d65fd0fd)](https://app.codacy.com/gh/VaasuDevanS/cowsay-python/dashboard)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/cowsay)
[![Github](https://img.shields.io/badge/github-cowsay--python-blue)](https://github.com/VaasuDevanS/cowsay-python)
<br>
![](https://img.shields.io/badge/Latest%20Release-Sep%2025,%202023-blue)
[![Downloads](https://static.pepy.tech/badge/cowsay)](https://pepy.tech/project/cowsay)
[![Downloads](https://static.pepy.tech/badge/cowsay/month)](https://pepy.tech/project/cowsay)
[![Downloads](https://static.pepy.tech/badge/cowsay/week)](https://pepy.tech/project/cowsay)


# Introduction

A python API / Command-line tool for the famous linux `cowsay`. <br>
Take a look at [CHANGELOG.md](https://github.com/VaasuDevanS/cowsay-python/blob/main/CHANGELOG.md) for the changes.


# Brief History
`cowsay` for GNU/Linux was initially written in perl by Tony Monroe. More info 
[here](https://en.wikipedia.org/wiki/Cowsay).


# Installation
```console
pip install cowsay
```


# API Usage
```pycon
>>> import cowsay

>>> cowsay.cow('Hello World')
 ___________
| Hello World |
  ===========
           \
            \
              ^__^
              (oo)\_______
              (__)\       )\/\
                  ||----w |
                  ||     ||


>>> print(cowsay.get_output_string('cow', 'Hello World'))
  ___________
| Hello World |
  ===========
           \
            \
              ^__^
              (oo)\_______
              (__)\       )\/\
                  ||----w |
                  ||     ||


>>> cowsay.cow('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris blandit rhoncus nibh. Mauris mi mauris, molestie vel metus sit amet, aliquam vulputate nibh.')
  _________________________________________________
 /                                                 \
| Lorem ipsum dolor sit amet, consectetur adipiscin |
| g elit. Mauris blandit rhoncus nibh. Mauris mi ma |
| uris, molestie vel metus sit amet, aliquam vulput |
| ate nibh.                                         |
 \                                                 /
  =================================================
                                                 \
                                                  \
                                                    ^__^
                                                    (oo)\_______
                                                    (__)\       )\/\
                                                        ||----w |
                                                        ||     ||


>>> my_fish = r'''
\
 \  
        /`·.¸
     /¸...¸`:·
 ¸.·´  ¸   `·.¸.·´)
: © ):´;      ¸  {
 `·.¸ `·  ¸.·´\`·¸)
     `\\´´\¸.·´
'''

>>> cowsay.draw('Sharks are my best friend', my_fish)
  _________________________
| Sharks are my best friend |
  =========================
                         \
                          \  
                                 /`·.¸
                              /¸...¸`:·
                          ¸.·´  ¸   `·.¸.·´)
                         : © ):´;      ¸  {
                          `·.¸ `·  ¸.·´\`·¸)
                              `\\´´\¸.·´
```


# Command Line Usage
```console
$ cowsay -t "Hello World"
  ___________
| Hello World |
  ===========
           \
            \
              ^__^
              (oo)\_______
              (__)\       )\/\
                  ||----w |
                  ||     ||


$ cowsay -t "Hello World" -c "tux"
  ___________
| Hello World |
  ===========
                \
                 \
                  \
                   .--.
                  |o_o |
                  |:_/ |
                 //   \ \
                (|     | )
               /'\_   _/`\
               \___)=(___/
```


# More Characters
```pycon
>>> cowsay.char_names
['beavis', 'cheese', 'cow', 'daemon', 'dragon', 'fox', 'ghostbusters', 'kitty', 'mashiro', 'meow', 'miki', 'milk', 'octopus', 'pig', 'stegosaurus', 'stimpy', 'trex', 
'turkey', 'turtle', 'tux']


>>> cowsay.char_funcs
{'beavis': <function func at 0x104b734c0>, 
'cheese': <function func at 0x104d285e0>, 
...
'tux': <function func at 0x104d28f70>}


>>> len(cowsay.chars)
19
```

# Contributers
<a href="https://github.com/VaasuDevanS/cowsay-python/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=VaasuDevanS/cowsay-python&columns=5" />
</a>

Guide: [CONTRIBUTING.md](https://github.com/VaasuDevanS/cowsay-python/blob/main/CONTRIBUTING.md)


# Star History
[![Star History Chart](https://api.star-history.com/svg?repos=VaasuDevanS/cowsay-python&type=Date)](https://star-history.com/#VaasuDevanS/cowsay-python&Date)
