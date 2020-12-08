# Cowsay

![](https://pepy.tech/badge/cowsay)
![](https://pepy.tech/badge/cowsay/month)
![](https://pepy.tech/badge/cowsay/week)

A python API / console script for the famous linux-cowsay. <br>
All contributions / forks are welcome.

Brief History
==============

cowsay for GNU/Linux was initially written in perl by Tony Monroe (tony@nog.net), with suggestions from Shannon Appel (appel@CSUA.Berkeley.EDU) and contributions from Anthony Polito (aspolito@CSUA.Berkeley.EDU).

Check here for the [list](https://github.com/VaasuDevanS/cowsay-python/graphs/contributors) of contributors for this python package.


Installation
============
```
pip install cowsay
```


Basic Usage
===========

```
>>> import cowsay
>>> cowsay.cow('Hello World')
  ___________
< Hello World >
  ===========
                \
                 \
                   ^__^
                   (oo)\_______
                   (__)\       )\/\
                       ||----w |
                       ||     ||

>>> cowsay.dragon('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris blandit rhoncus nibh. Mauris mi mauris, molestie vel metus sit amet, aliquam vulputate nibh.')
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
                                                        \
                                                         \
                                                                               / \  //\
                                                                |\___/|      /   \//  \\
                                                                /0  0  \__  /    //  | \ \
                                                               /     /  \/_/    //   |  \  \
                                                               \@_^_\@'/   \/_   //    |   \   \
                                                               //_^_/     \/_ //     |    \    \
                                                            ( //) |        \///      |     \     \
                                                          ( / /) _|_ /   )  //       |      \     _\
                                                        ( // /) '/,_ _ _/  ( ; -.    |    _ _\.-~        .-~~~^-.
                                                      (( / / )) ,-{        _      `-.|.-~-.           .~         `.
                                                     (( // / ))  '/\      /                 ~-. _ .-~      .-~^-.  \
                                                     (( /// ))      `.   {            }                   /      \  \
                                                      (( / ))     .----~-.\        \-'                 .~         \  `. \^-.
                                                                 ///.----..>        \             _ -~             `.  ^-`  ^-_
                                                                   ///-._ _ _ _ _ _ _}^ - - - - ~                     ~-- ,.-~
                                                                                                                      /.-~



```


More characters
===============
```
>>> cowsay.char_names
['beavis', 'cheese', 'daemon', 'cow', 'dragon', 'ghostbusters', 'kitty', 'meow', 'milk', 'pig', 'stegosaurus', 'stimpy', 'turkey', 'turtle', 'tux']

>>> cowsay.chars[0]
<function beavis at 0x0000000002D2F908>

>>> len(cowsay.chars)
15
```
