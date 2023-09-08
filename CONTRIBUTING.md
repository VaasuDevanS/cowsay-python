# Adding a new Character
1. Choose the new character and first test it's output using `cowsay.draw` method
   ```
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
   
   >>> cowsay.draw('Hello I am Scorpion', scorpion)
     ___________________
    | Hello I am Scorpion |
     ===================
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
