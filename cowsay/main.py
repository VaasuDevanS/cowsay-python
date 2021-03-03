"""
Author: Vaasudevan Srinivasan
Author Email: vaasuceg.96@gmail.com
Created on: May 08, 2017
Last Modified on: Dec 08, 2020
Description: Python package - cowsay
"""


from __future__ import print_function
import re
import sys


__version__ = '3.0'
__name__ = 'cowsay'

Beavis = r'''
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
             
            '''

Cheese = ''' 

     /     \\_/         |
    |                 ||
    |                 ||
   |    ###\\  /###   | |
   |     0  \\/  0    | |
  /|                 | |
 / |        <        |\\ \\
| /|                 | | |
| |     \\_______/   |  | |
| |                 | / /
/||                 /|||
   ----------------|
        | |    | |
        ***    ***
       /___\\  /___\\
       
       '''

Daemon = ''' 
            /- _  `-/  '
           (/\\/ \\ \\   /\\
           / /   | `    \\
           O O   ) /    |
           `-^--'`<     '
          (_.)  _  )   /
           `.___/`    /
             `-----' /
<----.     __ / __   \\
<----|====O)))==) \\) /====
<----'    `--' `.__,' \\
             |        |
              \\       /
        ______( (_  / \\______
      ,'  ,-----'   |        \\
      `--{__________)        \\/
      
       '''

Cow = r'''

   ^__^                             
   (oo)\_______                   
   (__)\       )\/\             
       ||----w |           
       ||     ||  
       
       '''

Dragon = r''' 

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
         
         '''

Ghostbusters = ''' 
                       __---__
                    _-       /--______
               __--( /     \\ )XXXXXXXXXXX\\v.
             .-XXX(   O   O  )XXXXXXXXXXXXXXX-
            /XXX(       U     )        XXXXXXX\\
          /XXXXX(              )--_  XXXXXXXXXXX\\
         /XXXXX/ (      O     )   XXXXXX   \\XXXXX\\
         XXXXX/   /            XXXXXX   \\__ \\XXXXX
         XXXXXX__/          XXXXXX         \\__---->
 ---___  XXX__/          XXXXXX      \\__         /
   \\-  --__/   ___/\\  XXXXXX            /  ___--/=
    \\-\\    ___/    XXXXXX              '--- XXXXXX
       \\-\\/XXX\\ XXXXXX                      /XXXXX
         \\XXXXXXXXX   \\                    /XXXXX/
          \\XXXXXX      >                 _/XXXXX/
            \\XXXXX--__/              __-- XXXX/
             -XXXXXXXX---------------  XXXXXX-
                \\XXXXXXXXXXXXXXXXXXXXXXXXXX/
                  ""VXXXXXXXXXXXXXXXXXXV""
                  
            '''

Kitty = ''' 

     ("`-'  '-/") .___..--' ' "`-._
         ` *_ *  )    `-.   (      ) .`-.__. `)
         (_Y_.) ' ._   )   `._` ;  `` -. .-'
      _.. `--'_..-_/   /--' _ .' ,4
   ( i l ),-''  ( l i),'  ( ( ! .-'  
        
        '''

Meow = r"""

                  _ ___.--'''`--''//-,-_--_.
      \\`"' ` || \\\\ \\ \\\\/ / // / ,-\\\\`,_
     /'`  \\ \\ || Y  | \\|/ / // / - |__ `-,
    /\@"\\  ` \\ `\\ |  | ||/ // | \\/  \\  `-._`-,_.,
   /  _.-. `.-\\,___/\\ _/|_/_\\_\\/|_/ |     `-._._)
   `-'``/  /  |  // \\__/\\__  /  \\__/ \\
        `-'  /-\\/  | -|   \\__ \\   |-' |
          __/\\ / _/ \\/ __,-'   ) ,' _|'
         (((__/(((_.' ((___..-'((__,'
         
        """

Milk = ''' 

       ____________ 
       |__________|
      /           /\\
     /           /  \\
    /___________/___/|
    |          |     |
    |  ==\\ /== |     |
    |   O   O  | \\ \\ |
    |     <    |  \\ \\|
   /|          |   \\ \\
  / |  \\_____/ |   / /
 / /|          |  / /|
/||\\|          | /||\\/
    -------------|   
        | |    | | 
       <__/    \\__>
       
       '''

Pig = r'''
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

      '''

Stegosaurus = '''                    
                                     / `.   .' " 
                             .---.  <    > <    >  .---.
                             |    \\  \\ - ~ ~ - /  /    |
         _____          ..-~             ~-..-~
        |     |   \\~~~\\.'                    `./~~~/
       ---------   \\__/                        \\__/
      .'  O    \\     /               /       \\  " 
     (_____,    `._.'               |         }  \\/~~~/
      `----.          /       }     |        /    \\__/
            `-.      |       /      |       /      `. ,~~|
                ~-.__|      /_ - ~ ^|      /- _      `..-'   
                     |     /        |     /     ~-.     `-. _  _  _
                     |_____|        |_____|         ~ - . _ _ _ _ _>

              '''

Stimpy = ''' 
        .    _  .    
       |\\_|/__/|    
       / / \\/ \\  \\  
      /__|O||O|__ \\ 
     |/_ \\_/\\_/ _\\ |  
     | | (____) | ||  
     \\/\\___/\\__/  // 
     (_/         ||
      |          ||
      |          ||\\   
       \\        //_/  
        \\______//
       __ || __||
      (____(____)
      
        '''

Turkey = r'''

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
                      
           '''

Turtle = ''' 

                                               ___-------___
                                           _-~~             ~~-_
                                        _-~                    /~-_
             /^\\__/^\\         /~  \\                   /    \\
           /|  O|| O|        /      \\_______________/        \\
          | |___||__|      /       /                \\          \\
          |          \\    /      /                    \\          \\
          |   (_______) /______/                        \\_________ \\
          |         / /         \\                      /            \\
           \\         \\^\\\\         \\                  /               \\     /
             \\         ||           \\______________/      _-_       //\\__//
               \\       ||------_-~~-_ ------------- \\ --/~   ~\\    || __/
                 ~-----||====/~     |==================|       |/~~~~~
                  (_(__/  ./     /                    \\_\\      \\.
                         (_(___/                         \\_____)_)


        '''

Tux = ''' 

        .--.
       |o_o |
       |:_/ |
      //   \\ \\
     (|     | )
    /'\\_   _/`\\
    \\___)=(___/
    
    '''


def wrap_lines(lines, max_width=49):
    # TODO: Wrap a line only at whitespaces
    new_lines = []
    for line in lines:
        for line_part in [
            line[i:i+max_width] for i in range(0, len(line), max_width)
        ]:
            new_lines.append(line_part)
    return new_lines


def string_processing(text):
    text = str(text)
    lines = [line.strip() for line in str(text).split("\n")]
    lines = [line for line in lines if line]
    lines = wrap_lines(lines)
    text_width = max([len(line) for line in lines])
    print("  " + "_" * text_width)
    if len(lines) > 1:
        print(" /" + " " * text_width + "\\")
    for line in lines:
        print("| " + line + " " * (text_width - len(line) + 1) + "|")
    if len(lines) > 1:
        print(" \\" + " " * text_width + "/")
    print("  " + "=" * text_width)                 
    return text_width
                    
    
def beavis(args):

    try:

        text_width = string_processing(args)
        flag = text_width

        print(' ' * (flag + 5) + '\\')
        print(' ' * (flag + 6) + '\\')
        print(' ' * (flag + 7) + '\\')

        char_lines = Beavis.split('\n')
        char_lines = [i for i in char_lines if len(i) != 0]

        for i in char_lines:
            print(' ' * flag + i)

    except:
        print("Can't Say...!! Give something much more easier to Mr.Beavis...")


def cheese(args):

    try:

        text_width = string_processing(args)
        flag = text_width

        print(' ' * (flag + 5) + '\\')
        print(' ' * (flag + 6) + '\\')
        print(' ' * (flag + 7) + '\\')
        print(' ' * (flag + 8) + '\\', end='')

        char_lines = Cheese.split('\n')
        char_lines = [i for i in char_lines if len(i) != 0]

        for i in char_lines:
            print(' ' * (flag + 5) + i)

    except:
        print("Can't Say...!! Give something much more easier to Mr.Cheese...")


def daemon(args):

    try:

        text_width = string_processing(args)
        flag = text_width

        print(' ' * (flag + 5) + '\\')
        print(' ' * (flag + 6) + '\\')
        print(' ' * (flag + 7) + '\\')
        print(' ' * (flag + 8) + '\\', end='')

        char_lines = Daemon.split('\n')
        char_lines = [i for i in char_lines if len(i) != 0]

        for i in char_lines:
            print(' ' * (flag - 3) + i)

    except:
        print("Can't Say...!! Give something much more easier to Mr.Daemon...")


def cow(args):

    try:

        text_width = string_processing(args)
        flag = text_width

        print(' ' * (flag + 5) + '\\')
        print(' ' * (flag + 6) + '\\')

        char_lines = Cow.split('\n')
        char_lines = [i for i in char_lines if len(i) != 0]

        for i in char_lines:
            print(' ' * (flag + 5) + i)

    except:
        print("Can't Say...!! Give something much more easier to Mr.Cow...")


def dragon(args):

    try:

        text_width = string_processing(args)
        flag = text_width

        print(' ' * (flag + 5) + '\\')
        print(' ' * (flag + 6) + '\\')
        print(' ' * (flag + 7) + '\\')
        print(' ' * (flag + 8) + '\\', end='')

        char_lines = Dragon.split('\n')
        char_lines = [i for i in char_lines if len(i) != 0]

        for i in char_lines:
            print(' ' * (flag + 3) + i)

    except:
        print("Can't Say...!! Give something much more easier to Mr.Dragon...")


def ghostbusters(args):

    try:

        text_width = string_processing(args)
        flag = text_width

        print(' ' * (flag + 5) + '\\')
        print(' ' * (flag + 6) + '\\')
        print(' ' * (flag + 7) + '\\')
        print(' ' * (flag + 8) + '\\', end='')

        char_lines = Ghostbusters.split('\n')
        char_lines = [i for i in char_lines if len(i) != 0]

        for i in char_lines:
            print(' ' * (flag - 3) + i)

    except:
        print("Can't Say...!! Give something much more easier to"
              "Mr.Ghostbusters...")


def kitty(args):

    try:

        text_width = string_processing(args)
        flag = text_width

        print(' ' * (flag + 5) + '\\')
        print(' ' * (flag + 6) + '\\')
        print(' ' * (flag + 7) + '\\')
        print(' ' * (flag + 8) + '\\')

        char_lines = Kitty.split('\n')
        char_lines = [i for i in char_lines if len(i) != 0]

        for i in char_lines:
            print(' ' * (flag + 3) + i)

    except:
        print("Can't Say...!! Give something much more easier to Ms.Kitty...")


def meow(args):

    try:

        text_width = string_processing(args)
        flag = text_width

        print(' ' * (flag + 5) + '\\')
        print(' ' * (flag + 6) + '\\')
        print(' ' * (flag + 7) + '\\')
        print(' ' * (flag + 8) + '\\')

        char_lines = Meow.split('\n')
        char_lines = [i for i in char_lines if len(i) != 0]

        for i in char_lines:
            print(' ' * (flag + 5) + i)

    except:
        print("Can't Say...!! Give something much more easier to Mr.Meow...")


def milk(args):

    try:

        text_width = string_processing(args)
        flag = text_width

        print(' ' * (flag + 5) + '\\')
        print(' ' * (flag + 6) + '\\')
        print(' ' * (flag + 7) + '\\')
        print(' ' * (flag + 8) + '\\', end='')

        char_lines = Milk.split('\n')
        char_lines = [i for i in char_lines if len(i) != 0]

        for i in char_lines:
            print(' ' * (flag + 5) + i)

    except:
        print("Can't Say...!! Give something much more easier to Mr.Milk...")


def pig(args):

    try:

        text_width = string_processing(args)
        flag = text_width

        print(' ' * (flag + 5) + '\\')
        print(' ' * (flag + 6) + '\\')
        print(' ' * (flag + 7) + '\\')
        print(' ' * (flag + 8) + '\\')

        char_lines = Pig.split('\n')
        char_lines = [i for i in char_lines if len(i) != 0]

        for i in char_lines:
            print(' ' * (flag + 5) + i)

    except:
        print("Can't Say...!! Give something much more easier to Mr.Pig...")


def stegosaurus(args):

    try:

        text_width = string_processing(args)
        flag = text_width

        print(' ' * (flag + 5) + '\\')
        print(' ' * (flag + 6) + '\\')
        print(' ' * (flag + 7) + '\\')
        print(' ' * (flag + 8) + '\\', end='')

        char_lines = Stegosaurus.split('\n')
        char_lines = [i for i in char_lines if len(i) != 0]

        for i in char_lines:
            print(' ' * (flag - 3) + i)

    except:
        print("Can't Say...!! Give something much more easier to"
              "Mr.stegosaurus...")


def stimpy(args):

    try:

        text_width = string_processing(args)
        flag = text_width

        print(' ' * (flag + 5) + '\\')
        print(' ' * (flag + 6) + '\\')
        print(' ' * (flag + 7) + '\\')
        print(' ' * (flag + 8) + '\\', end='')

        char_lines = Stimpy.split('\n')
        char_lines = [i for i in char_lines if len(i) != 0]

        for i in char_lines:
            print(' ' * (flag + 4) + i)

    except:
        print("Can't Say...!! Give something much more easier to Mr.Stimpy...")


def turkey(args):

    try:

        text_width = string_processing(args)
        flag = text_width

        print(' ' * (flag + 5) + '\\')
        print(' ' * (flag + 6) + '\\')
        print(' ' * (flag + 7) + '\\')
        print(' ' * (flag + 8) + '\\')

        char_lines = Turkey.split('\n')
        char_lines = [i for i in char_lines if len(i) != 0]

        for i in char_lines:
            print(' ' * (flag - 3) + i)

    except:
        print("Can't Say...!! Give something much more easier to Mr.Turkey...")


def turtle(args):

    try:
        text_width = string_processing(args)
        flag = text_width

        print(' ' * (flag + 5) + '\\')
        print(' ' * (flag + 6) + '\\')
        print(' ' * (flag + 7) + '\\')
        print(' ' * (flag + 8) + '\\', end='')

        char_lines = Turtle.split('\n')
        char_lines = [i for i in char_lines if len(i) != 0]

        for i in char_lines:
            print(' ' * (flag - 3) + i)

    except:
        print("Can't Say...!! Give something much more easier to Mr.Turtle...")


def tux(args):

    text_width = string_processing(args)
    flag = text_width

    print(' ' * (flag + 5) + '\\')
    print(' ' * (flag + 6) + '\\')
    print(' ' * (flag + 7) + '\\', end='')

    char_lines = Tux.split('\n')
    char_lines = [i for i in char_lines if len(i) != 0]

    for i in char_lines:
        print(' ' * flag + i)


chars = [beavis, cheese, daemon, cow, dragon, ghostbusters, kitty, meow, milk,
         pig, stegosaurus, stimpy, turkey, turtle, tux]

char_names = ['beavis', 'cheese', 'daemon', 'cow', 'dragon', 'ghostbusters',
              'kitty', 'meow', 'milk', 'pig', 'stegosaurus', 'stimpy',
              'turkey', 'turtle', 'tux']


def cli():

    if '--version' in sys.argv[1:]:
        print(__version__)
        exit(0)

    cow(' '.join(sys.argv[1:]))
