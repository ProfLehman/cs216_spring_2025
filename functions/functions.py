
# functions.py
# spring 2025
# prof. lehman

# sample functions overview

# Reasons to Use Functions in Python

# 1. Code Reusability
#    - Functions allow you to write code once and reuse it multiple times, reducing redundancy.

# 2. Modularity & Organization
#    - Breaking a program into smaller functions makes it easier to read, maintain, and debug.

# 3. Simplifies Debugging & Testing
#    - Debugging is easier because you can isolate specific functions rather than searching through a large block of code.

# 4. Improves Readability
#    - Code is more readable when it is divided into meaningful functions rather than a long script.

# 5. Encapsulation
#    - Functions encapsulate logic, reducing unintended interactions between different parts of a program.

# 6. Avoids Repetition (DRY Principle)
#    - The "Don't Repeat Yourself" (DRY) principle encourages reducing duplicate code by using functions.

# 7. Enables Code Abstraction
#    - A function hides the implementation details and allows the user to use it without knowing how it works internally.

# 8. Facilitates Collaboration
#    - In larger projects, multiple developers can work on different functions without interfering with each other’s code.

# 9. Allows Parameterization
#    - Functions can take arguments, making them flexible and adaptable to different situations.

# 10. Supports Recursive Solutions
#     - Functions allow recursion, which can be useful for solving problems that involve repetitive structures like trees or factorial calculations.

# 11. Memory Efficiency
#     - Functions help optimize memory usage by reducing the number of variables and unnecessary operations in the global scope.

# 12. Easier Scalability
#     - Well-structured code using functions is easier to extend and modify as the project grows.



# ************************************************************
# Functions with no arguments and no return
# can be used to display text.
# They can also be used to perform a section of code  

def greet():
    print("Hello, welcome to Python functions!")

def print_heading():
    print("+-----------------------------+")
    
def check_can_vote():
    age = int( input("Enter age: ") ) 
    if age >= 18:
        print("yes, can vote")
    else:
        print("sorry, must be 18+ to vote")
        
# Function calls use name of function with()
greet()
print_heading()
check_can_vote()

print()
print()

# ************************************************************
# Functions may have arguments and no return
# can be used to process arguments and display text.

def greet_person(name):
    print(f"Hello, {name}! Welcome to Python functions!")

def print_heading(width):
    print("+", end="")
    print( "-" * (width-2), end="") #fancy way to repeat text
    print("+")

def can_vote(age):
    if age >= 18:
        print("yes, can vote")
    else:
        print("sorry, must be 18+ to vote")

def print_sum(a, b):
    print(f"The sum of {a} and {b} is {a + b}")

def printStars( N ):
    count = 0
    while count < N:
        print("*", end="")
        count = count + 1
    print()
    
# function calls must include a value for the argument
greet_person("Norman")
greet_person("Dr. Emberton")

print_heading( 10 )
print_heading( 20 )

can_vote( 17 )
can_vote( 22 )

print_sum(3, 4)
print_sum(-900, -765)

printStars( 9 )
printStars( 3 )

print()
print()

# ************************************************************
#Functions may only have a return statement

def getMascot():
    return "Foresters"

def getFeetInMile():
    return 5280

print( getMascot() )
print( getFeetInMile() )
print()
print()


# Functions may have arguments and a return
# When a function returns a value it must be stored or printed

def greeting(name):
    return f"Hello, {name}! Welcome to Python functions!"

def multiply(a, b):
    return a * b

def can_vote(age):
    if age >= 18:
        return True
    else:
        return False

# print result of function call
print( greeting("Alice") )

# store result of function call
msg = greeting("Bob")
print( msg )

# use function in if statement
if can_vote(17) == True:
    print("yup, can vote")
else:
    print("nope, can't vote yet")
    
print( multiply(2,8) )

# --- end ---






