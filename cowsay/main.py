


#  Developer : Vaasu Devan S
#  Email     : vaasuceg.96@gmail.com
#              www.github.com/VaasuDevanS

#  cowsay for GNU/Linux was initially written in perl by Tony Monroe (tony@nog.net), with suggestions from Shannon Appel (appel@CSUA.Berkeley.EDU) and contributions from Anthony Polito (aspolito@CSUA.Berkeley.EDU).

# ___________________________________________________________________________________________________________________________ #

# Characters.py contains the Ascii code for the characters.
# Initial cowsay will have lots of characters than this.. But these are my favourite.

from __future__ import print_function
import re
import sys

flg=[]

Beavis =  '''
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


Cow = '''

   ^__^                             
   (oo)\_______                   
   (__)\       )\/\             
       ||----w |           
       ||     ||  
       
       '''


Dragon = ''' 

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

Meow = """

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


Turkey = '''

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

def about():
    
    print('''
    
             Original Author---> Tony Monroe (tony@nog.net)       # Thanks to him... !
             For Python     ---> Vaasu Devan S
             Email          ---> vaasuceg.96@gmail.com
             __version__    ---> 2.0.3
             
             visit my github page @ www.github.com/VaasuDevanS
             
             Cowsay for GNU/Linux is very very famous. 
			 It would be fun and cool to have those characters in python..
             
             Available Characters (in python): 
             ==============================================
             |'beavis'     'dragon'         'tux'         |
             |'turtle'     'ghostbusters'   'turkey'      |
             |'cheese'     'kitty'          'stegosaurus' |
             |'daemon'     'meow'           'stimpy'      |
             |'cow'        'milk'                         |
             ==============================================
             
             syntax:-
             
             >>> import cowsay 
             >>> cowsay.<character-name>(text-message)
             
                            (or)
                            
             >>> from cowsay import *
             >>> <character-name>(text-message)
             
             Example:-
             
             >>> import cowsay
             >>> cowsay.tux("Python is fun")
        
                 _______________            
                < Python is fun >
                -----------------
                               \\
                                \\
                                 \\
                                   .--.
                                  |o_o |
                                  |:_/ |
                                //   \\ \\
                                (|     | )
                               /'\\_   _/`\\
                               \\___)=(___/
                               
                               
            Enjoy coding with python and cowsay   :)
    
        ''')

__version__ = '2.0.3'
__name__ = 'cowsay' #For python


def String_processing(args):

    args=str(args)
    length=len(args)
    lines=args.split("\n")
    lines=[i.strip() for i in lines]
    lines=[i for i in lines if len(i)!=0]
    length=len(lines)
    
    if length==1:
        flag=len(lines[0])
        if flag<50:
            print("  "+"_"*flag)
            print("< "+lines[0]+" "*(flag-len(lines[0])+1)+">")
            print("  "+"="*flag)
            flg.append(flag)
        else:
            args=list("".join(lines[0]))
            for j,i in enumerate(args):
                if j%50==0:
                    args.insert(j,"\n")
            String_processing("".join(args))
               
    else:
        flag=len(max(lines,key=len))
        if all(len(i)<50 for i in lines): 
            print("  "+"_"*flag)
            print(" /"+" "*flag+"\\")            
            for i in lines:
                print("| "+i+" "*(flag-len(i)+1)+"|")
            print(" \\"+" "*flag+"/")
            print("  "+"="*flag)
            flg.append(flag)                    
        else:
            new_lines=[]
            for i in lines:
                if len(i)>50:
                    args=list("".join(i))
                    for j,i in enumerate(args):
                        if j%50==0:
                            args.insert(j,"\n") 
                    new_lines.append("".join(args))
                else:
                    new_lines.append(i+"\n")
            String_processing("".join(new_lines))
                    
                    
# Functions start here..        
    
def beavis(args):

    try : 
        String_processing(args)
        flag=flg[-1]
            
        print(" "*(flag+5)+"\\")
        print(" "*(flag+6)+"\\")
        print(" "*(flag+7)+"\\")
    
        char_lines=Beavis.split('\n')
        char_lines=[i for i in char_lines if len(i)!=0]
    
        for i in char_lines:
            print(" "*flag+i)

    except : print("Can't Say...!! Give something much more easier to Mr.Beavis...")
    

def cheese(args):

    try : 
                
        String_processing(args)
        flag=flg[-1]
            
        print(" "*(flag+5)+"\\")
        print(" "*(flag+6)+"\\")
        print(" "*(flag+7)+"\\")
        print(" "*(flag+8)+"\\",end='')
    
        char_lines=Cheese.split('\n')
        char_lines=[i for i in char_lines if len(i)!=0]
    
        for i in char_lines:
            print(" "*(flag+5)+i)

    except : print("Can't Say...!! Give something much more easier to Mr.Cheese...")
       
   

def daemon(args):

    try : 
                
        String_processing(args)
        flag=flg[-1]
            
        print(" "*(flag+5)+"\\")
        print(" "*(flag+6)+"\\")
        print(" "*(flag+7)+"\\")
        print(" "*(flag+8)+"\\",end='')
    
        char_lines=Daemon.split('\n')
        char_lines=[i for i in char_lines if len(i)!=0]
    
        for i in char_lines:
            print(" "*(flag-3)+i)

    except : print("Can't Say...!! Give something much more easier to Mr.Daemon...") 
        

def cow(args):

    try : 
                
        String_processing(args)
        flag=flg[-1]
            
        print(" "*(flag+5)+"\\")
        print(" "*(flag+6)+"\\")
    
        char_lines=Cow.split('\n')
        char_lines=[i for i in char_lines if len(i)!=0]
    
        for i in char_lines:
            print(" "*(flag+5)+i)

    except : print("Can't Say...!! Give something much more easier to Mr.Cow...")    
        

def dragon(args):

    try : 
                
        String_processing(args)
        flag=flg[-1]
            
        print(" "*(flag+5)+"\\")
        print(" "*(flag+6)+"\\")
        print(" "*(flag+7)+"\\")
        print(" "*(flag+8)+"\\",end='')
    
        char_lines=Dragon.split('\n')
        char_lines=[i for i in char_lines if len(i)!=0]
    
        for i in char_lines:
            print(" "*(flag+3)+i)

    except : print("Can't Say...!! Give something much more easier to Mr.Dragon...")  
    
    

def ghostbusters(args):

    try : 
                
        String_processing(args)
        flag=flg[-1]
            
        print(" "*(flag+5)+"\\")
        print(" "*(flag+6)+"\\")
        print(" "*(flag+7)+"\\")
        print(" "*(flag+8)+"\\",end='')
    
        char_lines=Ghostbusters.split('\n')
        char_lines=[i for i in char_lines if len(i)!=0]
    
        for i in char_lines:
            print(" "*(flag-3)+i)

    except : print("Can't Say...!! Give something much more easier to Mr.Ghostbusters...")  
        

def kitty(args):

    try : 
                
        String_processing(args)
        flag=flg[-1]
            
        print(" "*(flag+5)+"\\")
        print(" "*(flag+6)+"\\")
        print(" "*(flag+7)+"\\")
        print(" "*(flag+8)+"\\")
    
        char_lines=Kitty.split('\n')
        char_lines=[i for i in char_lines if len(i)!=0]
    
        for i in char_lines:
            print(" "*(flag+3)+i)

    except : print("Can't Say...!! Give something much more easier to Ms.Kitty...")
        

def meow(args):

    try : 
                
        String_processing(args)
        flag=flg[-1]
            
        print(" "*(flag+5)+"\\")
        print(" "*(flag+6)+"\\")
        print(" "*(flag+7)+"\\")
        print(" "*(flag+8)+"\\")
    
        char_lines=Meow.split('\n')
        char_lines=[i for i in char_lines if len(i)!=0]
    
        for i in char_lines:
            print(" "*(flag+5)+i)

    except : print("Can't Say...!! Give something much more easier to Mr.Meow...")  
    
    

def milk(args):

    try : 
                
        String_processing(args)
        flag=flg[-1]
            
        print(" "*(flag+5)+"\\")
        print(" "*(flag+6)+"\\")
        print(" "*(flag+7)+"\\")
        print(" "*(flag+8)+"\\",end='')
    
        char_lines=Milk.split('\n')
        char_lines=[i for i in char_lines if len(i)!=0]
    
        for i in char_lines:
            print(" "*(flag+5)+i)

    except : print("Can't Say...!! Give something much more easier to Mr.Milk...")    
        
    

def stegosaurus(args):

    try : 
                
        String_processing(args)
        flag=flg[-1]
            
        print(" "*(flag+5)+"\\")
        print(" "*(flag+6)+"\\")
        print(" "*(flag+7)+"\\")
        print(" "*(flag+8)+"\\",end='')
    
        char_lines=Stegosaurus.split('\n')
        char_lines=[i for i in char_lines if len(i)!=0]
    
        for i in char_lines:
            print(" "*(flag-3)+i)

    except : print("Can't Say...!! Give something much more easier to Mr.stegosaurus...")
    
    

def stimpy(args):

    try : 
                
        String_processing(args)
        flag=flg[-1]
            
        print(" "*(flag+5)+"\\")
        print(" "*(flag+6)+"\\")
        print(" "*(flag+7)+"\\")
        print(" "*(flag+8)+"\\",end='')
    
        char_lines=Stimpy.split('\n')
        char_lines=[i for i in char_lines if len(i)!=0]
    
        for i in char_lines:
            print(" "*(flag+4)+i)

    except : print("Can't Say...!! Give something much more easier to Mr.Stimpy...")  
        

def turkey(args):

    try : 
                
        String_processing(args)
        flag=flg[-1]
            
        print(" "*(flag+5)+"\\")
        print(" "*(flag+6)+"\\")
        print(" "*(flag+7)+"\\")
        print(" "*(flag+8)+"\\")
    
        char_lines=Turkey.split('\n')
        char_lines=[i for i in char_lines if len(i)!=0]
    
        for i in char_lines:
            print(" "*(flag-3)+i)

    except : print("Can't Say...!! Give something much more easier to Mr.Turkey...")    
    
    

def turtle(args):

    try : 
                
        String_processing(args)
        flag=flg[-1]
            
        print(" "*(flag+5)+"\\")
        print(" "*(flag+6)+"\\")
        print(" "*(flag+7)+"\\")
        print(" "*(flag+8)+"\\",end='')
    
        char_lines=Turtle.split('\n')
        char_lines=[i for i in char_lines if len(i)!=0]
    
        for i in char_lines:
            print(" "*(flag-3)+i)

    except : print("Can't Say...!! Give something much more easier to Mr.Turtle...")  
    
    

def tux(args):

    #try : 
                
        String_processing(args)
        flag=flg[-1]
            
        print(" "*(flag+5)+"\\")
        print(" "*(flag+6)+"\\")
        print(" "*(flag+7)+"\\",end='')
    
        char_lines=Tux.split('\n')
        char_lines=[i for i in char_lines if len(i)!=0]
    
        for i in char_lines:
            print(" "*(flag)+i)

    #except : print("Can't Say...!! Give something much more easier to Mr.Tux...")    
     

chars = [beavis , cheese , daemon , cow , dragon , ghostbusters , kitty , meow , milk , stegosaurus , stimpy , turkey , turtle , tux]

char_names = ['beavis', 'cheese', 'daemon', 'cow', 'dragon', 'ghostbusters', 'kitty', 'meow', 'milk', 'stegosaurus', 'stimpy', 'turkey', 'turtle', 'tux']
    
def cli():
    if '--version' in sys.argv[1:]:
        print(__version__)
        exit(0)
    cow(' '.join(sys.argv[1:]))
# End of File #
