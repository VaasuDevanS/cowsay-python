# Adding a new Character
1. Choose the new character and first test it's output using `cowsay.draw()` method
   ```console
   # https://www.asciiart.eu/animals
   
   >>> scorpion = r"""
    \
     \
      \
       ___    ___
      ( _<    >_ )
      //        \\
      \\___..___//
       `-(    )-'
         _|__|_
        /_|__|_\
        /_|__|_\
        /_\__/_\
         \ || /  _)
           ||   ( )
           \\___//
            `---'
   """
   
   >>> lorem: str = (
        'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam'
        'nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat,'
        'sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum.'
   )
   
   >>> cowsay.draw(lorem, scorpion)
     _________________________________________________
    /                                                 \
   | Lorem ipsum dolor sit amet, consetetur sadipscing |
   |  elitr, sed diamnonumy eirmod tempor invidunt ut  |
   | labore et dolore magna aliquyam erat,sed diam vol |
   | uptua. At vero eos et accusam et justo duo dolore |
   | s et ea rebum.                                    |
    \                                                 /
     =================================================
                                                     \
                                                      \
                                                       \
                                                        ___    ___
                                                       ( _<    >_ )
                                                       //        \\
                                                       \\___..___//
                                                        `-(    )-'
                                                          _|__|_
                                                         /_|__|_\
                                                         /_|__|_\
                                                         /_\__/_\
                                                          \ || /  _)
                                                            ||   ( )
                                                            \\___//
                                                             `---'

   ```
2. Fork the repo here https://github.com/VaasuDevanS/cowsay-python/fork   
3. Once the character and it's output are finalized, add the character in 
   `cowsay/characters.py` and it's expected solution in `cowsay/tests/solutions.py`
4. Add the character name in `test_char_names` function in `cowsay/tests/test_api.py`
5. Update `README.md` (`More Characters` section)
6. Run the test suite locally using `pytest`
7. Create a `Pull Request`


# Updating the codebase
Feel free to create a pull request to make any desired changes 
to the code without breaking the API :-)


# Adding new functionality
Feel free to create a pull request if you want to add more
functionality (like customizations to each characters, ...)
