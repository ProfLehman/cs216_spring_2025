# Student_final.py
#
# Spring 2025
# Prof. Lehman
#
# in-class exercise (with answers)
# demonstrates Student object
#
# 
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
#  data defines the information we store about an object
#  methods describe "actions"
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
    def __init__(self, name="unknown", age=-1, major="undeclared"):
        print("in constructor")
        self.name = name
        self.age = age
        self.major = major
  
    # "setters" allow data to be changed
    def set_name(self, new_name):
        self.name = new_name
        
    def set_age(self, new_age):
        if new_age >= 0:
            self.age = new_age
    
    def set_major(self, new_major):
        self.major = new_major


    # "getters" allow data to be access individualy
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def get_major(self):
        return self.major
    
    
    # other methods provide functionality unique to the object
    def can_vote(self):
        if self.age >= 18:
            return True
        else:
            return False
    
    
    # display object 
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Major: {self.major}")   
        
    # allows object to be displayed using print
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Major: {self.major}"
    
   # *** end of class definition ***


# *** main ***

# 1.
# create a Student instance using the default constructor
# ie. no starting data given
alice = Student()

# 2.
# display the instance using the display method
alice.display()

# 3.
# print the instance - calls str method
print( alice )
print()

# 4.
# create a Student instance using the alternate constructor
# ie. starting data given
bob = Student("Bob", 20, "computer science")

# 5.
# display the instance using the display method
bob.display()

# 6.
# print the instance - calls str method
print( bob )
print()

# 7.
# update the name and age for the first student
# using the "setters"
alice.set_name("Alice Anderson")
alice.set_age( 7 )
alice.set_major("data anlytics")
print( alice)
print()

# 8.
# display the data for both students using the "getters"
print( alice.get_name() )
print( alice.get_age() )
print( alice.get_major() )

print( bob.get_name() )
print( bob.get_age() )
print( bob.get_major() )
print()

# 9.
# demonstrate the can_vote method
print( alice.can_vote() )
print( bob.can_vote() )
print()

if alice.can_vote():
    print("Alice can vote")
else:
    print("Alice can not vote")
    
print()

# 10.
# add the field major to the student class,
# update the class to support this new field,
# and update the demo in main for the two instances










