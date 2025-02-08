# localGlobalDemo.py
# spring 2025
# prof. lehman
#
# demonstrates local vs global variables

# str, int, and float values are passed to
# functions by value ie. a copy
#
# Changes to the variable in the function will not
# affect the variable in the main section
# It is generally best to use different
# variable names in order to remember that
# the argument variable is a different memory
# location than the variable in main
#
# Global copies of variables can be used, but it is
# generally best to avoid global variables in functions.
#

# x is passed by value ie. a copy
def doubleIt( x ):  
    """ doubles x """  
    print("in function doubleIt local x =", x)
    x = x * 2
    print("in function doubleIt local x =", x)

# y is passed by value ie. a copy
def doubleIt2(y):
    """ returns y doubled """
    print("in function doubleIt2 local y =", y)
    y = y * 2
    print("in function doubleIt2 local y =", y)
    return y

# z use global value z
def doubleIt3():
    global z  # use z from main ie. global variable
    #z = 300 # what happens if you remove previous line and uncomment this line?
    print("in function doubleIt3 global z =", z)
    z = z * 2
    print("in function doubleIt3 global z =", z)


# main
x = 2
print("main x =", x)
doubleIt(x)  # call function doubleIt
print("main x =", x)  # x will still be 2
print()
print()

x = 20
print("main x =", x)
x = doubleIt2(x)  # call function doubleIt2 and assign x to return value
print("main x =", x)  # x has now changed
print()
print()

z = 200
print("main z =", z)
doubleIt3()  # call function doubleIt3
print("main z =", z)  # z has now changed
