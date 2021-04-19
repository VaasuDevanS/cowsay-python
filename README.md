# Cowsay

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
['beavis', 'cheese', 'daemon', 'cow', 'dragon', 'ghostbusters', 'kitty', 'meow', 'milk', 'pig', 'stegosaurus', 'stimpy', 'trex', 'turkey', 'turtle', 'tux']

>>> cowsay.chars
{'beavis': <function func at 0x000002339858E310>, 'cheese': <function func at 0x000002339858E3A0>, 'daemon': <function func at 0x000002339858E430>, 'cow': <function func at 0x000002339858E4C0>, 'dragon': <function func at 0x000002339858E550>, 'ghostbusters': <function func at 0x000002339858E5E0>, 'kitty': <function func at 0x000002339858E670>, 'meow': <function func at 0x000002339858E700>, 'milk': <function func at 0x000002339858E790>, 'pig': <function func at 0x000002339858E820>, 'stegosaurus': <function func at 0x000002339858E8B0>, 'stimpy': <function func at 0x000002339858E940>, 'trex': <function func at 0x000002339858E9D0>, 'turkey': <function func at 0x000002339858EA60>, 'turtle': <function func at 0x000002339858EAF0>, 'tux': <function func at 0x000002339858EB80>}

>>> len(cowsay.chars)
16
```
