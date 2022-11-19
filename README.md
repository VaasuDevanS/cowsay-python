
[![cowsay](https://github.com/VaasuDevanS/cowsay-python/actions/workflows/cowsay.yaml/badge.svg?branch=main)](https://github.com/VaasuDevanS/cowsay-python/actions/workflows/cowsay.yaml)
[![PyPI version](https://badge.fury.io/py/Cowsay.svg)](https://badge.fury.io/py/Cowsay)
[![Github](https://img.shields.io/badge/github-cowsay--python-blue)](https://github.com/VaasuDevanS/cowsay-python)
[![Documentation](https://img.shields.io/badge/documentation-cowsay--python-informational)](https://vaasudevans.github.io/cowsay-python)
<br>
![](https://pepy.tech/badge/cowsay)
![](https://pepy.tech/badge/cowsay/month)
![](https://pepy.tech/badge/cowsay/week)

### `Latest version: 5.0 (Release Date: Jun 21, 2022)`

> A python API / console script for the famous linux `cowsay` <br>
> All contributions / pull requests are welcome; Check [here](https://github.com/VaasuDevanS/cowsay-python/graphs/contributors) to see the contributors <br>
> Take a look at [CHANGELOG.md](https://github.com/VaasuDevanS/cowsay-python/blob/main/CHANGELOG.md) for the changes


# Brief History
> cowsay for GNU/Linux was initially written in perl by Tony Monroe (tony@nog.net), with suggestions from Shannon Appel (appel@CSUA.Berkeley.EDU) and contributions from Anthony Polito (aspolito@CSUA.Berkeley.EDU).


# Installation
```console
pip install cowsay
```

# Documentation
Documentation was generated using [pdoc](https://github.com/mitmproxy/pdoc) using the following command
```console
pdoc -d google cowsay -o docs
```


# Basic Usage
```python
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

>>> worm = '''
 \
  \  _
    ("\
     ) )
    ( /
'''
>>> print(cowsay.get_output_string(worm, 'So much dust here..'))
  ___________________
| So much dust here.. |
  ===================
                    \
                     \  _
                       ("\
                        ) )
                       ( /
```


# More characters
- Custom characters
```console
>>> cowsay.get_output_string('custom character here', 'your text')
  _________
| your text |
  =========
         custom character here

>>> duck = r'''
 \
  \   __
    <(o )___
    ( ._> /
     `---'
'''
>>> console.get_output_string(duck, 'I am a duck')
  ___________
| I am a duck |
  ===========
            \
             \   __
               <(o )___
               ( ._> /
                `---'
```

- Pre-made characters
```console
>>> cowsay.char_names
['beavis', 'cheese', 'cow', 'daemon', 'dragon', 'fox', 'ghostbusters', 'kitty', 'meow', 'miki', 'milk', 'pig', 'stegosaurus', 'stimpy', 'trex', 'turkey', 'turtle', 'tux']


>>> cowsay.chars
{'beavis': <function func at 0x00000220913B4670>, 'cheese': <function func at 0x00000220913B4F70>, 'daemon': <function func at 0x00000220913D40D0>, 
 'cow': <function func at 0x00000220913D41F0>, 'dragon': <function func at 0x00000220913D4280>, 'fox': <function func at 0x00000220913D4310>, 
 'ghostbusters': <function func at 0x00000220913D43A0>, 'kitty': <function func at 0x00000220913D4430>, 'meow': <function func at 0x00000220913D44C0>, 
 'miki': <function func at 0x00000220913D4550>, 'milk': <function func at 0x00000220913D45E0>, 'pig': <function func at 0x00000220913D4670>, 
 'stegosaurus': <function func at 0x00000220913D4700>, 'stimpy': <function func at 0x00000220913D4790>, 'trex': <function func at 0x00000220913D4820>, 
 'turkey': <function func at 0x00000220913D48B0>, 'turtle': <function func at 0x00000220913D4940>, 'tux': <function func at 0x00000220913D49D0>}


>>> len(cowsay.chars)
18


>>> for char, char_func in cowsay.chars.items():
...     char_func(f'Hi! I am {char}')
  _______________
| Hi! I am beavis |
  ===============
                    \
                     \
                      \
                            _------~~-,
                         ,'            ,
                         /               \\
                        /                :
                       |                  '
                       |                  |
                       |                  |
                        |   _--           |
                        _| =-.     .-.   ||
                        o|/o/       _.   |
                        /  ~          \\ |
                      (____\@)  ___~    |
                         |_===~~~.`    |
                      _______.--~     |
                      \\________       |
                               \\      |
                             __/-___-- -__
                            /            _ \\
  _______________
| Hi! I am cheese |
  ===============
               \
                \
                 \
                  \
                    /     \_/         |
                   |                 ||
                   |                 ||
                  |    ###\  /###   | |
                  |     0  \/  0    | |
                 /|                 | |
                / |        <        |\ \
               | /|                 | | |
               | |     \_______/   |  | |
               | |                 | / /
               /||                 /|||
                  ----------------|
                       | |    | |
                       ***    ***
                      /___\  /___\
  _______________
| Hi! I am daemon |
  ===============
                       \
                        \
                         \
                          \
                           /- _  `-/  '
                          (/\/ \ \   /\
                          / /   | `    \
                          O O   ) /    |
                          `-^--'`<     '
                         (_.)  _  )   /
                          `.___/`    /
                            `-----' /
               <----.     __ / __   \
               <----|====O)))==) \) /====
               <----'    `--' `.__,' \
                            |        |
                             \       /
                       ______( (_  / \______
                     ,'  ,-----'   |        \
                     `--{__________)        \/
  ____________
| Hi! I am cow |
  ============
            \
             \
               ^__^
               (oo)\_______
               (__)\       )\/\
                   ||----w |
                   ||     ||
  _______________
| Hi! I am dragon |
  ===============
                 \
                  \
                   \
                    \
                                          / \\  //\\
                           |\\___/|      /   \\//  \\\\
                           /0  0  \\__  /    //  | \\ \\
                          /     /  \\/_/    //   |  \\  \\
                          \@_^_\@'/   \\/_   //    |   \\   \\
                          //_^_/     \\/_ //     |    \\    \\
                       ( //) |        \\///      |     \\     \\
                     ( / /) _|_ /   )  //       |      \\     _\\
                   ( // /) '/,_ _ _/  ( ; -.    |    _ _\\.-~        .-~~~^-.
                 (( / / )) ,-{        _      `-.|.-~-.           .~         `.
                (( // / ))  '/\\      /                 ~-. _ .-~      .-~^-.  \\
                (( /// ))      `.   {            }                   /      \\  \\
                 (( / ))     .----~-.\\        \\-'                 .~         \\  `. \\^-.
                            ///.----..>        \\             _ -~             `.  ^-`  ^-_
                              ///-._ _ _ _ _ _ _}^ - - - - ~                     ~-- ,.-~
                                                                                 /.-~
  ____________
| Hi! I am fox |
  ============
             \
              \
               \
                |\_/|,,_____,~~`
                (.".)~~     )`~}}
                 \o/\ /---~\\ ~}}
                   _//    _// ~}
  _____________________
| Hi! I am ghostbusters |
  =====================
                             \
                              \
                               \
                                \
                                            __---__
                                         _-       /--______
                                    __--( /     \ )XXXXXXXXXXX\v.
                                  .-XXX(   O   O  )XXXXXXXXXXXXXXX-
                                 /XXX(       U     )        XXXXXXX\
                               /XXXXX(              )--_  XXXXXXXXXXX\
                              /XXXXX/ (      O     )   XXXXXX   \XXXXX\
                              XXXXX/   /            XXXXXX   \__ \XXXXX
                              XXXXXX__/          XXXXXX         \__---->
                      ---___  XXX__/          XXXXXX      \__         /
                        \-  --__/   ___/\  XXXXXX            /  ___--/=
                         \-\    ___/    XXXXXX              '--- XXXXXX
                            \-\/XXX\ XXXXXX                      /XXXXX
                              \XXXXXXXXX   \                    /XXXXX/
                               \XXXXXX      >                 _/XXXXX/
                                 \XXXXX--__/              __-- XXXX/
                                  -XXXXXXXX---------------  XXXXXX-
                                     \XXXXXXXXXXXXXXXXXXXXXXXXXX/
                                       ""VXXXXXXXXXXXXXXXXXXV""
  ______________
| Hi! I am kitty |
  ==============
                 \
                  \
                   \
                    \
                     ("`-'  '-/") .___..--' ' "`-._
                      ` *_ *  )    `-.   (      ) .`-.__. `)
                       (_Y_.) ' ._   )   `._` ;  `` -. .-'
                    _.. `--'_..-_/   /--' _ .' ,4
                   ( i l ),-''  ( l i),'  ( ( ! .-'
  _____________
| Hi! I am meow |
  =============
             \
              \
               \
                \
                               _ ___.--'''`--''//-,-_--_.
                   \\`"' ` || \\\\ \\ \\\\/ / // / ,-\\\\`,_
                  /'`  \\ \\ || Y  | \\|/ / // / - |__ `-,
                 /\@"\\  ` \\ `\\ |  | ||/ // | \\/  \\  `-._`-,_.,
                /  _.-. `.-\\,___/\\ _/|_/_\\_\\/|_/ |     `-._._)
                `-'``/  /  |  // \\__/\\__  /  \\__/ \\
                     `-'  /-\\/  | -|   \\__ \\   |-' |
                       __/\\ / _/ \\/ __,-'   ) ,' _|'
                      (((__/(((_.' ((___..-'((__,'
  _____________
| Hi! I am miki |
  =============
             \                                                      
              \                  &************************&
               \             &******************************&
                \          &**********************************&
                         &**************************************&
                       &*****************************************&
                      &*******************************************& 
                     &*********************************************&
                    &***********************************************&
                   &************************************************&
                   &***#########********#########*******************&
                   &*##       ##########          ##################&
                   &*##   O   ##@**####   O       ##***************&
                   &***#########@*******#########*****************&
                   &***********@*********************************&
                   &**********@*********************************&
                   &*********@*********************************&
                   &********@@*********************************&
                    &*******@@@@@@****************************&   
                     &**************************************&
                       &**************************************&
                        &******@@@@@@@@@@@@*********************&
                          &*************************************&   
                            &************************************&
                                  &*******************************&
                                    &*****************************&
  _____________
| Hi! I am milk |
  =============
             \
              \
               \
                \
                    ____________
                    |__________|
                   /           /\
                  /           /  \
                 /___________/___/|
                 |          |     |
                 |  ==\ /== |     |
                 |   O   O  | \ \ |
                 |     <    |  \ \|
                /|          |   \ \
               / |  \_____/ |   / /
              / /|          |  / /|
             /||\|          | /||\/
                 -------------|
                     | |    | |
                    <__/    \__>
  ____________
| Hi! I am pig |
  ============
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
  ____________________
| Hi! I am stegosaurus |
  ====================
                          \
                           \
                            \
                             \
                                                .       .
                                               / `.   .' \
                                       .---.  <    > <    >  .---.
                                       |    \  \ - ~ ~ - /  /    |
                           _____        ~-..-~             ~-..-~
                          |     |   \~~~\.'                    `./~~~/
                         ---------   \__/                        \__/
                        .'  O    \     /               /       \  "
                       (_____,    `._.'               |         }  \/~~~/
                        `----.          /       }     |        /    \__/
                              `-.      |       /      |       /      `. ,~~|
                                  ~-.__|      /_ - ~ ^|      /- _      `..-'   f:  f:
                                       |     /        |     /     ~-.     `-. _|| _||_
                                       |_____|        |_____|         ~ - . _ _ _ _ __>
  _______________
| Hi! I am stimpy |
  ===============
                \
                 \
                  \
                   \
                       .    _  .
                      |\_|/__/|
                      / / \/ \  \
                     /__|O||O|__ \
                    |/_ \_/\_/ _\ |
                    | | (____) | ||
                    \/\___/\__/  //
                    (_/         ||
                     |          ||
                     |          ||\
                      \        //_/
                       \______//
                      __ || __||
                     (____(____)
  _____________
| Hi! I am trex |
  =============
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
  _______________
| Hi! I am turkey |
  ===============
                       \
                        \
                         \
                          \
                                                            ,+*^^*+___+++_
                                                      ,*^^^^              )
                                                   _+*                     ^**+_
                                                 +^       _ _++*+_+++_,         )
                             _+^^*+_    (     ,+*^ ^          \\+_        )
                            {       )  (    ,(    ,_+--+--,      ^)      ^\\
                           { (\@)    } f   ,(  ,+-^ __*_*_  ^^\\_   ^\\       )
                          {:;-/    (_+*-+^^^^^+*+*<_ _++_)_    )    )      /
                         ( /  (    (        ,___    ^*+_+* )   <    <      \\
                          U _/     )    *--<  ) ^\\-----++__)   )    )       )
                           (      )  _(^)^^))  )  )\\^^^^^))^*+/    /       /
                         (      /  (_))_^)) )  )  ))^^^^^))^^^)__/     +^^
                        (     ,/    (^))^))  )  ) ))^^^^^^^))^^)       _)
                         *+__+*       (_))^)  ) ) ))^^^^^^))^^^^^)____*^
                         \\             \\_)^)_)) ))^^^^^^^^^^))^^^^)
                          (_             ^\\__^^^^^^^^^^^^))^^^^^^^)
                            ^\\___            ^\\__^^^^^^))^^^^^^^^)\\\\
                                 ^^^^^\\uuu/^^\\uuu/^^^^\\^\\^\\^\\^\\^\\^\\^\\
                                    ___) >____) >___   ^\\_\\_\\_\\_\\_\\_\\)
                                   ^^^//\\\\_^^//\\\\_^       ^(\\_\\_\\_\\)
                                    ^^^ ^^ ^^^ ^
  _______________
| Hi! I am turtle |
  ===============
                 \
                  \
                   \
                    \
                                               ___-------___
                                           _-~~             ~~-_
                                        _-~                    /~-_
                      /^\__/^\         /~  \                   /    \
                    /|  O|| O|        /      \_______________/        \
                   | |___||__|      /       /                \          \
                   |          \    /      /                    \          \
                   |   (_______) /______/                        \_________ \
                   |         / /         \                      /            \
                    \         \^\\         \                  /               \     /
                      \         ||           \______________/      _-_       //\__//
                        \       ||------_-~~-_ ------------- \ --/~   ~\    || __/
                          ~-----||====/~     |==================|       |/~~~~~
                           (_(__/  ./     /                    \_\      \.
                                  (_(___/                         \_____)_)
  ____________
| Hi! I am tux |
  ============
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

# Command Line Usage
```console
$ cowsay Hello World
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