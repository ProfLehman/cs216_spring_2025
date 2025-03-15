# needed to use Dice class defined in Dice.py

from Dice import *

# Dice_Test.py
# spring 2025
# lehman
# demonstrates using Dice class defined in a separate file Dice.py

# *** main ***
red = Dice("Red Dice", 3)
print( red )
print()

red.roll()
print( red )
print( red.get_value() )
print()

# note: notice that the main is not run in Dice.py
#       as it uses if __name__ == "__main__":