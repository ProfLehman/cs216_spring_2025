# -----------------------------------------------------------------------
#
#        file: Animal.py
#
#      Author: Prof. Lehman
#        Date: March 17, 2025
#
# Description: 'Animal' class with attributes for type, name, and sound,
#               getters and setters for each attribute,
#               a 'speak' method to print the sound,
#               a '__str__' method for formatted output.
#
#               Main demonstrates object creation, 
#               method usage, and attribute modification.
#              
# -----------------------------------------------------------------------


class Animal:

    # constructor
    def __init__(self, animal_type="unknown", name="unknown", sound="unknown"):
        self.animal_type = animal_type
        self.name = name
        self.sound = sound
    
    # Getters and Setters
    def get_animal_type(self):
        return self.animal_type
    
    def set_animal_type(self, animal_type):
        self.animal_type = animal_type
    
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
    
    def get_sound(self):
        return self.sound
    
    def set_sound(self, sound):
        self.sound = sound
    
    # other methods
    def speak(self):
        print( self.name, "says", self.sound)
    
    def __str__(self):
        return f"Animal Type: {self.animal_type}, Name: {self.name}, Sound: {self.sound}"


# --- main ---
if __name__ == "__main__":
  
    # instance with initial values specified
    shep = Animal("Dog", "Shep", "Woof")
    print(shep)
    shep.speak()
    print()

    # instance using default values
    maynard = Animal()
    print( maynard )
    maynard.speak()
    print()

    # set values
    maynard.set_animal_type("cat")
    maynard.set_name("Maynard")
    maynard.set_sound("meow, meow ...")
    print(maynard)
    maynard.speak()
    print()
    
    # list of animals
    harvey = Animal("rabbit", "Harvey", "nothing")
    
    pets = [shep, maynard, harvey]
    for pet in pets:
        #pet.speak()
        print( pet )






