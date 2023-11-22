Dice rolling simulator

Function roll_die():
    return random number between 1 and 6

Function  dice_rolling_simulator():
    Display "Welcome to the Dice Rolling Simulator!"

    Repeat:
        Display "Press Enter to roll the die..."
        Wait for user to press Enter
       Initialise the score as 0
        result = roll_die()
        Display "You rolled: " + result
        Add the result to the score variable

        Display "Roll again? (yes/no):"
        Get user input and convert to lowercase

    If the user input is not 'yes'
    Display The score and "Thanks for rolling! Goodbye."
