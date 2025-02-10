
# in_class_feb_10.py
# prof. lehman
# spring 2025
# demonstrates how to call functions

# given the following functions
def print_winner( name ):
    print(f"The winner is {name}!")
    
def return_winner( name ):
    return f"The winner is {name}"


# Part 1.  call print winner
print_winner("the Eagles")
print_winner("Bob")
print_winner("You")
print()
print()

# Part 2. call function and print result
print( return_winner("Chiefs") )

# Part 3. call function and store result in variable, then print it
msg = return_winner("Kyle")
print( msg )
print()
print()


#Part 4. function that determines the largest of three values
def biggest_of_three_print(a, b, c):
    big = a
    
    if b > big:
        big = b
        
    if c > big:
        big = c
        
    print( big )

# call function that does not return a value
biggest_of_three_print(100, 50, 25 ) #100
biggest_of_three_print(100, 150, 25 ) #150    
biggest_of_three_print(100, 150, 250 ) #250
biggest_of_three_print(50, 50, 50 ) #50
print()
print()

#Part 5.
# function that takes three values and returns largest
def biggest_of_three(a, b, c):
    big = a
    
    if b > big:
        big = b
        
    if c > big:
        big = c
        
    return big


# call and print
print( biggest_of_three(100, 50, 25 ) )

# call and store, then print
largest = biggest_of_three(100, 50, 25 )
print("largest was", largest)

if largest >= 100:
    print("over 100")
else:
    print("not over 100")
    
# call from within if statement
if biggest_of_three(100, 50, 25 ) >= 100:
    print("over 100")
else:
    print("not over 100")
    

print()
print()

# function that returns True or False
def valid_length( password ):
    if len(password) >= 8:
        return True
    else:
        return False
    
pw = input("Enter Password: ")

if valid_length(pw) == True:
    print("valid length")
else:
    print("invalid length - need 8 characters")
    
# because valid_length returns True or False " == True" is not needed
if valid_length(pw):
    print("valid length")
else:
    print("invalid length - need 8 characters") 
    
    
    