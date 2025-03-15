import random

# Dice.py
# spring 2024
# lehman
# demonstrates OOP with class variable maxRolled
# class variables are "shared" among all instances of the class

class Dice:

    # variables declared inside class and outside of functions
    # are shared between all instances of the class
    # this is also called a class attrribute
    maxRolled = 0

    # constructors setup the instance variables ie. self.attribute
    # each instance has it's own copy of the attributes
    def __init__(self, init_id="undefined", init_value=1):
        self.id = init_id
        self.value = init_value
        #self.set_value( init_value ) #could error check using set_value function

    def roll(self):
        self.value = random.randint(1, 6)
        if self.value > Dice.maxRolled:
            Dice.maxRolled = self.value # note reference Dice for class variable

    # "getters" return attributes
    def get_value(self):
        return self.value

    # "setters" update or change ie. set attributes
    def set_value(self, value):
        if value >= 1 and value <= 6:
            self.value = value #change value if valid
        else:
            print("Error: Value must be between 1 and 6")
            self.value = 1 #default to 1
            
    # "setter"
    def set_id(self, id):
        self.id = id
    
    # "getter"
    def get_maxRolled(self):
        return Dice.maxRolled
    
    # special method that defines how an object will be printed
    def __str__(self):
        return f"dice {self.id} value is {self.value}."
   
   
# *******************
# *** main ***
# *******************

# note: if this file is "run", then the following main is used
if __name__ == "__main__":

    # Create a new dice
    white = Dice("white", 8)
    print( white.value )
    print( white )
    print()
    
    white.value = 16
    print( white )
    white.set_value( 16 )
    print( white )
    print()
    print()
    
    red = Dice()
    red.set_id("red dice")
    blue = Dice("blue dice", 4)

    print( red )
    print( blue )
    print()
    print( "red, max rolled for all classes", red.get_maxRolled() )
    print( "blue, max rolled for all classes", blue.get_maxRolled() )
    print()

    red.roll()
    print( red )
    print()

    print( "red, max rolled for all classes", red.get_maxRolled() )
    print( "blue, max rolled for all classes", blue.get_maxRolled() )



    