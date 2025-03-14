# OOP - Object Oriented Programming
#
# main way organize code
#    also used by 
#    C++  (C language extended with objects)
#    Java, C#, Swift, JavaScript, PHP, etc...
#
# manage complexity
# re-use code
# more "natural" thinking about code as "objects"
#
# objects have "properties" or "attributes"
#  data that defines and describes the object
#
# define objects in a "class"
#
#  data and methods describe "actions"
#
#  group data and methods (functions) encapsulation
#
#  each "instance" has its own copy of data
#   but it shares methods
#
#  class
#  data
#  methods

# class describes object
class Student:
    
    # constructor - special method that sets-up object
    # declare and initialize our data for object
    def __init__(self, name="unknown", age=-1):
        print("in constructor")
        self.name = name
        self.age = age
  
    # "setters" allow data to be changed
    def set_name(self, new_name):
        self.name = new_name
        
    def set_age(self, new_age):
        self.age = new_age
    
    
    # "getters" allow data to be access individualy
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    
    # other methods provide functionality unique to the object
    def canVote(self):
        if self.age >= 18:
            return True
        else:
            return False
    
    
    # display object 
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")   
        
    # allows object to be displayed using print
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"
    
   # *** end of class definition ***


# *** main ***
alice = Student()
print( alice )


