Cowsay
******

A python API/console script for the famous cowsay-linux. 

cowsay for GNU/Linux was initially written in perl by Tony Monroe (tony@nog.net), with suggestions from Shannon Appel (appel@CSUA.Berkeley.EDU) and contributions from Anthony Polito (aspolito@CSUA.Berkeley.EDU).

For python by Vaasu Devan S <vaasuceg.96@gmail.com>

Github Url https://www.github.com/VaasuDevanS

Installation
************

>>> python -m pip install cowsay
>>> python3 -m pip install cowsay

Importing the Package
=============================================

>>> import cowsay

Basic Information
******************

Original Author---> Tony Monroe (tony@nog.net)       # Thanks to him... !

For Python     ---> Vaasu Devan S

Email          ---> vaasuceg.96@gmail.com

__version__    ---> 1.0
            
       
Available Characters for python are:

['beavis', 'cheese', 'daemon', 'cow', 'dragon', 'ghostbusters', 'kitty', 'meow', 'milk', 'stegosaurus', 'stimpy', 'turkey', 'turtle', 'tux']

             
syntax:-

>>> import cowsay 
>>> cowsay.<character-name>(text-message)

(or)

>>> from cowsay import *
>>> <character-name>(text-message)

Example:-

>>> import cowsay
>>> cowsay.tux("Python is fun")


This will bring the tux character and will say the message passed as arguments.


**cowsay.chars** contains all the function names.

**cowsay.char_names** contains all the character names as strings.

**cowsay.about()** will display the basic info on how to use this module.
