# Cowsay

[![cowsay](https://github.com/VaasuDevanS/cowsay-python/actions/workflows/cowsay.yaml/badge.svg?branch=main)](https://github.com/VaasuDevanS/cowsay-python/actions/workflows/cowsay.yaml)
![](https://pepy.tech/badge/cowsay)
![](https://pepy.tech/badge/cowsay/month)
![](https://pepy.tech/badge/cowsay/week)

A python API / console script for the famous linux-cowsay. <br>
All contributions / forks are welcome. <br>
Take a look at CHANGELOG.md for the changes.

Brief History
==============

cowsay for GNU/Linux was initially written in perl by Tony Monroe (tony@nog.net), with suggestions from Shannon Appel (appel@CSUA.Berkeley.EDU) and contributions from Anthony Polito (aspolito@CSUA.Berkeley.EDU).

Check [here](https://github.com/VaasuDevanS/cowsay-python/graphs/contributors) for the list of contributors for this python package. <br>
Check [here](https://github.com/VaasuDevanS/cowsay-python/blob/master/CHANGELOG.md) for the change log.


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


>>> print(cowsay.get_output_string('trex', 'Hello (extinct) World'))
  _____________________
| Hello (extinct) World |
  =====================
                            \
                             \
                              \
                               \
                                  .-=-==--==--.
                            ..-=="  ,'o`)      `.
                          ,'         `"'         \
                         :  (                     `.__...._
                         |                  )    /         `-=-.
                         :       ,vv.-._   /    /               `---==-._
                          \/\/\/VV ^ d88`;'    /                         `.
                              ``  ^/d88P!'    /             ,              `._
                                 ^/    !'   ,.      ,      /                  "-,,__,,--'""""-.
                                ^/    !'  ,'  \ . .(      (         _           )  ) ) ) ))_,-.\
                               ^(__ ,!',"'   ;:+.:%:a.     \:.. . ,'          )  )  ) ) ,"'    '
                               ',,,'','     /o:::":%:%a.    \:.:.:         .    )  ) _,'
                                """'       ;':::'' `+%%%a._  \%:%|         ;.). _,-""
                                       ,-='_.-'      ``:%::)  )%:|        /:._,"
                                      (/(/"           ," ,'_,'%%%:       (_,'
                                                     (  (//(`.___;        \
                                                      \     \    `         `
                                                       `.    `.   `.        :
                                                         \. . .\    : . . . :
                                                          \. . .:    `.. . .:
                                                           `..:.:\     \:...\
                                                            ;:.:.;      ::...:
                                                            ):%::       :::::;
                                                        __,::%:(        :::::
                                                     ,;:%%%%%%%:        ;:%::
                                                       ;,--""-.`\  ,=--':%:%:\
                                                      /"       "| /-".:%%%%%%%\
                                                                      ;,-"'`)%%)
                                                                     /"      "|


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
['beavis', 'cheese', 'cow', 'daemon', 'dragon', 'fox', 'ghostbusters', 'kitty', 'meow', 'miki', 'milk', 'pig', 'stegosaurus', 'stimpy', 'trex', 'turkey', 'turtle', 'tux']

>>> cowsay.chars
{'beavis': <function func at 0x00000220913B4670>, 'cheese': <function func at 0x00000220913B4F70>, 'daemon': <function func at 0x00000220913D40D0>, 'cow': <function func at 0x00000220913D41F0>, 'dragon': <function func at 0x00000220913D4280>, 'fox': <function func at 0x00000220913D4310>, 'ghostbusters': <function func at 0x00000220913D43A0>, 'kitty': <function func at 0x00000220913D4430>, 'meow': <function func at 0x00000220913D44C0>, 'miki': <function func at 0x00000220913D4550>, 'milk': <function func at 0x00000220913D45E0>, 'pig': <function func at 0x00000220913D4670>, 'stegosaurus': <function func at 0x00000220913D4700>, 'stimpy': <function func at 0x00000220913D4790>, 'trex': <function func at 0x00000220913D4820>, 'turkey': <function func at 0x00000220913D48B0>, 'turtle': <function func at 0x00000220913D4940>, 'tux': <function func at 0x00000220913D49D0>}

>>> len(cowsay.chars)
18
```

Command Line Usage
==================

```
$ cowsay Hello World
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


$ cowsay --character pig Hello World
  ___________
| Hello World |
  ===========
           \
            \
             \
              \
                        ,.
                       (_|,.
                       ,' /, )_______   _
                   __j o``-'        `.'-)'
                   (")                 \'
                   `-j                |
                       `-._(           /
                           |_\  |--^.  /
                       /_]'|_| /_)_/
                           /_]'  /_]'


$ cowsay Hello World --character tux
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
